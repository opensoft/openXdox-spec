# Domain Xdox Products — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Future codeXdox and medXdox specialize openXdox through domain models, views, and factory bindings while sharing the document core.
Topics: dox-product-layering, domain-specialization, codexdox, medxdox
Repository context: openXdox-spec; future codeXdox and medXdox product relationships
Captured: 2026-09-06

Lane: dox-product-layering

This non-normative note records planned products, not existing implementations
or newly declared product pins.

## User direction

Brett named codeXdox and medXdox as future products. openXfactory is neutral;
codeXfactory is its engineering specialization. codeXdox is the corresponding
engineering specialization of the document product.

## Proposed composition

codeXdox reuses openXdox and adds engineering schemas, templates, terminology,
views, and adapters to codeXfactory. Candidate capabilities include requirements,
designs, specifications, and traceability to code, pull requests, and tests.
These examples are proposed scope, not an accepted feature list.

medXdox follows the same pattern for medical document models and workflows with
the corresponding medical factory. Its concrete scope remains undefined; this
packet does not assign it responsibility for an entire clinical system.

The preferred implementation direction is composition with versioned dependencies.
Editor improvements flow to openDox, generic factory integration improvements to
openXdox, and engineering-specific behavior to codeXdox. Whether extensions ship
as plugins, packages, configuration, or a combination remains open.

## Product identity versus instance configuration

An alternative is to keep every domain as an instance of openXdox with a different
corpus. That is the model in the older openxFactory naming record. Brett's current
direction introduces named domain products. A useful proposed distinction is that
a domain product supplies reusable domain behavior; an installation supplies a
tenant's corpus and configuration. A corpus change alone need not create a product.

## Dependency declarations and naming

The proposed product ancestry is codeXdox → openXdox → openDox, with medXdox
following the same pattern. The existing openXdox manifest already declares its
openDox pin. A future domain project should declare its actual pinned dependency
and separately make compatibility with its domain factory explicit.

Use Brett's conversation spellings here: openDox, openXdox, codeXdox, medXdox,
openXfactory, and codeXfactory. Existing repositories and records also use
openxFactory, codexFactory, and codexDox. Canonical brand spelling, repository
names, wire identifiers, and naming-validator treatment need reconciliation
before scaffolding. This document performs no rename or pin declaration.

## Possible feats

- **Engineering extension slice** — demonstrate one engineering document model
  and its factory workflow without forking the editor.
- **Naming amendment** — reconcile the older single-capability/instance model
  with the intended named product model through governance.

## Open questions

- Which engineering capabilities first make codeXdox distinct from configuration?
- What is the minimum medical specialization and its factory compatibility contract?
- How are supported core, integration, and domain versions tested together?

## Relationships

- [Factory integration](dox-product-layering-factory-integration.md) supplies the neutral seam.
- [Layer composition](dox-product-layering-synthesis-composition.md) maps dependencies and ownership.
