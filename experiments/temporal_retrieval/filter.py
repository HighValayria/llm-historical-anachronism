"""Deterministic, metadata-only admission checks for a Temporal RAG probe.

This module deliberately does not retrieve documents or call a model.  It only
decides whether a *candidate already supplied by a caller* may enter a
cutoff-bounded candidate set.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Mapping


DATE_FIELDS = (
    "document_date",
    "event_date",
    "knowledge_valid_from",
    "knowledge_valid_to",
)


@dataclass(frozen=True)
class AdmissionDecision:
    """A reproducible candidate admission decision, including its reason."""

    allowed: bool
    reason: str


def _parse_date(value: object, field: str) -> date | None:
    if value is None or value == "":
        return None
    if not isinstance(value, str):
        raise ValueError(f"{field} must be an ISO-8601 YYYY-MM-DD string or null")
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f"{field} is not an ISO-8601 YYYY-MM-DD date") from error


def admit_candidate(
    candidate: Mapping[str, object], cutoff_date: str, *, unknown_date_policy: str = "exclude"
) -> AdmissionDecision:
    """Admit a candidate only when its temporal metadata is compatible.

    ``document_date``, ``event_date``, and ``knowledge_valid_from`` must not be
    after ``cutoff_date``.  ``knowledge_valid_to``, when supplied, must not be
    before the cutoff: an expired knowledge claim is not eligible at that time.
    The cutoff itself is inclusive.  Under the safe default, an unknown value in
    any declared date field excludes the candidate rather than silently letting
    future material into the set.
    """

    if unknown_date_policy not in {"exclude", "allow"}:
        raise ValueError("unknown_date_policy must be 'exclude' or 'allow'")
    cutoff = _parse_date(cutoff_date, "cutoff_date")
    assert cutoff is not None

    parsed = {field: _parse_date(candidate.get(field), field) for field in DATE_FIELDS}
    unknown = [field for field, value in parsed.items() if value is None]
    if unknown and unknown_date_policy == "exclude":
        return AdmissionDecision(False, f"unknown_date:{','.join(unknown)}")

    for field in ("document_date", "event_date", "knowledge_valid_from"):
        value = parsed[field]
        if value is not None and value > cutoff:
            return AdmissionDecision(False, f"future_{field}")

    valid_to = parsed["knowledge_valid_to"]
    if valid_to is not None and valid_to < cutoff:
        return AdmissionDecision(False, "expired_knowledge_valid_to")

    return AdmissionDecision(True, "admitted")
