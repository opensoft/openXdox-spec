# Ideation-Dashboard Examples and Schemas — Stale-Citation Erratum

Status: record
Kind: report
Captured: 2026-09-10
Repository context: openXdox-spec
Corrects: `examples/ideation-dashboard/README.md`, `contracts/schemas/ideation-dashboard-snapshot.schema.yaml`, `contracts/schemas/ideation-dashboard-snapshot-index.schema.yaml`
Summary: Names the source-path citations in three arrived files that the carve left stale, and their live targets, without mutating the frozen, byte-identical documents.
Topics: openxdox, carve, ideation-dashboard, stale-citation

## Why this is a separate document, not an edit

All three files below arrived at carve commit
`b075fd91dc8fced8e1373825ba80220c33536bae` (tag `opendox-carve-0`) as
`moved_verbatim` rows of `docs/opendox-carve-manifest.yaml`
(`opensoft/openxFactory`, FLOOR PART 1): the arrived blob's `sha256` and
mode must EQUAL the row's, with no exception for an editorial byte.
Confirmed unedited here — `git cat-file blob HEAD:<path> | sha256sum`
reproduces each row's declared `sha256` exactly for all three files. Touching
any byte of any of them is an undeclared movement, and
`scripts/verify-carve-arrival.py` (run from an `opensoft/openxFactory`
checkout against this repository) refuses any such diff with
`arrival-digest-mismatch` — the same conclusion carve leg 4's own landing
record reached (`opensoft/openxFactory#656`, comment `5623282626`: "a fix
here would be an undeclared movement (proven: a one-token edit refuses
arrival-digest-mismatch)"). Fixing them in place therefore needs a
Q-L1-family manifest amendment in `opensoft/openxFactory` — outside this
document's authority. This erratum is the correction of record until that
amendment lands, in the pattern already established by openxFactory's own
`docs/doxbench-runtime-refresh-dogfood-erratum.md`: it corrects without
mutating.

## The citations

Measured against `docs/opendox-carve-manifest.yaml` at `opensoft/openxFactory`
main (`85fb85622a2c83cca909d3bda7cae9be4ad6a713`, 2026-09-10) and the arrived
files' own text. None of the citations below is a schema `$ref`, an import,
or an exec edge — every hit is prose (a README sentence or a YAML comment),
so nothing executes against a stale path; each is a documentation pointer a
reader would otherwise follow to nothing in this repository.

| file : line(s) | cites | why it is stale | live target |
| --- | --- | --- | --- |
| `examples/ideation-dashboard/README.md`:10, 207, 302, 318, 321, 325 | `scripts/validate-ideation-dashboard-contracts.py` | the manifest moved this validator to the sibling openXdox-code leg; it is not present in this repository | `opensoft/openXdox-code`'s `scripts/validate-ideation-dashboard-contracts.py` |
| `examples/ideation-dashboard/README.md`:208 | `scripts/validate-ideation-cross-reference.py` | no manifest row moves this script anywhere; it exists only in `opensoft/openxFactory` | `opensoft/openxFactory`'s `scripts/validate-ideation-cross-reference.py` |
| `contracts/schemas/ideation-dashboard-snapshot-index.schema.yaml`:44 | `scripts/validate-ideation-dashboard-contracts.py` | same as the README row above | `opensoft/openXdox-code`'s `scripts/validate-ideation-dashboard-contracts.py` |
| `contracts/schemas/ideation-dashboard-snapshot.schema.yaml`:108 | `docs/document-lifecycle.md` | no manifest row moves this document anywhere; it stays only in `opensoft/openxFactory` (the controlled `Status:` header vocabulary is openxFactory's own governance) | `opensoft/openxFactory`'s `docs/document-lifecycle.md` |

Citations correctly attributed to a third repository already (for example
`codexFactory feature 007` in `contracts/schemas/gate-action-record.schema.yaml`)
are not listed above: codexFactory was not touched by this carve, so those
citations remain live. `"repository": "openxFactory"` values inside the
example/negative fixtures are sample DATA, not citations — openxFactory
remains a valid repository identifier in that vocabulary regardless of the
carve, so those are unaffected.

## Disposition

Owed: a manifest amendment (Q-L1-family) declaring the lines above so a
future commit at `opensoft/openXdox-spec` can correct them in place.
Recorded for the BUILD-arc register (`opensoft/openxFactory#656`).
