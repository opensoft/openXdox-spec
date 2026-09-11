# Proposal Ratification: add-openxdox-projection-surfaces

Status: ratified
Kind: report
Decision date: 2026-09-11
Ratified by: Brett Heap
Session: openxfactory-36
Citation: [openxFactory#656, comment 5633977407](https://github.com/opensoft/openxFactory/issues/656#issuecomment-5633977407)

## Decision

RATIFIED by Brett Heap. Verbatim, on the record:

> **"ratified — archive add-openxdox-projection-surfaces"**

Given 2026-09-11, first-hand, in session `openxfactory-36`, and recorded on
openxFactory issue
[#656](https://github.com/opensoft/openxFactory/issues/656#issuecomment-5633977407)
(comment id `5633977407`). The word names both acts — ratify the text as
proposed, and archive it — so this record and the archive it accompanies are
one ruling, not two.

## What was ratified

The change landed ACTIVE via `opensoft/openXdox-spec` PR #9, merge `8557fc19`:
`openspec/changes/add-openxdox-projection-surfaces/{proposal.md,tasks.md,specs/openxdox-projection-surfaces/spec.md}`.

One capability, `openxdox-projection-surfaces`, carrying **one requirement**
("§ 4.5 projection surfaces render declared contracts without re-deriving
conformance") with **three scenarios** — role-and-authority projection,
evidence-and-provenance surface, and model/scenario workbench. This leg is
documentation-only; the code the scenarios describe is already merged in
`opensoft/openXdox-code`:

- #10 `4f98e77c7985f786af2ec295c38b6b06a7f5fce6` — role-and-authority
  projection
- #11 `427230c340cdb1f5d114d3868073cd156fa33ada` — evidence-and-provenance
  surface
- #12 `5333b125dc0f2dd9ee6f6e558c758fbfe6c49b4d` — model/scenario workbench

No wording was named for change by the word above, so none was changed: the
requirement and its three scenarios are ratified exactly as proposed and
merged at `8557fc19`.

## Lane

Lane: openxfactory-4-opendox-extraction (formerly openxfactory-opendox).

## Limits

This record performs no merge and closes no issue. It records the word and
what it reached: ratification of the text, and authorization to archive it
(`openspec archive add-openxdox-projection-surfaces`), promoting the delta
into `openspec/specs/openxdox-projection-surfaces/spec.md`.

## Erratum — 2026-09-11

The ratified text's workbench scenario said the binding "assembles through
the § 2.4 seam beside the other three route-extension columns without
collision." The promoted spec now says it assembles "beside the gate,
projection route, role-authority, and evidence-and-provenance columns
without collision" — naming all four existing columns instead of stating
an unnamed count of three.

**Evidence.** `opensoft/openXdox-code` `5333b125dc0f2dd9ee6f6e558c758fbfe6c49b4d`,
`tests/test_model_scenario_workbench_seam.py::test_assembles_beside_all_four_existing_contribution_columns`,
which builds the five-extension assembly (gate, projection, role-authority,
evidence, workbench) and asserts 7 bindings with no collision — the module's
own docstring states the workbench "does not collide with any of the four."
The ratified "three" undercounted by one against this evidence; raised as a
Copilot review thread on `opensoft/openXdox-spec` PR #10
([discussion_r3988997514](https://github.com/opensoft/openXdox-spec/pull/10#discussion_r3988997514)),
answered and resolved there
([discussion_r3989020743](https://github.com/opensoft/openXdox-spec/pull/10#discussion_r3989020743))
naming this erratum as the follow-up.

**Ruling.** Brett Heap, ASK-5 = erratum, 2026-09-11, verbatim: **"ASK-5:
erratum, proceed"**
([opensoft/openxFactory#656, comment 5634505747](https://github.com/opensoft/openxFactory/issues/656#issuecomment-5634505747)).

The archived delta under `specs/` stays verbatim as ratified; the promoted
spec carries the correction.
