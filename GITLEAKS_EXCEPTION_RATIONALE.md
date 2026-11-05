# Gitleaks Exception Rationale

Date: 2026-11-05
Decision: approve exact-fingerprint exceptions for two audited legacy findings only

## Mechanism

The repository-root `.gitleaksignore` contains four entries:

- two commit-qualified fingerprints for `gitleaks git` history scanning;
- two path/rule/line fingerprints for `gitleaks dir` work-tree scanning.

Together they cover only:

- `sourcegraph-access-token` at line 565 of the single saved Wellcome page;
- `generic-api-key` at line 638 of the same file;
- and, for history scanning, only their occurrence in commit `b06656fed6ca` (abbreviated here; exact in `.gitleaksignore`).

The exception does not contain either matched value. It does not suppress the file, directory, commit, HTML extension or either rule globally.

## Why this is safe and minimal

The first rule matched a browser-visible Cookie Control licence identifier inside the documented client-side `CookieControl.load` configuration. It is not a Sourcegraph token. The second matched a UUID in a serialized `link_type/key/url` content record. It is not an authentication value. The findings have different underlying values.

Gitleaks v8.30.0 documents `.gitleaksignore` as a mechanism for ignoring specific findings by exact `Fingerprint`. The fingerprint is positional, so any rule, line, path or commit change falls outside this exception.

## Control results

- Unmodified raw scan without an exception: 2 history findings and 2 current-tree findings.
- Scan with exact fingerprints: 0 unhandled history findings and 0 unhandled current-tree findings.
- Synthetic control in an isolated temporary copy: a new high-entropy `api_key` at line 2 of the same HTML path was detected by `generic-api-key`. This demonstrates that the exception is not a file- or rule-wide bypass.
- The synthetic value and temporary copy were never committed and were removed after the control.

## Maintenance rule

If the saved HTML is edited, regenerated or moved, the fingerprints must not be mechanically updated. Any changed or new finding requires fresh review. The exception must never be expanded to a whole path or rule solely to keep a scan green.
