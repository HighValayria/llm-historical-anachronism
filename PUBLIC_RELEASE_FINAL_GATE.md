# Public Release Final Gate — P2

Date: 2026-11-05
Branch: `public-sync-g7c-20261105`
Original approved candidate: `1755539e22f1` (abbreviated)
Base: `origin/main` at `f2cb1ceaff95` (abbreviated)
Status: `ready_for_researcher_reapproval_not_pushed`

## Gate outcome

The two legacy findings were classified with sufficient evidence and are covered by exact fingerprints only. No real Sourcegraph token or project-owned API credential was identified. The Cookie Control value is an intentionally public, domain-authorized client licence identifier from the captured third-party page; the other value is a content-link UUID.

Because P2 adds a versioned exception and audit documents, the branch no longer points to the previously approved `1755539` candidate. The new exact commit is intentionally reported in the external handoff after commit creation rather than embedded here.

## Required checks

| Check | Result |
|---|---|
| Direct derivation from remote `main` | pass; no private research commit is merged or cherry-picked |
| Original no-exception history scan | 2 findings, both audited legacy findings |
| Original no-exception tree scan | 2 findings, same two audited legacy findings |
| Exact-exception full-history scan | pass; 0 unhandled findings |
| Exact-exception current-tree scan | pass; 0 unhandled findings |
| Same-path synthetic credential control | pass; new line-2 synthetic `generic-api-key` finding detected |
| Candidate increment scan | pass; no unhandled finding |
| Hidden condition mapping / raw response / workbook | none in publication increment |
| Public focused tests | pass; 6 tests |
| Public full test suite | pass; 33 tests and 3 subtests |
| Push or merge | not performed |

## Release boundary

The public payload remains aggregate status, generic temporal-filter code/tests and release-control documentation. It still excludes C0/C1 mappings, formal model outputs, human workbooks, claim-level G5–G7 data, detailed labels, S2 material, authorization records and private research history.

## Approval consequence

The technical security gate is clear, but the candidate commit has changed. Publication requires renewed researcher approval of the new commit and updated manifest. P2 performs no push and no merge.
