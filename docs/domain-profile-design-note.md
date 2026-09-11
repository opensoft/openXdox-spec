# The Domain Profile the Lifecycle Engine Reads (RULING C2)

Status: draft
Kind: architecture
Repository context: openXdox-spec
Realizes: `domain-mapping-declaration` (ADDED by `openxFactory`
`openspec/changes/split-opendox-two-layer-product/specs/domain-mapping-declaration/spec.md`)
Closes-design-for: `split-opendox-two-layer-product` `tasks.md` § 4.4
Purpose: settle the SHAPE of the domain profile — what it declares, how the
lifecycle engine reaches it, where the first instance lives — so that § 4.4's
code half is a mechanical refactor against a written contract rather than an
invented one.
Topics: openxdox, domain-mapping-declaration, lifecycle, ruling-c2

> **This note designs; it does not build.** No engine code changes with it, no
> profile instance is authored by it, and the schema beside it
> (`contracts/schemas/domain-profile.schema.yaml`) is a DRAFT whose open shape
> questions are listed in § 8 and asked of Brett Heap as ASK-4 on
> `opensoft/openxFactory#656` (comment `5633855878`; the lane's CLAIM is
> comment `5633760341`). The code half — `gate_console.py` /
> `generator.py` at `opensoft/openXdox-code`, and the first concrete profile
> instance at `opensoft/openxFactory` — is RULED to start only after BUILD
> slice 2b lands, because it touches the same files
> (`openxFactory#656` comment `5628886636`, "Sequencing").

---

## 1. The gap, measured

RULING C2 (`openxFactory#656`, 2026-09-04T17:47Z) is that **openXdox is the
domain-mapping core, PARAMETERIZED by a domain profile that a descendant
supplies**, and that *"a clinician using `MedxDox` never sees the word
'requirement'"*. `tasks.md` § 4.4 states the consequence in one box:

> **PARAMETERIZE, do not ship one domain's words (RULING C2).** The lifecycle
> engine reads its status vocabulary, transitions, authorities and immutability
> point from a domain profile. A hardcoded status word is a defect under
> `domain-mapping-declaration`.

The engine does not do this today. A sweep of `opensoft/openXdox-code` `main`
`src/openxdox/` for `domain_profile|DomainProfile|status_vocabulary|
domain_mapping` returns **zero matches**, and the status words are literals in
the two busiest carved modules. Re-swept live for this note:

| # | file:line | literal | what it is |
|---|---|---|---|
| 1 | `gate_console.py:171` | `STAGED_STATUS = "staged"` | the module constant every other staged-status site reads |
| 2 | `gate_console.py:903` | `status_flip=STAGED_STATUS if is_outline else flip` | the outline arm of the demote plan |
| 3 | `gate_console.py:968` | `"kind": "staged"` | the demote transition manifest's destination kind |
| 4 | `gate_console.py:1151` | `if state in ("rejected", ...)` | terminal-state guard, first word |
| 5 | `gate_console.py:1151` | `if state in (..., "superseded")` | terminal-state guard, second word |
| 6 | `gate_console.py:1351` | `_flip_status(..., outline.status_flip or STAGED_STATUS)` | the status a returning primary fragment is flipped to |
| 7 | `gate_console.py:1374` | `_add_status_header(base, outline.status_flip or STAGED_STATUS)` | the status header written when the outline carries none |
| 8 | `gate_console.py:1651` | `"kind": "staged"` | the execution receipt's destination kind |
| 9 | `generator.py:349` | `if origin.get("kind") != "staged"` | the declared-origin reader's kind test |
| 10 | `generator.py:367` | `return "staged", parts[2]` | the declared-origin reader's return |

