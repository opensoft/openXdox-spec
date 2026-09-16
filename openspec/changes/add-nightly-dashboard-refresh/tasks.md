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

Its review at `cba3b46` raised three more, all of them real gaps in the carried
text and all of them § 2.1's business: 5.6, 5.7 and 5.8 below. The same round
also found that 5.2 CONTRADICTED the requirement it tracks, which is a defect in
this ledger rather than in the carriage — corrected in the box itself.

Its review at `a082aca` raised three. One is a real gap in the carried text and
is registered as 5.9 below. One was the same class of ledger defect as before —
5.2's narrowing, written in the previous round, had overshot the correction it
was making — and is widened in the box itself. The third was about a claim in
the PULL REQUEST's own description rather than about any file, and is fixed
there: the description called this *"the first OpenSpec change ever authored in
this corpus"*, which is false. This corpus has carried an OpenSpec change since
2026-09-11 — `openspec/changes/archive/2026-09-11-add-openxdox-projection-surfaces`
— and promoted it to `openspec/specs/openxdox-projection-surfaces`. The true
claim, and the one § 8.5 actually needs, is that this is the first RE-HOMED
receiving change in this corpus.

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
      without fixing key names or the association to the pin. Two realizations
      can emit incompatible comments and make different refresh decisions.
      **§ 2.1's business** for the same reason as 5.1.
      **NARROWED 2026-09-16, on Copilot's reading of `cba3b46`, and the narrowing
      is a correction rather than a scope cut.** This box also listed "the
      behaviour on a parse failure" as unfixed, and then said a page later that
      the packet's *prose* supplies a default. Both halves were wrong in the same
      direction: the behaviour is fixed, and it is fixed in the REQUIREMENT, not
      in prose around it — `specs/openxdox-refresh-lane/spec.md:51`, *"Provenance
      that is ABSENT or unparseable … SHALL be treated as CHANGED: the lane
      builds once, and the pin it produces establishes the provenance every later
      run reads."* That is a normative SHALL with its own stated reason (failing
      open costs one redundant build; failing closed leaves a hand-pinned plane
      permanently unrefreshed). A task ledger that reports a settled obligation
      as open is the same defect as one reporting an option as owed, and it
      would have sent the re-authoring to write a rule that already exists.
      **WIDENED 2026-09-16, on Copilot's reading of `a082aca`, because the
      narrowing overshot.** What remains open is the RECORD SHAPE, which is two
      things and not one: the KEY NAMES, and the ASSOCIATION of each recorded
      revision with the pin it sits beside. The second is SEMANTIC, not grammar.
      Two realizations could agree on every key name, emit records a common
      parser accepts, and still disagree about which of the two revisions the
      `digest:` beside them was built from — and the no-change comparison would
      then read a well-formed record and reach the wrong answer. Calling the
      residue "the grammar alone" would have let § 2.1 fix a parser and leave
      that ambiguity standing, which is the same failure this box was opened to
      prevent. The box's own opening sentence had it right — *"without fixing
      key names or the association to the pin"* — and the narrowing contradicted
      it two paragraphs later.
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
- [ ] 5.6 **The status artifact REQUIRES a field two of its own outcomes cannot
      produce.** The outcome requirement (`specs/openxdox-refresh-lane/spec.md`)
      lists `skipped` and `no-change` among the outcomes it must distinguish, and
      in the same sentence requires every recorded outcome to carry "the snapshot
      `source_revision`". A no-change run stops BEFORE snapshot generation and a
      readiness skip can stop before any snapshot has ever existed — on a first
      run there is not even a previous pin to copy from. So the payload the
      requirement demands is unproducible for exactly the two outcomes it was
      written to make auditable. **§ 2.1's business**: the re-authoring states
      whether the field is omitted, carried from the previously pinned image, or
      represented as explicitly unavailable — and the third is the only one of
      the three that cannot be mistaken for a fresh reading.
- [ ] 5.7 **A validator that could not RUN has no output to record.** The
      strict-validation refusal requires the lane to "record the failure with the
      validator's own output". A validator that fails to EXECUTE — missing,
      uninstallable, killed — produces no such output, so the requirement's own
      remedy is undefined in the one case where the diagnostic matters most.
      **§ 2.1's business**: the re-authoring distinguishes a validation FAILURE
      from a validator-EXECUTION failure and names what the artifact carries for
      the second. The publish-nothing half needs no change and must not be
      weakened by the fix: both cases publish nothing.
- [ ] 5.8 **A PARKED pull request can make the lane churn nightly.** The
      authoritative provenance is read from the served plane's DEFAULT branch, so
      while a pin pull request sits open and unmerged the recorded revisions do
      not move. With no new inputs the next run still reads the old provenance,
      decides CHANGED, rebuilds, and — because these image builds are explicitly
      non-reproducible, which the packet itself argues at length — pushes a new
      digest and advances it into the same open pull request. Every night, for as
      long as the review is parked. The packet ALREADY names the condition, in
      the outcome requirement's last sentence: an unmerged pin on a fixed branch
      "SHALL be reportable as a stuck chain". It makes it reportable and does not
      make it stop the rebuild. **§ 2.1's business**: the re-authoring says
      whether the preflight consults the OPEN pull request's candidate provenance
      before deciding, or whether a stuck chain suppresses the rebuild until it
      clears.
- [ ] 5.9 **The normative PUSH TARGET names the registry HOST, not the image
      REPOSITORY.** The refresh-lane requirement says the child SHALL *"push to
      `acropensoftxfactoryqa.azurecr.io` under a date-stamped tag"*
      (`specs/openxdox-refresh-lane/spec.md`, the lane requirement). A registry
      host is not a push target: an image reference is `<registry>/<repository>:<tag>`,
      so a conforming implementation is free to publish into ANY repository of
      that registry and still satisfy the sentence. MEASURED, so the gap is not
      theoretical: the realization that travelled with this packet pushes to
      `acropensoftxfactoryqa.azurecr.io/ideation-dashboard`
      (`DEFAULT_IMAGE`, openxFactory `scripts/ideation_dashboard/dashboard_refresh_lane.py:154`
      — identical at the frozen source `cb2d3a2c` and at today's `main`), and
      the SAME document already presumes that repository three times over: the
      pin diff is scoped to *"the `ideation-dashboard` entry inside the `images:`
      block"*, the authority requirement scopes the credential to *"the single
      image repository"*, and the boundary paragraph spells it *"the single
      `ideation-dashboard` IMAGE repository"*. So the normative sentence is the
      one place in the requirement where the repository half went missing, and a
      reader who implements from the SHALL alone can push somewhere the
      credential does not even reach. **§ 2.1's business**: the re-authoring
      states the push target as the complete repository-plus-tag reference and
      uses that one reference for the credential scope, so the push target and
      the credential scope are the same named thing rather than two phrasings a
      realization must reconcile.
