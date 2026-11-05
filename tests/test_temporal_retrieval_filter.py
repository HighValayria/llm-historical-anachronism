from __future__ import annotations

import unittest
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "experiments" / "temporal_retrieval"))

from filter import admit_candidate  # noqa: E402


def candidate(**overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "document_date": "1900-01-01",
        "event_date": "1899-12-31",
        "knowledge_valid_from": "1899-12-31",
        "knowledge_valid_to": "1900-01-01",
    }
    value.update(overrides)
    return value


class TemporalRetrievalFilterTests(unittest.TestCase):
    def test_cutoff_boundary_is_inclusive_for_all_date_types(self) -> None:
        decision = admit_candidate(candidate(), "1900-01-01")
        self.assertTrue(decision.allowed)
        self.assertEqual("admitted", decision.reason)

    def test_future_document_event_and_validity_start_are_excluded(self) -> None:
        for field in ("document_date", "event_date", "knowledge_valid_from"):
            with self.subTest(field=field):
                decision = admit_candidate(candidate(**{field: "1900-01-02"}), "1900-01-01")
                self.assertFalse(decision.allowed)
                self.assertEqual(f"future_{field}", decision.reason)

    def test_knowledge_expired_before_cutoff_is_excluded(self) -> None:
        decision = admit_candidate(candidate(knowledge_valid_to="1899-12-31"), "1900-01-01")
        self.assertFalse(decision.allowed)
        self.assertEqual("expired_knowledge_valid_to", decision.reason)

    def test_unknown_dates_are_excluded_by_safe_default(self) -> None:
        decision = admit_candidate(candidate(event_date=None), "1900-01-01")
        self.assertFalse(decision.allowed)
        self.assertEqual("unknown_date:event_date", decision.reason)

    def test_unknown_dates_can_only_be_allowed_by_an_explicit_policy(self) -> None:
        decision = admit_candidate(candidate(event_date=None), "1900-01-01", unknown_date_policy="allow")
        self.assertTrue(decision.allowed)

    def test_malformed_dates_and_policy_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            admit_candidate(candidate(document_date="1900/01/01"), "1900-01-01")
        with self.assertRaises(ValueError):
            admit_candidate(candidate(), "1900-01-01", unknown_date_policy="guess")


if __name__ == "__main__":
    unittest.main()
