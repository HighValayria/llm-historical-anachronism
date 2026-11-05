# Public Release Manifest — G7-C Progress Candidate

Prepared: 2026-11-05
Proposed branch: `public-sync-g7c-20261105`
Base: `origin/main` at `f2cb1ceaff959f4dbf1a42ad764b5bea2a38bf26`
Release status: P2 security-gate revision; local candidate only; not pushed; renewed researcher approval required

Parent candidate: `1755539e22f1` (abbreviated). P2 preserves that candidate and adds only the exact Gitleaks exception, security audit records and an additive manifest-hash correction.

All table hashes are SHA-256 over the exact file bytes stored in the Git commit tree. They are not hashes of a Windows checkout after `core.autocrlf` line-ending conversion.

The candidate commit is created after this manifest is finalized. Its SHA is intentionally recorded in the external handoff and audit result rather than embedded here, avoiding a self-referential commit hash.

## Public payload whitelist

| Path | SHA-256 | Source | Publication reason |
|---|---|---|---|
| `README.md` | `de808f3b129a207baa749fe1994c0d849bf9b70d2e6bf7965f9380b9308fbcda` | remote README plus sanitized status derived from local G7-C commit `35ac438964b7999cd7dcc9b04b7ff32ee763c6ae` | Corrects the public progress statement without releasing record-level data. |
| `PUBLIC_RESEARCH_STATUS.md` | `0d77ddc42558874ba02fa5ee3465248e0ea1642e9c781cb4cc6a43673e9d214b` | aggregate G7-C state and sync audit | Publishes only stage counts, limits and method status. |
| `experiments/temporal_retrieval/README.md` | `655fbb1e5cedb1866dd6339f3f7e6787f6c1c8b84c9f32cc80f4fefb25875054` | commit `5682175992a2e004c78705b10767c00cb1e81cc0` | Documents a generic, zero-call temporal-metadata filter contract. |
| `experiments/temporal_retrieval/filter.py` | `abf79be2abb679122ca3ee254a072916afb49ec9ff3eca4949f98dcba3b3d48c` | commit `5682175992a2e004c78705b10767c00cb1e81cc0` | Reusable source code containing no model output, labels or historical source text. |
| `tests/test_temporal_retrieval_filter.py` | `79fef18341fa913484fc26a29d6238db0ad2ac448609f38383acb180fdb79b5f` | commit `5682175992a2e004c78705b10767c00cb1e81cc0` | Six deterministic tests using synthetic dates only. |
| `.gitleaksignore` | `7d1d07cf7fab3109bd2980c646c93507c8f572b04013f353e900f28dbfb64616` | P2 legacy-finding triage | Four exact fingerprints: two history findings and their two work-tree equivalents; no value, path, rule or commit-wide exception. |
| `GITLEAKS_LEGACY_FINDINGS_TRIAGE.md` | `ff7344ce42a08f92473990c0396851019622dce734c2e86537eda8c4f1b69aef` | P2 local contextual audit | Records the two redacted classifications, irreversible digests and account-impact decision. |
| `GITLEAKS_EXCEPTION_RATIONALE.md` | `676b4237377f8823f99b16da62d871475d7e13190a1876b93003b3fdd8c13879` | P2 exception audit | Explains the exact-fingerprint scope and synthetic negative-control result. |
| `PUBLIC_RELEASE_FINAL_GATE.md` | `613860dba2d3cee774fd784b2db0cf3ef74b67323ee8340a0faa7328d99cf08e` | P2 final gate | Records scan, test, lineage and reapproval status without publishing a suspicious value. |

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

The complete local repository has a private 75-commit research history after the public base. This branch does not cherry-pick that history. It contains the original sanitized publication commit plus additive P2 security-gate commits on top of the public base. Internal data, detailed evidence chains and private scoring reproducibility remain outside the candidate.
