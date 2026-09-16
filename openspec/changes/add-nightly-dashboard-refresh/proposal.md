---
Status: draft
Re-homed-from: openxFactory `openspec/changes/add-nightly-dashboard-refresh`, closed as re-homed 2026-09-16 under RULING Q6
Ratified-in-openxFactory: ratified 2026-08-25 and re-ratified 2026-09-04 (Brett Heap, in session: "ratify add-nightly-dashboard-refresh against its own record")
code_surface: opensoft/openXdox-code (the refresh lane and the served plane's baked artifacts), plus the aggregation-side artifact-only worker, WHICH STAYS IN THE AGGREGATION (`opensoft/openxFactory` `openspec/changes/split-opendox-two-layer-product/tasks.md` § 6.1) and is named here as a dependency rather than as a surface this change moves
---

# Proposal: add-nightly-dashboard-refresh

## Why

`add-nightly-dashboard-refresh` was ratified in `opensoft/openxFactory` on
2026-08-25 and re-ratified 2026-09-04. RULING Q6 (2026-09-04T17:49Z,
`opensoft/openxFactory` issue #656) froze it where it stood and re-homed it to
**openXdox**, because — in `design.md` § D9's words — *the refresh lane is
projection-mechanism work*, and projection mechanism is openXdox's.

The substance: a served plane bakes two artifacts — a fallback snapshot and the
corpus tree its `/source` viewer resolves against — and they go stale on the
IMAGE's cadence. A scheduled rebake bounds that staleness, and it must bake both
at ONE revision, because an image whose snapshot names revision X while its
`/source` tree carries revision Y displays a freshness claim the viewer cannot
satisfy and loses every document that landed between the two.

## What changes

**TWO capability deltas, and they arrive on different terms. That difference is
the whole of § 6.1 and it is stated here rather than left to a diff.**

### 1. `ideation-dashboard` — 1 ADDED + 1 MODIFIED, BYTE-IDENTICAL

`sha256 50fd14ba376b9c718b28d219ccdc402593ee93e65be619a950d8eed5923b56e6`, 6,663
bytes — the digest the openxFactory delta carries at `main` `cb2d3a2c`. Not one
character edited, and none was owed: the string `openxFactory` does not occur in
it (`grep -c` → **0**). ADDED: *The served plane's baked artifacts are rebaked on
a schedule at one revision*. MODIFIED: *Runtime snapshot fetch with baked fallback
and displayed freshness* — one of the FOUR promoted titles the split packet's
§ THE SIBLING COLLISION table (a) names, with **openXdox** as its destination.

### 2. `openxdox-refresh-lane` — the SEVEN, and they arrive UNFINISHED ON PURPOSE

`tasks.md` § 6.1 is explicit that these seven **"do NOT travel and are NOT added
to `openxFactory`"**, and `design.md` § D9 says where they go instead: *"the
refresh lane in openXdox reads the corpus through the adapter, so the
requirements are re-authored against the adapter IN openXdox rather than added to
`openxFactory`'s `doc-health`."*

**The binding half is satisfied absolutely**: they are NOT added to
`openxFactory`'s `doc-health`, nothing promotes in openxFactory at all, and they
do not land on a `doc-health` capability here either — `doc-health` stays
openxFactory's own capability and Q4 points that dependency one way.

**The re-authoring against the adapter is NOT performed here, and that is a
decision rather than an omission.** These seven are openxFactory-nightly-specific
in their ANTECEDENTS, not merely in a subject noun: *"The nightly doc-health run
SHALL include an ideation-dashboard IMAGE REFRESH lane"*, *"the aggregation's
`openxFactory` submodule pin"*, the Omnigent artifact worker, the named registry.
Re-pointing them is not the carve seam's declared subject edit — *"the subject
`openxFactory SHALL` becomes the receiving repository's"* — it is a rewrite of
what each obligation is ABOUT. **And the adapter they must be re-authored against
does not exist in any corpus today**: `corpus-adapter-seam` is a delta of
`split-opendox-two-layer-product` and is unpromoted, and the successor capability
id is that packet's § 5.2a, unbuilt. Seven requirements authored against an
undeclared seam would be authored on sand, and would have to be rewritten again
the moment the seam is declared.

So they are carried **byte-identical below their first line**, and `tasks.md`
§ 2.1 carries the re-authoring as the open, blocked act it is.
`sha256 deae8d393936be605542f6731f7164a34e1b0ff281362cd8dc1df64566ba24a9` here
against `6b4a577dc5f3f0924d0a442415c92c2a9c6b824b3ac231ce5890915c931ea44c` at
openxFactory: `diff` reports **exactly one differing line**, line 1, the delta
file's capability heading (`# doc-health` → `# openxdox-refresh-lane`). That one
line is the whole of the edit and it is measurable with `diff`.

**The capability id `openxdox-refresh-lane` is an authoring choice and is flagged
as one.** The packet rules no destination capability id. `doc-health` was ruled
out; this repository's one promoted capability, `openxdox-projection-surfaces`,
is narrowly about the § 4.5 read-only route-extension projections and these are
not those; and folding seven nightly-lane requirements into `ideation-dashboard`
would assert they are dashboard requirements, which they are not. The name follows
the convention this repository's existing capability already sets. Contest it on
the pull request; nothing else depends on it.

## Impact

- Affected specs: `ideation-dashboard` (1 ADDED, 1 MODIFIED);
  `openxdox-refresh-lane` (7 ADDED, unratified here and owing a re-authoring)
- Affected code: `opensoft/openXdox-code`, as the projection mechanism arrives
  with the carve. **The aggregation-side artifact-only worker STAYS in the
  aggregation** (`tasks.md` § 6.1) and nothing here moves a workflow.
- **THE `ideation-dashboard` HALF CANNOT ARCHIVE YET.** `openspec validate
  --strict` passes and says so: *"Archive would refuse this delta:
  ideation-dashboard: target spec does not exist."* That capability reaches this
  corpus with `split-opendox-two-layer-product` § 5's shed. The
  `openxdox-refresh-lane` half is all-ADDED and would archive into a new spec,
  but it does not archive ahead of its sibling: they are one change.
- **Standing.** The requirement text was ratified by Brett Heap in openxFactory;
  that act is cited unedited in the front matter. Ratification IN THIS CORPUS is
  openXdox's own owed act and is NOT claimed here — and for the seven it is
  explicitly BLOCKED on the re-authoring, because openXdox would otherwise be
  ratifying obligations about another repository's nightly run.
