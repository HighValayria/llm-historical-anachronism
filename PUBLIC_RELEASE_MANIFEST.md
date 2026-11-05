# Public Release Manifest — G7-C Progress Candidate

Prepared: 2026-11-05
Proposed branch: `public-sync-g7c-20261105`
Base: `origin/main` at `f2cb1ceaff959f4dbf1a42ad764b5bea2a38bf26`
Release status: P2 security-gate revision; local candidate only; not pushed; renewed researcher approval required

Parent candidate: `1755539e22f1` (abbreviated). P2 preserves that candidate and adds only the exact Gitleaks exception plus security audit records.

The candidate commit is created after this manifest is finalized. Its SHA is intentionally recorded in the external handoff and audit result rather than embedded here, avoiding a self-referential commit hash.

## Public payload whitelist

| Path | SHA-256 | Source | Publication reason |
|---|---|---|---|
| `README.md` | `c1137caab4f60b67860f53ef8bfd4e60e9a9f1e4a3093e67cddc8d203e12bb4d` | remote README plus sanitized status derived from local G7-C commit `35ac438964b7999cd7dcc9b04b7ff32ee763c6ae` | Corrects the public progress statement without releasing record-level data. |
| `PUBLIC_RESEARCH_STATUS.md` | `98a4d9164dcd11575a993ac32aa0e2d4757ad9367d749d63c3a2ddb29999294a` | aggregate G7-C state and sync audit | Publishes only stage counts, limits and method status. |
| `experiments/temporal_retrieval/README.md` | `69a7253371a3ce499b4c2d1b46f8d280e82abee42d572e18fa3c5ca79518e52c` | commit `5682175992a2e004c78705b10767c00cb1e81cc0` | Documents a generic, zero-call temporal-metadata filter contract. |
| `experiments/temporal_retrieval/filter.py` | `b8745e0c8c27421d6a6c828023daeef3ed1bd6f487bb4575abc2d53fb158776a` | commit `5682175992a2e004c78705b10767c00cb1e81cc0` | Reusable source code containing no model output, labels or historical source text. |
| `tests/test_temporal_retrieval_filter.py` | `9c183a22635e76965c6b4981488579cd3ff78a3c575ecf60d3c225787bc452b9` | commit `5682175992a2e004c78705b10767c00cb1e81cc0` | Six deterministic tests using synthetic dates only. |
| `.gitleaksignore` | `90308926904e70a59afcb925137c2c73cdfb9623f43907eec05b4d7306078860` | P2 legacy-finding triage | Four exact fingerprints: two history findings and their two work-tree equivalents; no value, path, rule or commit-wide exception. |
| `GITLEAKS_LEGACY_FINDINGS_TRIAGE.md` | `08e3147ada23fac83299e63c88f52fee2e836d76d460e2d62baf0cf991711f82` | P2 local contextual audit | Records the two redacted classifications, irreversible digests and account-impact decision. |
| `GITLEAKS_EXCEPTION_RATIONALE.md` | `9f8e4a6f2488876a4fbe73e4b5e9288e4b79f02810ec06e423e87d95fc8386ef` | P2 exception audit | Explains the exact-fingerprint scope and synthetic negative-control result. |
| `PUBLIC_RELEASE_FINAL_GATE.md` | `44e6b870df8ce68919d16212ed7c79a2600342c0fe38f4a935d5c74ca08d11ca` | P2 final gate | Records scan, test, lineage and reapproval status without publishing a suspicious value. |

`PUBLIC_RELEASE_MANIFEST.md` and `PUBLIC_RELEASE_AUDIT.md` are excluded from their own hash table to avoid recursive self-hashing. Their final hashes are recorded in the external handoff.

## Explicit exclusions

The candidate contains no newly added condition mapping, raw model response, human-review workbook, claim-level adjudication, detailed internal label, S2 item, transfer file, authorization record, environment credential or unlicensed historical document. No file from the private G5–G7 data packages is copied.

## Verification summary

- New binary attachments: none.
- Custom credential/secret pattern scan: no match in the candidate delta.
- Gitleaks v8.30.0: official archive checksum verified; exact-exception full-history and current-tree scans pass with zero unhandled findings.
- Gitleaks control: without the exception the scanner reproduces exactly two history and two tree findings; a same-path synthetic credential remains detectable.
- TruffleHog: `not_verified` because the tool is unavailable.
- Temporal-filter tests: 6 passed.
- Public-tree test suite: 33 passed and 3 subtests passed.

## Difference from the complete local research repository

The complete local repository has a private 75-commit research history after the public base. This branch does not cherry-pick that history. It contains the original sanitized publication commit plus one P2 security-gate commit on top of the public base. Internal data, detailed evidence chains and private scoring reproducibility remain outside the candidate.