That is the ten the register records (`openxFactory#656` comment
`5628886636`: *"4.4's hardcoded status literals are now 10 across
`gate_console.py` / `generator.py`"*) — **ten sites over nine lines**, line
`1151` carrying two of them. Confirmed at current line numbers.

**The re-sweep finds six more LINES the count of ten does not include**, all of
the word `draft`: `gate_console.py:167` (`DRAFT_STATUS = "draft"`), `:826`,
`:1012`, `:1339` (which carries it twice), `:1487`, `:1569` — seven more
occurrences. They are not a new defect; they are the same defect, one status
word further along, and § 4.4's code half must migrate them on the same
accessor or it will leave half a vocabulary hardcoded.

Counted once and stated unambiguously, because the code half will work from
this number: **seventeen occurrences over fifteen lines**, across two module
constants (`STAGED_STATUS`, `DRAFT_STATUS`), two inline `"kind": "staged"`
literals, two in `generator.py`, and the two terminal words at `:1151`.

These words are `openxFactory`'s OWN `Status:` taxonomy
(`openxFactory/docs/document-lifecycle.md`, `Status: standard`), living inside
the domain-neutral `openxdox` package. That is verbatim the failure the
capability names:

> #### Scenario: openxFactory's own vocabulary is treated as neutral
> - **WHEN** `openxFactory`'s nine-word `Status:` taxonomy … is placed in the
>   neutral layer rather than in the engineering descendant's declaration
> - **THEN** the placement is refused under RULING C2

**A discrepancy this note records rather than resolves.** The packet and this
repository's own CLAUDE.md both call it the "nine-word" taxonomy, and both then
list eight words. `document-lifecycle.md`'s controlled table carries **eight**
rows — `brainstorm | staged | draft | ratified | standard | superseded |
retired | record`. The profile below declares the eight the live table carries.
The phrase "nine-word" is a citation defect somewhere upstream, not a ninth
status; it is flagged here for the register and is not this slice's to fix.

**What the fix is NOT.** Per RULED OQ-3 (`#656` comment `5547107565`),
`document-lifecycle` stays `openxFactory`'s vocabulary, *"exposed through its
own adapter"*, and no `document-lifecycle` delta is taken now. The fix is not to
erase the engineering column's words; it is to make the ENGINE read them from a
supplied profile, with `openxFactory`'s own adapter — D3's third column, RULING
DQ-1 — supplying that profile for itself, exactly as `MedxDox` will one day
supply its own.

---

## 2. The five axes

`domain-mapping-declaration`'s first ADDED requirement fixes the axis list, and
this note does not extend it. A profile declares exactly five:

1. **ARTIFACT KINDS** — the typed things the domain works on.
2. **LIFECYCLE** — per kind: the closed status vocabulary, every legal
   transition as an ordered pair, the AUTHORITY each transition requires, and
   the status at which the record becomes immutable-with-addenda.
3. **ACTS and GATES** — the verbs, and the gate each verb passes.
4. **EVIDENCE CLASSES** — what a derived statement must cite.
5. **PROMOTING AUTHORITIES** — named as roles, never as people.

The capability's second requirement adds two refusals the schema encodes
structurally rather than leaving to a reader: **a transition with no declared
authority is refused rather than defaulted to "any actor"**, and **a vocabulary
with no declared immutability point is refused rather than defaulted to
"never"** — *"both defaults are the permissive answer to a question the domain
was asked precisely because permissiveness is unsafe."* The third requirement
adds the TRUTH STORE a derived model may never write; for an engineering domain
the spec names it itself: *"the repository and its branch protection"*.

---

## 3. Worked example: `openxFactory`'s own engineering profile

The first — and today the only — profile. Sourced entirely from
`openxFactory/docs/document-lifecycle.md` (`Status: standard`), which is cited
per row rather than paraphrased. The machine-readable form of this section is
`contracts/schemas/domain-profile.example.yaml`; it is an EXAMPLE here, because
the REAL instance is authored at `openxFactory` in the code half.

### 3.1 Artifact kinds

| kind | what it is | where it lives |
|---|---|---|
| `governance-document` | a governance doc carrying the controlled `Status:` header | `docs/`, `ideation/` |
| `staging-topic` | a feat-spec-shaped fragment in the work queue | `ideation/staging/<topic>/` |
| `openspec-change` | an active proposal (proposal / tasks / design / spec deltas) | `openspec/changes/<id>/` |
| `evidence-record` | a generated report, simulation or audit | `review/`, `health/`, gate records |

### 3.2 Lifecycle — the closed vocabulary

`brainstorm`, `staged`, `draft`, `ratified`, `standard`, `superseded`,
`retired`, `record` (`document-lifecycle.md` § "Status", the controlled table).
The vocabulary is ORDERED in the profile, spine order, so a renderer has a
stable axis without inventing one.

### 3.3 Lifecycle — transitions and the authority each requires

Read off `document-lifecycle.md` § "Gates In Practice" and § "Status Claim
Rules". Authorities are role names the profile's authority axis also carries.

| from → to | authority | basis |
|---|---|---|
| `brainstorm` → `staged` | `lane-author` | *"brainstorm material is selected, deduplicated, and targeted into `ideation/staging/`"* |
| `staged` → `draft` | `change-author` | *"an OpenSpec change is created carrying the spec deltas … Proposed prose becomes `draft`"* |
| `draft` → `ratified` | `ratifying-authority` | *"Backed by an approved OpenSpec change, or by a durable ratification record"* |
| `ratified` → `standard` | `promoting-authority` | *"the change archives and its requirements live under canonical specs; affected docs may claim `standard`"* — and no document may claim `standard` unless a promoted spec or canonical contract backs it |
| `draft` → `staged` | `gate-actor` (human only) | the mechanized reverse transition, D16 — the gate console's `demote`; agents are structurally unable to author a gate-action record |
| `ratified` → `staged` | `gate-actor` (human only) | same act, applied to a ratified change being returned |
| `ratified` → `superseded` | `ratifying-authority` | *"Kept for provenance; header names the successor"* |
| `standard` → `superseded` | `ratifying-authority` | same rule, applied to a promoted document |
| `ratified` → `retired` | `ratifying-authority` | *"Withdrawn; header names the reason or decision record"* |
| `standard` → `retired` | `ratifying-authority` | same |
| → `record` | `evidence-producer` | out of band; a record is WRITTEN as a record and does not travel the spine |

`brainstorm` is the only status under which contradiction is legal, and
`record` is excluded from prose-to-spec conversion and contradiction checks —
both are declared as per-status flags rather than encoded in the engine.

### 3.4 Lifecycle — the immutability point

Per kind, because the engineering domain has two different answers and a single
scalar would be a lie:

- `governance-document`, `openspec-change`: **`ratified`**. Past ratification a
  document changes only through a cited OpenSpec change — the addendum — and
  post-ratification mutation of a proposal's declared origin is reported by the
  nightly `proposal-origin` doc-health family as a **contested** finding
  (`document-lifecycle.md` § "Origin at the proposal gate").
- `evidence-record`: **`record`**. *"Immutable evidence artifact"*; an error in
  one is corrected by a SEPARATE document, never by an edit. This repository
  carries the worked example:
  [docs/stale-citations-erratum-2026-09-10.md](stale-citations-erratum-2026-09-10.md)
  is precisely that addendum, written *"without mutating the frozen,
  byte-identical documents"*.

### 3.5 Acts and gates

The engineering domain's acts are the gate-console verbs already enumerated in
this repository at `contracts/schemas/gate-action-record.schema.yaml:165`:
`demote`, `edit-apply`, `ratify`, `kickoff`, `dispose-possible`, `propose`,
`lens-save-recipe`, `lens-add-as-cluster`, `create-document`, `edit-document`,
`open-pr`, `abandon-session`, `promote-to-staging`, `derive-possibles`,
`research-brief`, `create-project`, `edit-project`, `share-session`,
`cleanup-abandoned-branch`, `approve-model`. Every one passes the same gate:
**the human gate console** — an authenticated human actor, agent-invoked
actions refused before a record is ever written. The profile declares the act
list and names that gate; it does not restate the schema's per-action
conditionals, which stay where they are.

### 3.6 Evidence classes

The artifact kinds a gate-action record may cite, per the same schema's
per-action requirements: `ratification-record` (required by `ratify`),
`workflow-job` (required by `kickoff`, `propose`, `promote-to-staging`,
`derive-possibles`, `research-brief`), `register-update` (required by
`dispose-possible`), `document` (required by `create-document`), `commit`
(required by `edit-document`), `pull-request` (required by `open-pr`).

### 3.7 Promoting authorities, and the truth store

Roles, not people: `lane-author`, `change-author`, `gate-actor` (human-only),
`ratifying-authority`, `promoting-authority`, `evidence-producer`. The truth
store the engineering domain's derived models may never write is **the
repository and its branch protection** — named by the capability's third
requirement itself — with the external enforcement point being the repository
ruleset that makes `validate` a required check
([docs/branch-protection.md](branch-protection.md)).

---

## 4. How the engine reaches the profile

**RULED: the LAZY PROXY** (ASK-2, `openxFactory#656` comment `5628886636`):

> **RULED (2): LAZY PROXY** — a module in openDox-code resolves the profile at
> first attribute access; openxFactory registers the real module at process
> start; that operational contract is DOCUMENTED in the runbook.

The mechanism is already in the tree and tested: `openDox-code`
`src/opendox/consumer_reach.py` does exactly this for the `human_seen` class of
reach (`module(name, *, reason)` → `_LateConsumerModule`, `function(holder,
attr)` → `_LateConsumerCallable`, raising `ConsumerReachUnavailable` with the
layering spelled out instead of a `ModuleNotFoundError` from an import line a
thousand lines away). The profile rides the SAME mechanism.

**The attribute contract the § 4.3 slice must honour — named here, not built
here.** The lifecycle engine lives at `openXdox-code`
(`src/openxdox/gate_console.py`, `src/openxdox/generator.py`), one layer ABOVE
the `openDox-code` module the ruling names. § 4.3 settles the registration; this
note only fixes what the engine will ask for, so the two halves do not have to
be authored by the same hand:

- a module — working name `openxdox.domain_profile` — exposing
  **`current() -> DomainProfile`**, resolved LATE (first call, never import
  time) and raising a refusal that names the layering when no profile has been
  registered, on `consumer_reach`'s pattern;
- a **`DomainProfile`** object whose read surface is the five axes, with at
  minimum: `statuses` (ordered tuple), `status(name)`, `transitions` (ordered
  pairs with `authority`), `immutability_point(kind)`, `terminal_statuses`,
  `acts`, `evidence_classes`, `authorities`, `truth_store`, and the identity
  fields `mapping_id` / `neutral: false`;
- **registration at process start** by `openxFactory`'s own adapter, and by
  nothing in the neutral packages — the operational contract the ruling says is
  documented in the runbook. `openXdox-code` and `openDox-code` never import
  `openxFactory`; the direction the carve removed stays removed.

**Refusal, not a default.** When no profile is registered the engine refuses.
It does not fall back to the words it used to hardcode — a fallback is how the
literals would survive the refactor invisibly, and it is the permissive answer
the capability's second requirement already refuses twice.

---

## 5. Where the first instance lives, and how a descendant supplies its own

**First instance: `opensoft/openxFactory`** — D3's third column (the fifteen
engineering rows), which RULING DQ-1 keeps in `openxFactory` rather than
shedding: *"`openxFactory` KEEPS its own adapter"*. It is authored there in the
code half, not here, and not by this slice. The example beside this note is an
EXAMPLE.

