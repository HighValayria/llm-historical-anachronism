# Public Release Audit — G7-C Progress Candidate

Date: 2026-11-05
Branch: `public-sync-g7c-20261105`
Base commit: `f2cb1ceaff959f4dbf1a42ad764b5bea2a38bf26`
Result: `p2_security_gate_ready_for_researcher_reapproval_not_pushed`

## History construction

The candidate was cloned from GitHub `main` and branched directly at the verified remote commit. None of the 75 private local commits was cherry-picked or merged. P2 retains the original sanitized commit and adds one versioned, exact-fingerprint security-gate revision.

## Content review

The release delta contains eleven files: the original seven-file sanitized payload plus `.gitleaksignore` and three P2 security-control reports. It contains no newly added workbook, archive, PDF, model output, hidden mapping, record-level adjudication or operational authorization material.

The public status accurately records that the restricted S1 v0.1 view has 20 internal-development records and 30 unscored qualitative references. It also states that Gold is not finalized, independent human review is incomplete, and M2 has not been implemented or run.

## Security and blinding checks

| Check | Result |
|---|---|
| Candidate branch based directly on verified public base | pass |
| Private research commits merged or cherry-picked | none |
| Condition/blind mapping in release delta | none found |
| Raw formal model output in release delta | none |
| Human-review workbook or binary attachment in release delta | none |
| Claim-level label or adjudication dataset in release delta | none |
| Common credential/private-key patterns in release delta | no match |
| Gitleaks v8.30.0 source | official GitHub release; Windows x64 archive matched the official SHA-256 checksum |
| Gitleaks raw control | exactly 2 legacy history and 2 legacy current-tree findings reproduced |
| Gitleaks with exact fingerprints | full history and current tree pass with 0 unhandled findings |
| Same-path synthetic credential | detected; exception is not file- or rule-wide |
| TruffleHog | `not_verified` — unavailable |
| Personal document metadata in release delta | none; no office document is added |

Gitleaks is now verified. TruffleHog remains unavailable, so the audit does not claim cross-tool exhaustive scanning.

## Public verification

- `python -B tests/test_temporal_retrieval_filter.py`: 6 tests passed.
- `python -B -m pytest -q`: 33 tests and 3 subtests passed.
- The temporal filter performs no retrieval, model call or network request.
- Tests requiring private G5–G7 data are intentionally not published. No substitute data was fabricated to make them pass.

## Known limits

- The public tree cannot reproduce the private Baseline outputs, human scoring or G7-C record-level decisions.
- Formal Gold and independent review remain incomplete.
- This candidate publishes no M2 effectiveness result.
- The G5–G7 provenance issue is diagnosed separately in the private repository and is not hidden by this release.

## Approval gate

The P2 candidate is technically suitable for renewed researcher review. Because its commit differs from the previously approved `1755539` candidate, publication requires explicit approval of the new exact commit and updated manifest. No push was performed during P2.
