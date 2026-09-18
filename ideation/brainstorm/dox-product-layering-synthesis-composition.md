# Synthesis: Dox Product Composition — Brainstorm

Status: brainstorm
Kind: architecture
Summary: A standalone collaboration core, neutral factory integration, and domain extensions form independently understandable product layers.
Topics: dox-product-layering, product-composition, synthesis
Repository context: openXdox-spec; cross-product architecture discussion
Captured: 2026-09-06

Lane: dox-product-layering

This synthesis is non-normative. It combines the confirmed standalone direction
with proposed implementation and ownership boundaries.

## Possible feats

- **Cross-layer reference journey** — demonstrate a document edited in openDox,
  submitted through openXdox, and processed by an engineering factory binding.
- **Capability ownership inventory** — classify existing doxBench capabilities
  against these layers before proposing extraction work.

## Members and their joints

Atomic members: [standalone core](dox-product-layering-standalone-core.md),
[factory integration](dox-product-layering-factory-integration.md), and
[domain products](dox-product-layering-domain-products.md).

### Dependency and reuse

| Product | Proposed responsibility | Consumes |
|---|---|---|
| openDox | General editing and collaboration | No factory dependency |
| openXdox | Neutral governed document integration | openDox and openXfactory contracts |
| codeXdox | Engineering document specialization | openXdox and codeXfactory contracts |
| medXdox | Medical document specialization | openXdox and medical factory contracts |

Factory specialization and document-product specialization are separate but
connected relationships: codeXfactory specializes the neutral factory, while
codeXdox specializes its document-facing product. Neither relationship implies
that a factory is renamed into a document application.

### Information flow and authority

A candidate engineering journey starts with creating and collaborating on a
document using the shared core. codeXdox supplies its engineering schema and
traceability view. openXdox submits an intent identifying the relevant revision.
codeXfactory evaluates the governed request and returns a result that the document
surface displays. Editorial state, requested factory state, and accepted factory
state remain distinguishable.

### Failure and independence

When the factory is unavailable, the core remains a useful document application.
Factory-dependent actions and protected writes retain their restrictions.
Reconnect behavior must reconcile stale revisions and request results rather
than silently converting ordinary document edits into approved transitions.

## Emergent behavior

The same collaboration engine can serve independent document users, neutral
factory users, and domain users. A domain product can deliver specialized work
without creating its own editor or duplicating factory authority.

## Tensions to hold

- Rich collaboration must coexist with openDox's intended simplicity.
- Shared document representations must leave room for domain validation.
- Separate releases need compatibility checks across both product ancestry and
  factory contracts; an ancestry pin alone does not prove runtime compatibility.
- A future extraction must preserve existing behavior and its governing records.

## Recombination opportunities

The extension boundary may support further domains or multiple storage adapters.
These are opportunities, not selected products or commitments.

## Open questions

Deployment topology, identity mapping, extension packaging, and revision-bound
approval behavior need design work. No extraction sequence or implementation
task list is authorized by this brainstorm.

## Relationships

[Product overview](dox-product-layering-overview.md) provides the conversation
record, evidence, and complete document map.