**A future `MedxDox`** supplies its own profile the same way and changes no
neutral code: its own YAML instance, validated against this schema, registered
by its own adapter at process start. Its vocabulary is its own — the
capability's own worked case is a clinical note travelling `drafted → attested →
filed → immutable-with-addenda` — and *"all three are expressible in one engine,
because they differ in their words and not in their shape."* The neutral
`openxdox` package gains nothing, loses nothing, and never learns the word
`ratified`.

---

## 6. The migration table: literal → axis → accessor

What the code half does, per site. Mechanical once this note is settled.

| # | site | axis | accessor |
|---|---|---|---|
| 1 | `gate_console.py:171` `STAGED_STATUS` | lifecycle / vocabulary | `profile.status("organized")` — resolved by ROLE, not by the word |
| 2 | `gate_console.py:903` | lifecycle / transitions | the demote transition's declared `to` status |
| 3 | `gate_console.py:968` | artifact kinds | the destination kind of the `demote` transition |
| 4-5 | `gate_console.py:1151` `("rejected", "superseded")` | lifecycle / terminal statuses | `profile.terminal_statuses` (see § 8 Q4 — these are REGISTER-possible states, not document statuses) |
| 6 | `gate_console.py:1351` | lifecycle / vocabulary | same accessor as #1, via `outline.status_flip or …` |
| 7 | `gate_console.py:1374` | lifecycle / vocabulary | same accessor as #1 |
| 8 | `gate_console.py:1651` | artifact kinds | same accessor as #3, on the execution receipt |
| 9 | `generator.py:349` | artifact kinds | the declared-origin kind the profile names |
| 10 | `generator.py:367` | artifact kinds | same |
| +6 | `gate_console.py:167`, `:826`, `:1012`, `:1339` (×2), `:1487`, `:1569` (`DRAFT_STATUS`) | lifecycle / vocabulary | `profile.status("proposed")` — the same migration, the `draft` word |

**Resolve by ROLE, not by string.** `STAGED_STATUS` is not "the string
`staged`"; it is "the status this domain's documents carry while ORGANIZED".
A profile whose organized status is spelled `triaged` must work with no engine
change, which a `profile.statuses["staged"]` lookup would not deliver. The
lifecycle-state column of `document-lifecycle.md`'s own table (`captured |
organized | proposed | ratified | promoted | superseded | retired | out of
band`) is the neutral role vocabulary that makes this possible, and it is why
the schema carries a `role:` per status.

---

## 7. Out of scope

- **Any engine code.** No file at `openXdox-code` or `openDox-code` is touched
  by this slice; RULED sequencing holds them until BUILD slice 2b lands.
- **The real profile instance at `openxFactory`.** Authored in the code half.
- **A `document-lifecycle` delta.** Refused now by RULED OQ-3; the revisit
  trigger is named — `MedxDox`.
- **The § 4.3 registration point** (routes and subcommands). Same ruled
  mechanism, different payload; this note names only what the engine reads.
- **Enforcing transitions at runtime.** See § 8 Q3 — an open question, not a
  silent decision.
- **Correcting the "nine-word" citation** upstream (§ 1).

---

## 8. Open questions — ASK-4

Asked of Brett Heap on `openxFactory#656` in multi-choice form, comment
`5633855878`; the schema beside this note encodes the RECOMMENDED option in each
case and is redrafted on any other ruling. The full options and their trade-offs
are on that comment; the headlines are:

- **Q1 — carriage.** YAML loaded via the lazy proxy / a Python dataclass built
  by `openxFactory`'s adapter / both, YAML canonical and the dataclass the
  runtime form. *Recommended: both.*
- **Q2 — where the schema lives.** `openXdox-spec` (the enforcement side, this
  draft) / the `openxFactory` packet's `contracts/schemas/`.
  *Recommended: here.*
- **Q3 — enforcement depth in v1.** Vocabulary + immutability point read and
  enforced now, transitions and authorities DECLARED only / everything enforced
  at once / vocabulary only. *Recommended: the first.*
- **Q4 — `terminal_statuses`.** Whether `("rejected", "superseded")` at
  `gate_console.py:1151` becomes a declared axis field, and on which
  vocabulary — those two words are REGISTER-possible states, not document
  statuses, so the profile may need a second, per-kind vocabulary rather than
  one. *Recommended: a per-kind `terminal_statuses`.*
- **Q5 — one proxy or two.** The engine is at `openXdox-code` and the ruling
  names a module at `openDox-code`; whether one registration point serves both
  payloads or each leg carries its own. *Recommended: one registry, two
  accessors.*
