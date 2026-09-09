# openXdox Factory Integration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: openXdox composes openDox with neutral factory contracts while the factory owns governed transitions and execution authority.
Topics: dox-product-layering, factory-integration, openxdox, review-authority
Repository context: openXdox-spec; integration with openXfactory
Captured: 2026-09-06

Lane: dox-product-layering

This is a non-normative design proposal. Brett's stated direction is that
openXdox is openDox working with the domain-neutral openXfactory system.

## Proposed ownership

openXdox supplies document-facing integration with factory artifact identity,
lifecycle views, authority checks, intent submission, and execution receipts.
It consumes openDox editing/collaboration capabilities and factory contracts.
The factory remains responsible for deciding whether a governed action is
permitted and for executing or rejecting the transition.

This boundary avoids maintaining a second authoritative workflow engine in the
document application. Local availability hints cannot substitute for enforcement
at the factory action boundary.

## Editorial review and governed approval

openDox can support “approve this document” as an editorial decision. openXdox
can expose “approve this proposal” as a request for a factory transition. These
are separate operations, even when shown beside the same document. Editorial
approval does not automatically grant factory approval or execution authority.

A proposed interaction is: edit a document, complete editorial review if needed,
submit a governed intent tied to the reviewed revision, and show the factory's
result. Revision binding and stale-review handling require explicit contracts.

## Availability boundary

A candidate architectural acceptance test is to disconnect the factory:
ordinary document work remains available, while factory actions become clearly
unavailable. This does not authorize bypassing factory controls or changing
protected artifacts outside their governed write path. Any permitted draft work
must remain distinguishable from an accepted governed revision.

## Alternatives and tensions

Putting factory policy in the core would weaken openDox's independence.
Duplicating policy in openXdox risks inconsistent decisions. A contract-driven
integration is preferred in this discussion, but its transport and packaging
are still open.

## Possible feats

- **Governed action adapter** — specify requests, revision references, authority
  responses, and receipts independently of a particular domain.
- **Disconnected-factory demonstration** — exercise continued ordinary document
  work and explicit unavailability of governed actions.

## Open questions

- How are document identity, revision identity, and factory artifact identity related?
- How do pending requests, retries, failures, and revoked access appear to users?
- Which edits to governed artifacts require factory-mediated application?

## Relationships

- [Standalone core](dox-product-layering-standalone-core.md) owns general collaboration.
- [Domain products](dox-product-layering-domain-products.md) specialize this integration.
- [Layer composition](dox-product-layering-synthesis-composition.md) explains end-to-end behavior.
