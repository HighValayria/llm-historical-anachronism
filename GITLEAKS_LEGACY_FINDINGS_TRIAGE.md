# Gitleaks Legacy Findings Triage

Date: 2026-11-05
Scanner: Gitleaks v8.30.0, official Windows x64 release
Scanner archive SHA-256: `54fe94f644b832dd08e8c3a5915efb3bfa862386d59fb27ca0792cb687a83573`
Target: `experiments/data_feasibility_pilot/metadata/wellcome_za7rnxwq_item_page.html`
Originating commit: `b06656fed6ca` (abbreviated; exact commit is encoded in the ignore fingerprint)

No complete matched value is reproduced in this report. The only value-level identifiers below are irreversible SHA-256 digests.

## Finding 1: `sourcegraph-access-token`

- Location: line 565 in the committed snapshot; one occurrence in the file.
- Extracted-value length: 40 characters.
- Extracted-value SHA-256: `2e28a810f0582b21789dabddf6820459e719ed95bf51bc872e26bc97c0983d20`.
- Context: the value is the `apiKey` member of a browser-side `CookieControl.load({ product, apiKey, ... })` configuration object. It is not in a Sourcegraph configuration, authorization header, environment file or server-side credential store.
- External documentation check: Cookie Control's official version 9 setup documentation requires a site-specific `apiKey` and `product` in the JavaScript object passed to `CookieControl.load`. Its documentation also states that the registered website domain authorizes the licence. This is an intentionally browser-visible client licence identifier.
- Repository account check: no other tracked Sourcegraph reference or Sourcegraph account configuration was found outside this saved page snapshot.
- Classification: **rule-level false positive; public client licence identifier**. It may still identify the third-party website's Cookie Control licence, but it is not a Sourcegraph access token and is not a private credential of this research project.
- Account action: no project account revocation or rotation is indicated. The project must not attempt to use the identifier. No external validity probe was performed.

## Finding 2: `generic-api-key`

- Location: line 638 in the committed snapshot; one occurrence in the file.
- Extracted-value length: 36 characters.
- Extracted-value SHA-256: `6bb39b58a39918a7bbec3146a5cf90733893d40c0fce71d7eb4afe7ecf7aa284`.
- Context: a UUID-formatted value stored in the `key` field of an embedded content-link record whose adjacent fields are `link_type` and `url`. The record describes a `Web` link to `forms.office.com`; it is not an API-key assignment, authentication header or service configuration.
- Classification: **false positive; public content-record UUID**.
- Account action: none. There is no credential or related service account to revoke.

## Cross-finding and history checks

- The two findings do **not** contain the same underlying value; their irreversible digests differ.
- Both were introduced by the same saved public Wellcome Collection page snapshot in commit `b06656fed6ca`.
- That commit is an ancestor of `origin/main`, and the target file is already present in `origin/main`; neither finding is introduced by the G7-C publication delta.
- The repository source manifest records the snapshot's public source URL as `https://wellcomecollection.org/works/za7rnxwq`.
- No suspected value was sent to a third-party validator or used in an external request.
- Secret-bearing transient scan reports were not retained. Committed reports contain only rule names, locations, fingerprints and irreversible digests.

## Decision

Both findings have sufficient contextual evidence for a narrowly scoped false-positive disposition. The release may use exact finding fingerprints, but must not ignore the whole HTML file, the originating commit, either detection rule, or a broad path pattern.
