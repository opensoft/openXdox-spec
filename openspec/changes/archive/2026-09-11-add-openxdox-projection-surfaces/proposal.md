code_surface: opensoft/openXdox-code (already shipped: `src/openxdox/role_authority_projection.py` #10 `4f98e77c7985f786af2ec295c38b6b06a7f5fce6`, `src/openxdox/evidence_provenance_surface.py` #11 `427230c340cdb1f5d114d3868073cd156fa33ada`, `src/openxdox/model_scenario_workbench.py` #12 `5333b125dc0f2dd9ee6f6e558c758fbfe6c49b4d` — the three merges are the realization evidence this proposal cites)
target_release: none — this leg is documentation-only; the code surface already ships on openXdox-code's own release line
Status: ratified
Ratified by: Brett Heap, 2026-09-11 — https://github.com/opensoft/openxFactory/issues/656#issuecomment-5633977407, record `review/ratification-2026-09-11.md`

---

# Proposal: add-openxdox-projection-surfaces

## Why

`split-opendox-two-layer-product` task § 4.5 named three independent BUILD
features and ruled their launch order (ASK-3, `opensoft/openxFactory#656`
comment
[5628886636](https://github.com/opensoft/openxFactory/issues/656#issuecomment-5628886636)):
the role-and-authority projection, the evidence-and-provenance surface, and
the model/scenario workbench. All three are now built and merged in
`opensoft/openXdox-code` — #10 `4f98e77c7985f786af2ec295c38b6b06a7f5fce6`, #11
`427230c340cdb1f5d114d3868073cd156fa33ada`, #12
`5333b125dc0f2dd9ee6f6e558c758fbfe6c49b4d` — and each of the three PR bodies
states that § 4.5's box does not tick until this leg carries a requirement row
for the work. This change is that row.

## What Changes

- ADD one capability, `openxdox-projection-surfaces`, carrying one
  requirement with three scenarios — one per landed feature.
- No implementation changes: this leg is spec-only, and the code these
  scenarios describe already exists, tested and merged, in
  `opensoft/openXdox-code`.

## Capabilities

### New Capabilities
- `openxdox-projection-surfaces`: the three § 4.5 read-only route-extension
  projections (role-and-authority, evidence-and-provenance, model/scenario
  workbench), each rendering an already-declared neutral contract without
  re-deriving any conformance judgement reserved to a canonical validator.

### Modified Capabilities
(none)

## Impact

Documentation only, in this leg (`opensoft/openXdox-spec`). The code this
requirement describes is already merged in `opensoft/openXdox-code`:
`src/openxdox/role_authority_projection.py` (#10),
`src/openxdox/evidence_provenance_surface.py` (#11), and
`src/openxdox/model_scenario_workbench.py` (#12).

Refs opensoft/openxFactory#656.
