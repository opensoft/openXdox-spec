# Tasks: add-nightly-dashboard-refresh

## 1. Arrival

- [x] 1.1 The `ideation-dashboard` delta is carried BYTE-IDENTICAL from the
      openxFactory packet at `cb2d3a2c` (`sha256 50fd14ba…`, 6,663 bytes,
      `diff`-verified) and the openxFactory packet is closed as re-homed in the
      same window.
- [x] 1.2 The seven are carried with **exactly one line changed** — the delta
      file's capability heading, `# doc-health` → `# openxdox-refresh-lane` —
      and `diff` against the openxFactory delta reports that one line and
      nothing else.
- [ ] 1.3 The capability `ideation-dashboard` reaches this corpus with
      `split-opendox-two-layer-product` § 5's shed. **Until it does, the
      `ideation-dashboard` half cannot archive** — `openspec validate --strict`
      passes and reports "Archive would refuse this delta: target spec does not
      exist".
- [ ] 1.4 Confirm or replace the capability id `openxdox-refresh-lane`. It is an
      authoring choice: the packet rules no destination id, `doc-health` is ruled
      out, `openxdox-projection-surfaces` is narrowly the § 4.5 route-extension
      projections, and `ideation-dashboard` would assert these are dashboard
      requirements.

## 2. THE OWED RE-AUTHORING — the one thing this change does not do

- [ ] 2.1 **Re-author the seven against the ADAPTER.** `design.md` § D9 of
      `split-opendox-two-layer-product`: *"the refresh lane in openXdox reads the
      corpus through the adapter, so the requirements are re-authored against the
      adapter IN openXdox."* As they stand, their antecedents name openxFactory's
      nightly doc-health run, the aggregation's `openxFactory` submodule pin, the
      Omnigent artifact worker and a named registry.
      **BLOCKED ON:** the adapter capability's declaration. `corpus-adapter-seam`
      is an unpromoted delta of `split-opendox-two-layer-product`, and its
      successor capability id is that packet's § 5.2a, unbuilt. Seven
      requirements authored against an undeclared seam would have to be authored
      again the moment the seam is declared.
- [ ] 2.2 **Do not ratify the seven in this corpus until 2.1 is done.**
      Ratifying them as they stand would have openXdox ratify obligations about
      another repository's nightly run.

## 3. The realization that travelled with it

The openxFactory packet's realization boxes were worked there; the mechanism
moves with the carve into `opensoft/openXdox-code` rather than being rebuilt.

- [ ] 3.1 Re-verify the refresh lane and the served plane's baked artifacts
      against `openXdox-code` after the carve lands there. The four-part floor
      proves test counts per destination rather than inheriting them.
- [ ] 3.2 The openxFactory packet's thirteen open task boxes travel with it and
      are re-read against openXdox's own realization once 2.1 has settled what
      the obligations say here.

## 4. What did NOT travel

- [x] 4.1 **The aggregation-side artifact-only worker STAYS in the aggregation**
      (`split-opendox-two-layer-product` `tasks.md` § 6.1). Recorded as a
      decision, not an omission; no workflow moves in this change.
- [x] 4.2 **Nothing was added to `openxFactory`'s `doc-health`**, which is the
      binding half of § 6.1 and is satisfied absolutely: the openxFactory closure
      promotes no delta at all.

## 5. Readings registered at arrival, NOT applied to the carried text

RULING Q6 freezes this packet where it stands and § 6.1 carries its deltas
**byte-identical** (the `ideation-dashboard` file exactly; the seven with one
line changed, their capability heading). That carriage is the closure's own
evidence — openxFactory PR #1060 states it as a sha256 equality — so a reading
of the TEXT, however right, cannot be answered by editing the text here. It is
registered instead, against the box that will rewrite these obligations anyway.

Copilot reviewed openXdox-spec #15 at `6c17fd0` and raised five. **Four are
inputs to § 2.1** and are listed as such; the fifth was a misreading and is
recorded as answered rather than dropped, so it is not re-raised in the next
round as though it were new.

- [ ] 5.1 **The baked-input PATH SCOPE is not normatively fixed**
      (`specs/openxdox-refresh-lane/spec.md`, the no-change predicate). One run
      may record scope A and the next use scope B, and a change inside A can
      then be omitted from the comparison. Either name a fixed path set or make
      a scope change force a rebuild. **§ 2.1's business**: the predicate is
      about the corpus this lane reads, and once that read goes through the
      adapter the path set is the adapter's to define rather than a repetition
      of openxFactory's tree shape.
- [ ] 5.2 **The provenance record has no declared GRAMMAR** — the requirement
      asks for a stable machine-readable key/value comment the NEXT run parses,
      without fixing key names, the association to the pin, or the behaviour on
      a parse failure. Two realizations can emit incompatible comments and make
      different refresh decisions. **§ 2.1's business** for the same reason, and
      the parse-failure arm has a default already stated in the packet's own
      prose (absent or unparseable provenance counts as CHANGED and bootstraps),
      which the re-authoring should raise into the requirement.
- [ ] 5.3 **The fallback-staleness bound names no duration and no authoritative
      setting** (`specs/ideation-dashboard/spec.md`), so a conformant
      implementation may choose an arbitrarily long rebake interval. The
      requirement deliberately says "a stated bound … stated wherever the served
      plane is documented"; whether openXdox pins a number or names the
      configuration that carries it is openXdox's ratification decision, not a
      carriage decision.
- [ ] 5.4 **The authority chain is called FOUR rungs and enumerates five
      authorities** (worker, lane App, approver App, GitHub auto-merge, the
      in-cluster reconciler). Either auto-merge and reconciliation sit inside an
      existing rung — which is the packet's evident intent, since the ruling that
      authored this chain speaks of four SEPARATE AUTHORITIES holding rungs and
      treats delivery as the install layer's own path — or the count is wrong.
      State which at re-authoring, because an invariant that cannot be counted
      consistently cannot be checked.
- [x] 5.5 **ANSWERED, no change owed:** the scenario clause *"any path would
      have the rebake lane apply its own image to the serving host, or hold a
      credential that could"* was read as an incomplete predicate. It is a gapped
      coordination — "or hold a credential that could [apply its own image to the
      serving host]" — and the `THEN` names the remedy in the same breath (the
      lane proposes a digest pin; the install layer applies it). The clause is
      byte-identical to openxFactory's ratified text and is not defective.
