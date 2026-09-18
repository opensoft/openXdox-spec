# openDox Standalone Collaboration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: openDox is a complete standalone document editing and collaboration product that requires no factory.
Topics: dox-product-layering, standalone-collaboration, opendox
Repository context: openXdox-spec; proposed boundary with openDox
Captured: 2026-09-06

Lane: dox-product-layering

This is a non-normative conversation capture, not a released product contract.

## Confirmed direction

Brett described openDox as the general simple core system, then explicitly
confirmed: “openDox support a complete standalone editing and collaboration
workflow -yes”. Standalone therefore means a useful, complete product, rather
than a viewer that needs a factory to perform substantive work.

## Proposed scope

Users can create, edit, organize, search, share, discuss, review, and publish
documents. Candidate core capabilities include comments, suggestions, revision
history, provenance, permissions, and ordinary editorial review. These detailed
capabilities are a proposed interpretation of complete collaboration; their
individual requirements have not been settled.

openDox owns document operations and collaboration semantics. Generic extension
interfaces can support downstream products without importing factory lifecycle,
authority, or domain concepts into the core. A simple default experience should
remain available as collaboration capabilities grow.

## Boundaries and alternatives

A browsing-only core was considered in the conversation and rejected by Brett's
confirmation. A factory-dependent editor would also fail the stated standalone
goal. The storage backend, editor technology, collaboration protocol, deployment
model, and identity provider remain undecided.

Standalone does not itself promise offline operation. Independence from a factory
and independence from all network services are different requirements.

## Possible feats

- **Standalone collaboration baseline** — define and demonstrate the complete
  create-to-publish workflow with no factory installed.
- **Core extension contract** — identify generic document hooks needed by
  downstream integrations while retaining a simple default product.

## Open questions

- Does the first collaboration release require simultaneous editing, asynchronous
  suggestions, or both?
- Which document formats, publishing targets, and permission models are essential?
- What offline or self-hosting capabilities are required, if any?

## Relationships

- [Factory integration](dox-product-layering-factory-integration.md) adds governed actions.
- [Layer composition](dox-product-layering-synthesis-composition.md) relates the core to downstream products.
