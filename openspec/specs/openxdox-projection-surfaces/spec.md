# openxdox-projection-surfaces Specification

## Purpose

Describe openXdox's three § 4.5 read-only route-extension projections — the
role-and-authority table, the evidence-and-provenance surface, and the
model/scenario workbench — each rendering an already-declared neutral
contract at request time without re-deriving any conformance judgement
reserved to a canonical validator. These are presentation seams assembled at
`route_extension` § 2.4, not new authority or conformance data models.

## Requirements
### Requirement: § 4.5 projection surfaces render declared contracts without re-deriving conformance

openXdox SHALL render, through read-only route-extension projections
assembled at the `route_extension` § 2.4 seam, the role-and-authority table,
the evidence-and-provenance dials, and the model/scenario workbench already
declared by its neutral contracts — and SHALL NOT compute, in any of the
three, a conformance verdict reserved to a canonical validator.

#### Scenario: role-and-authority projection

- WHEN a request reaches `GET /projections/role-authority`
- THEN the surface renders the ratified Hermes role table
  (`docs/roles-and-authority.md`, `opensoft/openxFactory`) joined, at request
  time, to the resolved actor, the capability dict, and the loopback
  verdict already reachable through the core's own primitives
- AND the resolved actor identity is redacted off-loopback
- AND no new authority data model or conformance judgement is introduced
- AND the binding assembles through the § 2.4 seam beside the gate and
  projection route columns without collision

#### Scenario: evidence-and-provenance surface

- WHEN a parsed `xfactory_derived_model_conformance` document is supplied to
  `GET /projections/evidence`
- THEN the surface renders, per declared family and per `role: model`
  member, the `evidence_field`, `assumption_register_field`, and
  `invented_facts_field` named by whichever `form` the domain declared
  (`assumption_register` or `assumptions_forbidden`)
- AND it computes no conformance verdict over the declaration
- AND `role: scenario` members are excluded, since the schema carries no
  `provenance` block for them
- AND the binding assembles through the § 2.4 seam beside the
  role-authority, gate, and projection route columns without collision

#### Scenario: model/scenario workbench

- WHEN a parsed `xfactory_derived_model_conformance` document is supplied to
  `GET /projections/workbench`
- THEN the surface renders, per declared family, its `role: model` members
  and optional `role: scenario` members in two separate tuples, its
  declared `scope` and `isolation_boundary`, the `truth_store` and
  `truth_store_class` joined to each member's own `truth_store_access`
  binding, the `hypothesis_proposed | no_signal | discarded` confinement of
  scenario output beside each member's `action_authority` bindings, and the
  named `promoting_authority`
- AND it re-derives no conformance judgement reserved to the canonical
  validator (`scripts/validate-derived-models.py`)
- AND the binding assembles through the § 2.4 seam beside the gate,
  projection route, role-authority, and evidence-and-provenance columns
  without collision

