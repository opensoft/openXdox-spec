# Dox Product Layering Overview — Brainstorm

Status: brainstorm
Kind: reference
Summary: openDox provides complete standalone collaboration, openXdox adds neutral factory integration, and future codeXdox and medXdox add domain specialization.
Topics: dox-product-layering, opendox, openxdox, codexdox, medxdox
Repository context: openXdox-spec; product relationships with openDox and future domain products
Captured: 2026-09-06

Lane: dox-product-layering

This packet captures the conversation as non-normative exploration. It records
user direction separately from suggested design; it does not ratify contracts,
rename repositories, or authorize implementation.

## Motivation

Brett wants a clear map of openDox, openXdox, and planned codeXdox and medXdox.
openDox is the general simple core. openXdox connects it to the neutral factory
system, which itself has domain specializations such as codeXfactory. The product
boundaries should support useful standalone collaboration and shared development
across the future domain products.

## Confirmed direction and proposed details

- **User-stated:** openDox is the general core; openXdox works with neutral
  openXfactory; codeXdox and medXdox are planned domain products.
- **Explicitly confirmed:** openDox supports a complete standalone editing and
  collaboration workflow. Brett answered “yes” to that scope choice.
- **Proposed in discussion:** ownership of specific collaboration features,
  composition through extensions, factory ownership of governed transitions,
  explicit compatibility contracts, and disconnected-factory acceptance checks.
- **Unresolved:** detailed feature scope, collaboration technology, canonical
  naming, packaging, deployment, and extraction of existing work.

## Goals

Users can complete ordinary document work without any factory. Factory users gain
governed actions through a neutral integration. Domain users gain specialized
models and workflows while sharing the editor and collaboration engine.

## Non-goals

This capture does not choose an editor, storage engine, real-time collaboration
protocol, release plan, or medical feature set. It does not modify older naming
decisions or represent the newly scaffolded projects as implemented products.

## What the system delivers

| Layer | Intended user capability |
|---|---|
| openDox | Create, edit, organize, discuss, review, share, and publish documents independently |
| openXdox | Work with factory artifacts and submit governed actions from the document workspace |
| codeXdox | Use engineering document models and codeXfactory workflows |
| medXdox | Use medical document models and corresponding factory workflows |

The detailed verbs and domain examples remain candidate scope.

## System model

```text
openDox                             complete standalone collaboration
  └── openXdox + openXfactory        neutral factory integration
        ├── codeXdox + codeXfactory  engineering specialization
        └── medXdox + medical factory
```

The diagram expresses product composition, not a deployment topology. A typical
journey is document creation and collaboration, optional editorial approval,
submission of a governed intent, and display of the factory's result. Editorial
approval and factory approval have distinct meaning.

## Cluster map

[Product composition](dox-product-layering-synthesis-composition.md) explains
dependency, information flow, authority, and behavior when factory access fails.

## How it fits: evidence from the quick local review

The local openDox and openXdox checkouts inspected during this conversation have
assembly/spec/code structures with scaffold infrastructure and no substantive
product implementation in their new code legs. openDox's contract manifest
records no released bundle. openXdox already declares and records an openDox pin
in the assembly's `project.yaml` and `contracts/opendox-pin.yaml`.

Existing doxBench documentation, contracts, and tests were found in the xFactory
tree. The older openxFactory record at `docs/openxdox-naming.md` describes domain
uses as instances of one openXdox capability and treats openDox as a taken name.
The design at `openspec/changes/add-ideation-intent-plane/design.md` retains that
older naming interpretation. These local observations identify migration and
naming questions; they are not a complete code audit or a deployment assessment.

The new product map needs an explicit amendment to that older record before it
becomes normative. Existing doxBench capabilities should be inventoried against
the proposed ownership boundaries before extraction. Future codeXdox ancestry
would follow codeXdox → openXdox → openDox, with factory compatibility recorded
separately. No pins or existing records were changed by this capture.

## Possible feats

- **Product-boundary proposal** — turn the settled parts of this packet into a
  governed proposal with measurable acceptance criteria and a later implementation
  handoff.

## Key open decisions

- What is the minimum complete standalone collaboration release?
- Which existing doxBench capabilities belong to each layer?
- How do document revisions, editorial approval, and governed artifacts relate?
- What reusable behavior first distinguishes codeXdox from an openXdox installation?
- Which canonical brand, repository, and wire spellings should future products use?

## Document map

- [Standalone core](dox-product-layering-standalone-core.md) — atomic scope and independence.
- [Factory integration](dox-product-layering-factory-integration.md) — atomic governed-action boundary.
- [Domain products](dox-product-layering-domain-products.md) — atomic specialization model.
- [Product composition](dox-product-layering-synthesis-composition.md) — synthesis of all three atoms.
- This overview — motivation, decision provenance, current evidence, and navigation.
