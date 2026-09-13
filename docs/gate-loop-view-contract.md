# The Gate Loop's View Contract (openDox-spec § 5.1)

Status: draft
Kind: architecture
Repository context: openXdox-spec
Realizes: `opensoft/openDox-spec` `docs/front-end-package-boundary.md` § 5.1 —
the openXdox-spec counterpart that note names and deliberately does not author
Closes-design-for: `split-opendox-two-layer-product` `tasks.md` § 3.4 slice S5
(the gate loop contributed behind a `ViewBinding`) — its PRECONDITION, not the
slice itself
Purpose: settle what a contributed `ViewBinding` may ASSUME about openDox's
shell — which regions it may name, what the context object holds, what the
capability probe carries, and what the shell says when a binding's `requires` is
unmet — so that S5's code half is a mechanical set of moves against a written
contract rather than an invented one.
Topics: openxdox, opendox, front-end, package-boundary, view-registry, slice-s5

> **This note designs; it does not build.** No file at `openDox-code` or
> `openXdox-code` moves with it, no binding is authored by it, and no test is
> written by it. What it adds is a measurement of the shell as the S3 view
> registry actually leaves it, stated as the contract S5 must satisfy. § 8
> carries the twelve questions a ruling had to settle before S5 starts; each was
> a point the shell has NOT fixed. **All twelve are now RULED** —
> Brett Heap, 2026-09-12, amendment #1 (§ 10) — and each is marked at the point
> it was decided; Q6 by a dedicated correction after the sitting's own closing
> line was found to have overstated it (§ 8, § 10). The measurements below are
> unchanged by the ruling.

**Everything measured here was read live on 2026-09-12 at these heads:**
`opensoft/openDox-code` branch `build/s3-view-registry` (PR
[#14](https://github.com/opensoft/openDox-code/pull/14))
`a497d7156f63a920a750171dfe9b9bd1fc06e8d7`; `opensoft/openDox-spec`
`docs/front-end-package-boundary.md` `61866d29bb21ed86e40709481c8e2cb357361fe6`;
`opensoft/openXdox-code` `main` `17384c07dd6aadaa30c35d333e7e83d5298dda43`;
`opensoft/openXdox-spec` `main` `ae59dfa5d81ed363c6655da9179478e083d02e2d`.
S3 is IN FLIGHT: PR #14 is open, and a fix round may move its head. Every
citation below is `path:line @ a497d715` unless another sha is named, and a
line that has moved is re-read before it is relied on.

---

## 1. The obligation, measured

openDox-spec's front-end boundary note names this document and stops. Its § 5.1,
verbatim, at `61866d29`:

> ### 5.1 The openXdox-spec counterpart this note does NOT author
>
> **S5 needs one, and it is not written here.** The gate-loop column's VIEW
> CONTRACT — what a contributed `ViewBinding` may assume about the shell (mount
> points, the context object's shape, the capability probe's payload, the
> refusal text when a binding's `requires` is unmet) — is a requirement ON
> openXdox, and by the same reasoning that put the domain-profile note at
> openXdox-spec it belongs at `opensoft/openXdox-spec` `docs/`. This note names
> the obligation and stops. Everything S1–S4 needs is here.

**Why the contract is a requirement ON openXdox, and therefore lands here.** The
same reasoning that put `docs/domain-profile-design-note.md` at this leg:
RULING C2 parameterizes openXdox by a profile *a descendant supplies*, so the
SHAPE of what the descendant supplies is openXdox's requirement even though the
reader of it is openDox's code. S5 inverts the direction and keeps the logic. The
boundary note's § 2.1 test for class B is *"delete the gate column and the file
has nothing left to render"*, and its S5 row is the column contributing four such
files back: `dispose.js`, `gate.js`, `swb-create.js`, `swb-session.js`, so that
*"a student install comes up with no gate bar, no dispose tray, no session verbs,
and no 404"*. openDox cannot state what those four files may assume — it does not
own them after S5. openXdox cannot discover it — the shell is openDox's. So the
contract is a requirement openXdox must MEET and openDox must HOLD, and a
requirement with two parties is a spec-leg document, which is what this is.

**What S3 actually delivered, and what it did not.** The registry exists in both
halves — `src/opendox/view_extension.py` (619 lines, the authority) and
`src/opendox/web/views/view_extension.js` (455 lines, the mirror) — and the shell
is wired through it: `app.js`:976–979 collects the core arm and the consumer
column through one `collectViewBindings`, and `app.js`:980 resolves the gate bar
by id instead of importing it. That is § 4.1's named example discharged.

Three things S5 needs are NOT delivered, and each is measured below rather than
assumed:

1. **Nothing mounts a contributed binding.** The tab router mounts only bindings
   that declared a `control` (`app.js`:656), and a contributed entry declaring
   one is refused where the payload is read
   (`views/view_extension.js`:322–332). The one place the shell mounts through
   the CONTRIBUTED-SHAPED path at all is `resolveView(views, "gate.bar")` at a
   single named call site (`app.js`:980) — and at this head that call resolves a
   binding still in the CORE arm and marked TRANSITIONAL there
   (`app.js`:590–599). S5 deletes that entry and the identical binding arrives
   through `contributedViewBindings()`, at which point the call site becomes the
   shell's only contributed mount and it is still BY ID, not generic: a second
   contributed binding would need a second openDox call site. **§ 8 Q1 —
   RULED, amendment #1 (§ 10):** a generic mount pass — after
   `collectViewBindings`, the shell mounts every contributed binding whose
   region is `dom` into that region's host, in declaration order; `shell`
   regions stay caller-driven, the gate bar kept as the declared exception.
2. **Nothing publishes a manifest.** `view_manifest`, `host_view_extensions` and
   `collect_view_bindings` have ZERO callers anywhere under `src/` outside the
   module that defines them (swept at `a497d715`). The server-side hop is
   S5's, as `views/view_extension.js`:286–288 says of itself.
3. **Nothing consults `requires`.** The field is declared
   (`view_extension.py`:248–251), validated (:321–329), carried into the
   manifest (:355) and mirrored in the client (`views/view_extension.js`:159–163,
   :185) — and no line of either half READS it to decide anything. The refusal
   text § 5.1 asks this note to settle therefore does not exist yet in code: § 5
   below records what the shell does say, and **§ 8 Q4 — RULED, amendment #1
   (§ 10)** — supplies the one it does not: dotted paths into the
   `/capabilities` payload, evaluated by the client at mount; unmet +
   `optional: true` contributes no content for that binding, with a named
   reason recorded (§ 2.2's region-sharing stands — nothing else already in
   the region is touched); unmet + required refuses, naming the binding, the
   path and the probed value.

---

## 2. The mount contract

### 2.1 The twelve regions

`REGIONS` is the whole of what a binding may name — `view_extension.py`:163–176,
mirrored at `views/view_extension.js`:69–82, and held to each other and to
`index.html` by `tests/test_view_registry.py`'s drift group. Nine `dom`, three
`shell`:

| region | kind | the host, measured |
|---|---|---|
| `view-funnel` | dom | `index.html`:77 — `<section class="view" id="view-funnel" role="tabpanel" aria-labelledby="tab-funnel">`, empty, VISIBLE at boot |
| `view-wheel` | dom | `index.html`:78 — same shape, `hidden` |
| `view-board` | dom | `index.html`:79 — same shape, `hidden` |
| `view-canvas` | dom | `index.html`:80 — same shape, `hidden` |
| `view-lens` | dom | `index.html`:81 — same shape, `hidden` |
| `view-docs` | dom | `index.html`:82 — same shape, `hidden` |
| `view-lineage` | dom | `index.html`:83 — same shape, `hidden` |
| `explorer-root` | dom | `index.html`:109 — `<div id="explorer-root"></div>`, no ARIA, never `hidden` |
| `staging-workbench-root` | dom | `index.html`:115 — `<div id="staging-workbench-root"></div>`, same |
| `viewer-gatebar` | shell | built per artifact: `views/viewer.js`:342 creates `el("div", "viewer-gate")` inside the viewer chrome and calls the caller's `mountGate` with it (:343–344) |
| `wheel-intent` | shell | **no host exists.** The string appears nowhere in the bundle outside the two `REGIONS` tables and one comment at `app.js`:1226 |
| `dispose-intent` | shell | **no host exists**, same sweep. S2 landed as `views/intent-binding.js`, a dynamic-import guard, and the chips render into a `span.intentchips` the tray itself creates (`views/dispose.js`:212–214) |

`dom_regions()` (`view_extension.py`:519–526) returns the nine in declared order;
`regionHost(binding, doc)` (`views/view_extension.js`:448–455) returns
`getElementById(binding.region)` for a `dom` region and REFUSES for a `shell`
one, because *"a 'shell' region has no standing element by definition, so asking
for one is a caller error rather than an absence"*.

**§ 8 Q9 — RULED, amendment #1 (§ 10):** both declared `shell` regions stand.
`wheel-intent` and `dispose-intent` stay declared in both halves, recorded here
as unhosted and unread today. Q1's generic mount pass never reaches either —
it walks `dom` regions only — so a binding naming one is not auto-mounted; and
because `regionHost()` REFUSES for a `shell` region (above), a caller that does
try to resolve one gets that refusal, not a silent no-op. Both facts are now
written down rather than left to be discovered.

**§ 8 Q8 — RULED, amendment #1 (§ 10): a thirteenth region, prospective, not
yet in the table above.** The table above measures the S3 head's twelve; the
row below is what the ruling adds for S5 to declare — kept separate so the
measured table stays a measurement:

| region | kind | the host, RULED (not yet in code) |
|---|---|---|
| `page-overlay` | shell | a fourth `shell` region: the shell builds it and hands it over, the same caller-driven handoff `viewer-gatebar` already uses (§ 2.1 above) — declared to end `views/dispose.js`:69's undeclared reach into `document.body` (§ 6.2) |

Once S5 declares it, this row moves into the table above and this note's
§ 9 does not call that a correction — the table has measured thirteen from
that point on.

### 2.2 What the host element guarantees — and what it does not

Measured against `app.js`'s tab router (`initTabs`, :647–693) and the seven core
views:

- **It is not emptied by the shell.** Every core view clears its own root on
  mount: `views/docs.js`:137, `views/wheel.js`:453, `views/funnel.js`:426,
  `views/board.js`:206, `views/canvas.js`:288, `views/lineage.js`:126,
  `views/explorer.js`:149, `views/staging-workbench.js`:323 — all
  `root.innerHTML = ""` or its `container`/`host` spelling. The shell never
  does it, so **two bindings sharing one region append to each other's output.**
  Sharing a region is legal: the collision refusal keys on `(region, id)`
  (`view_extension.py`:335–344, `views/view_extension.js`:191), and
  `tests/test_view_registry.py` asserts in as many words that one id in two
  regions is not a collision.
- **It is sized by CSS, not by the shell.** `styles.css`:144 —
  `.view { flex: 1 1 auto; min-height: 0; display: flex; flex-direction: column; }`
  — with `.view[hidden] { display: none; }` at :418. `explorer-root` and
  `staging-workbench-root` carry no `.view` class and no sizing of their own.
- **It is NOT re-mounted on a tab switch.** `show()` mounts once per `render()`
  cycle, guarded by a `rendered` Set (`app.js`:685–688), and thereafter calls
  `controllers[region].redraw()` when the controller exposes one (:689–691).
  Visibility is a `hidden` toggle (:673). A binding therefore mounts once and
  must survive being hidden and shown, and a binding that needs a redraw
  declares one by returning a controller with `redraw()`.
- **Mount order in a region is declaration order, flat.** `collect_view_bindings`
  keeps it deliberately (`view_extension.py`:455–462) and the core arm is first
  because the caller passes it first (`app.js`:977 before :978).

### 2.3 The `(region, id)` slot collision refusal

`collect_view_bindings` refuses two bindings claiming one slot, naming both
modules — `view_extension.py`:503–510, mirrored at
`views/view_extension.js`:253–261:

> two view bindings claim region `<region>` slot `<id>`: `<previous.module>` and
> `<binding.module>`. The second could never mount, and a panel that looks
> declared and never renders is worse than one that refuses.

For a contributing column this reads as one rule: **an id is unique within a
region across the core arm AND every contributed column**, and the core arm's
eight ids are reserved — `funnel.realization`, `wheel.deck`, `board.pipeline`,
`canvas.cluster`, `lens.keyword`, `docs.list`, `lineage.readiness`, `gate.bar`
(`app.js`:513–600). `gate.bar` is the one S5 deletes from the core arm and
re-supplies (`app.js`:590–595), so it is reserved TO openXdox and to nothing
else.

---

## 3. The context object

The object `initTabs` hands to every core binding's `mount(root, snap, ctx)` is
built at `app.js`:1220–1258. Fourteen fields. "Class" is the census class
(openDox-spec § 3.2) of the module that reads the field today.

**The marking rule, stated so it can be checked:** a field is **STABLE** when a
CLASS-A module already depends on it — openDox core cannot change it without
breaking itself, so a contributed binding may build on it. Every other field is
**UNSETTLED**: its only dependants are class-C or transitional-`?` modules, all
of which S4 and S7 are scheduled to rewrite, so a contributed binding that reads
one is building on a surface with no declared owner.

| # | field | shape at `a497d715` | read today by | |
|---|---|---|---|---|
| 1 | `views` | the COLLECTED registry, core arm then consumer column (`app.js`:976–979) | the tab router itself, `app.js`:656 (**A**) | **STABLE** |
| 2 | `nav` | six cross-view jumps: `openDoc`, `openLens`, `openCanvas`, `openWorkbench`, `openDraft`, `openRepository` (`app.js`:1184–1219) | `views/docs.js` via `ctx.nav.openDoc` (`app.js`:571, **A**); `wheel.js` (C); `lens.js` (`?`) | **STABLE** — but only the key `openDoc` has a class-A dependant |
| 3 | `caps` | the `/capabilities` payload, read-only-stripped under a composed view (`app.js`:954) | `wheel.js` (C) at :522; `lens.js` (`?`) at :538 | UNSETTLED |
| 4 | `explorer` | the mounted explorer controller (`app.js`:981), reached as `ctx.explorer.openTile` | `funnel.js` (C) :517; `board.js` (C) :527 | UNSETTLED |
| 5 | `notebook` | the NotebookLM tile action (`app.js`:1003) | `funnel.js`, `wheel.js`, `board.js`, `canvas.js` — all C | UNSETTLED |
| 6 | `composed` | boolean: this render is a composed multi-repository snapshot | `wheel.js` (C) :523 | UNSETTLED |
| 7 | `sourceBase` | `sourceBaseFor(active)` — the `/source/` prefix for the active key | `wheel.js` (C) :523 | UNSETTLED |
| 8 | `signal` | the render cycle's `AbortSignal` | `funnel.js` (C) :518; `wheel.js` (C) :523 | UNSETTLED |
| 9 | `probedCaps` | the UNSTRIPPED probe (`app.js`:945) | `lens.js` (`?`) :561, one affordance | UNSETTLED |
| 10 | `writableRepository` | `probedCaps?.repository \|\| null` (`app.js`:1237) | `lens.js` (`?`) :562 | UNSETTLED |
| 11 | `rawSnapshot` | the unnarrowed composed snapshot (`app.js`:1240) | `lens.js` (`?`) :539 | UNSETTLED |
| 12 | `visible` | the current visible repository set, or `null` (`app.js`:1240) | `lens.js` (`?`) :540 | UNSETTLED |
| 13 | `onVisible` | write-through for the visible set (`app.js`:1243–1247) | `lens.js` (`?`) :541 | UNSETTLED |
| 14 | `onDrillIn` | the repository-lens drill-in (`app.js`:1248–1257) | `lens.js` (`?`) :542 | UNSETTLED |

**Two STABLE, twelve UNSETTLED** — and the count is the finding. The context
object is not a designed interface; it is the union of what seven core views
happened to need, and twelve of its fourteen fields are read only by modules
S4 and S7 are scheduled to rewrite. A contributed binding may rely on `views`
and on `nav.openDoc` and on nothing else without a further ruling: § 8 Q3 and
Q4 are RULED (amendment #1, § 10) — the mount signature and the `requires`
refusal semantics — but which of the remaining twelve fields a binding may
read stays this table's STABLE/UNSETTLED marking, S7's to resolve.

**And the gate bar never receives this object at all.** `gate.bar` is not a tab,
so the tab router never mounts it; `app.js`:993–995 wraps it in a closure that
hands `mountGateBar` a host the VIEWER built, a per-artifact context the viewer
composed (`views/viewer.js`:344 — `{ changeId, path, repository, actor }`), and
an options object carrying exactly `{ caps }`. There are therefore TWO mount
signatures in the shell today and the contributed one is the minority case with
no snapshot in it. **§ 8 Q3 — RULED, amendment #1 (§ 10):** one signature,
`mount(host, snapshot, ctx)`, with the gate bar's shape kept as the one
declared exception until S5 rewrites it.

---

## 4. The capability probe

### 4.1 The payload as served

`GET /capabilities` is answered at `src/opendox/serve.py`:906–942. The body is
the startup verdict `compute_capabilities()` builds (:452–473) plus three
per-process or per-request additions:

| field | where | value |
|---|---|---|
| `actions.notebook` | `serve.py`:454 | `nlm` present AND real checkout AND loopback |
| `actions.gate` | :455 | a resolved actor AND a real checkout AND loopback |
| `actions.refresh` | :456 | a refresh binding resolved |
| `actions.session` | :457 | same predicate as `gate` |
| `actions.edit` | :458 | same predicate as `gate` |
| `actions.intent` | :464 | `not loopback` — the only capability true OFF loopback |
| `actor` | :466 | the local identity, or `null` |
| `refresh` | :467–472 | `{ binding, loopback_only }` |
| `console_token` | :1520–1523 | present only when `actions.session` |
| `repository` | :925–928 | per request: the ONE repository this serve can write to |
| `hosted_actor` | :939 | per request: the gateway-stamped `X-Auth-Request-User`, display-only |

There is **no `views` key**. `view_manifest()` (`view_extension.py`:577–619)
composes one — `schema_version`, `kind`, `facet`, `host_facet`, `host_profile`,
`regions`, `contributed_routes`, `views` — and nothing calls it. The one-line hop
that publishes it sits in `serve.py`'s own declared-edit window and is S5's, as
PR #14's body states.

### 4.2 How the client reads it

`probeCapabilities()` (`views/notebook.js`:33–41) fetches the route ONCE at load
with `cache: "no-store"`. **Any non-OK response or network failure degrades to
`{ actions: { notebook: false } }`** (:38) — an object with no `views` key —
which is how the static served image, which 404s the route, becomes an empty
consumer column without a single branch anywhere else.

| situation | the answer | where |
|---|---|---|
| no `/capabilities` at all (static image) | `[]` — empty column | `views/notebook.js`:38 then `views/view_extension.js`:294 |
| `views` absent or `null` | `[]` — empty column | `views/view_extension.js`:294 |
| `views` present but not an object, or an array | **REFUSES** | :295–298 |
| `kind` ≠ `"opendox.view-manifest"` | **REFUSES** | :299–302 |
| `schema_version` ≠ `1` | **REFUSES** | :303–308 |
| `views` not an array | **REFUSES** | :310–312 |
| an entry carrying `mount` or `control` | **REFUSES** | :322–332 |
| `contributed_routes` present but not an array | **REFUSES** | :339–358 |
| host registered, no `VIEW_EXTENSIONS` facet | `()` — empty column, NAMED | `view_extension.py`:568–574 with `host_facet: "absent"` (:593–608) |
| no host registered at all | **REFUSES** — `ProfileNotRegistered` passes through | `view_extension.py`:536–541 |

The asymmetry is argued at `view_extension.py`:533–562 and is the contract's
posture in one line: **absent is an empty column, malformed fails closed**,
because a payload that decides which code the shell imports is not something to
guess at.

### 4.3 `host_facet` — the named absence

`view_manifest(..., host_facet=..., host_profile=...)` admits exactly
`"declared"` or `"absent"` and refuses a third answer (`view_extension.py`:
598–602), so a host debugging a panel that never appeared reads the reason out of
the payload the page already fetched. For a contributing column this is the
difference between *"no host is registered"* (a refused build), *"a host is
registered and contributes no panels"* (`host_facet: "absent"` with the profile
named) and *"a host contributes panels and this is not one of them"* (a
`views` array that does not carry the id).

### 4.4 What `requires` may name — measured, and RULED

`ViewBinding.requires` is documented as *"Capability keys (`/capabilities`'
`actions`) or profile facets the binding needs. Consulted by the CLIENT at mount"*
(`view_extension.py`:248–251). Two measured facts stand against that sentence:

1. The ONE live value in the estate is `requires: ["actions.gate"]`
   (`app.js`:598) — a DOTTED PATH into the payload, not a key of `actions`.
2. **No client consults it.** The sweep for a read of `requires` across
   `src/opendox/web/` and `src/opendox/view_extension.py` at `a497d715` returns
   the declaration, the validation, the manifest field and the freeze — and no
   consumer. `tests/test_view_registry.py` touches it three times
   (:180, :830, :870), all of them shape assertions.

So the spelling and the semantics of `requires` are now RULED — **§ 8 Q4,
amendment #1 (§ 10), `opensoft/openxFactory#656` comment `5648049748`**: dotted
paths into the `/capabilities` payload, evaluated by the client at mount; unmet
+ `optional: true` contributes no content for that binding, with a named
reason recorded (§ 2.2's region-sharing stands — an unmet optional binding
does not clear anything else already mounted in the region); unmet + required
refuses, naming the binding, the path and the probed value. Until S5 lands the
code, a binding declaring `requires` is still declaring an intention the shell
does not yet act on.

---

## 5. The refusal text

**Scope: the ASSEMBLY-AND-RESOLVE path** — the refusals a contributing column
meets when its binding is collected, looked up, loaded and mounted. All are
`ViewBindingError` (`views/view_extension.js`:100–105;
`view_extension.py`:217–225): one class for every declaration defect, because
*"a caller does nothing different for any of them"*.

**The table below is NOT the seam's every refusal, and saying so is the point.**
A second family sits upstream of it — the per-field DECLARATION-SHAPE refusals a
binding's own author meets at construction: the id grammar, the entry grammar
and its dunder guard, the `view_class` membership, and the type of `routes`,
`requires` and `optional`. They are enumerated at `view_extension.py`:258–333 and
mirrored field for field at `views/view_extension.js`:122–193 — including the two
the S3 review added, the type-before-membership order on `region` and
`view_class` (`view_extension.py`:264–275) and the one compiled `_ENTRY` pattern
both halves share rather than each asking its own language what an identifier is
(:204–214). They are not repeated here because a column meets them before it
ships, whereas the eleven below are what a DEPLOYED assembly can still refuse.
Two further refusal families are tabled elsewhere in this note: the manifest-shape
refusals at § 4.2, and the non-conforming-extension refusals
(`view_extension.py`:475–497, `views/view_extension.js`:241–250) which belong to
whoever ASSEMBLES the shell rather than to a contributing column.

| # | when | the text, quoted | where |
|---|---|---|---|
| 1 | a required binding is absent | "no view binding `<id>` is registered. This shell was assembled without the column that contributes it; a binding that is correct to be absent must declare `optional: true` and be read with lookupView()." | `views/view_extension.js`:379–382 |
| 2 | an OPTIONAL binding is absent | *no text* — `lookupView` returns `null` (:365–370) and `resolveView` returns `null` (:399); the caller decides | :361–370, :397–399 |
| 3 | the module fails to load | "view binding `<id>` names module `<module>`, which failed to load: `<native message>`. A binding that cannot be mounted must not look registered." | :414–417 |
| 4 | the entry is not exported | "view binding `<id>` names entry `<entry>`, which `<module>` does not export. A binding that cannot be mounted must not look registered." | :428–431 |
| 5 | the entry is not a function | "view binding `<id>` names entry `<entry>`, which `<module>` exports as `<typeof>` rather than a function. An entry is the export that MOUNTS the panel; a binding that cannot be mounted must not look registered." | :434–438 |
| 6 | a region the shell does not declare | "view binding `<id>` names region `<region>`, which the shell does not declare (declared: …). A panel bound to a region that does not exist is silently unmounted." | :129–132 |
| 7 | a `shell` region asked for a standing element | "region `<region>` is a shell region: it has no standing element, and the shell hands its host to the binding at mount time" | :450–452 |
| 8 | a slot collision | quoted in full at § 2.3 | :255–260 |
| 9 | a non-class-B binding naming another column's route | "view binding `<id>` is class `<class>` and declares route `<pattern>`, which another column contributed. RULED Q3 …: a route constant travels with the BINDING THAT CALLS IT, never with the model that happens to declare it." | :264–269 |
| 10 | a contributed entry carrying `mount` or `control` | "the /capabilities `views` payload declares `<field>` on `<id>`: `mount` and `control` belong to the shell's own core arm and cannot cross the process boundary. A contributed binding names a module and an entry and is loaded through resolveView()." | :326–330 |
| 11 | a non-bundle-relative module specifier | "a contributed module must be a bundle-relative './…js' specifier that does not climb out of the bundle. An absolute URL is a remote script, which § 4.4's vendor policy forbids outright." | :134–141 |
| — | **an unmet `requires`** | **no code exists yet; RULED target (§ 8 Q4): required — refuses, naming the binding, the path and the probed value; optional — no throw, region gets no content from this binding, with a named reason recorded** | § 4.4 above; § 8 Q4 (RULED) |

**Two things a contributed binding may rely on today.** First, refusal #2: an
absent optional binding is a `null`, never a throw, and `views/viewer.js`:312–313
is the worked example downstream — `const mountGate = o.mountGate || null`, so
the viewer renders the document and no gate bar. Second, refusals #3–#5: a
binding that cannot be mounted never LOOKS registered, so a column may ship a
binding whose module is missing and get a named refusal rather than a raw
`TypeError` from inside a mount.

**And one thing it may not.** Every refusal above is thrown inside `render()`'s
`try` (`app.js`:834; the collect at :976, the resolve at :980) and caught at
`app.js`:1276–1279, which sets the human-visible text to:

> Could not load the snapshot (`<message>`). The renderer reads a single
> generated snapshot; regenerate it and reload.

A refused ASSEMBLY is therefore reported to the human as a SNAPSHOT defect, with
the seam's own carefully-composed message parenthesised inside advice that does
not apply. The messages are right; the frame around them is wrong. **§ 8 Q11 —
RULED, amendment #1 (§ 10):** the shell catches `ViewBindingError` separately
and reports it as an assembly refusal naming the binding, the rule and the
probed value — never again framed as a snapshot defect. *(The ruling names
all three; the RECOMMENDED text below only named the binding — the ruling
extends it.)*

---

## 6. What the gate loop needs

The four class-B files, each with the shell surface it reaches TODAY, stated as
the contract S5 must satisfy. The S5 success test is openDox-spec's own: *"a
student install comes up with no gate bar, no dispose tray, no session verbs, and
no 404."*

### 6.1 `views/gate.js` — 184 lines

| what it reaches | measured |
|---|---|
| host | `div.viewer-gate`, built per artifact by `views/viewer.js`:342 inside the viewer chrome, handed to the caller's `mountGate` (:343–344). Region `viewer-gatebar`, kind `shell` |
| mount signature | `mountGateBar(container, ctx, opts)` — `gate.js`:140 |
| its `ctx` | `{ changeId, path, repository, actor }` — composed by `views/viewer.js`:344, NOT the shell's context object |
| its `opts` | `{ caps }` — `app.js`:994; `opts.fetcher` is honoured (`gate.js`:175) and never supplied by the shell |
| capability | `caps?.actions?.gate` — `gate.js`:168; absent, the bar renders descriptors and does not execute |
| route | `GATE_RATIFY_ROUTE = "/actions/gate/ratify"` — `gate.js`:120, declared on the binding at `app.js`:598 |
| a SECOND export the shell uses | `isGateBearing(path)` — `gate.js`:32, reached at `app.js`:939 as `gateView.exports.isGateBearing`. The binding declares `entry: "mountGateBar"` and nothing else; the shell reaches past it through the namespace `resolveView` returns (`views/view_extension.js`:440) |
| bundle imports | **none** — `gate.js` keeps its own `el()` at :105–110, deliberately, "so its pure helpers keep running standalone under node" |
| CSS | `.viewer-gate` `styles.css`:771; `.gatebar` / `-title` / `-actions` / `-cmd` :772–777; `.gatebtn` :775 and `.gatebtn-live` |

This is the file S5 has the easiest path for: it is import-free, its binding
already exists in the core arm marked TRANSITIONAL (`app.js`:590–595), and
deleting that entry plus arriving through `contributedViewBindings()` changes
nothing else in `app.js`. What it still needs — Q2 (the second export), Q5
(where the bytes come from) and Q7 (the CSS) — **is now RULED (amendment #1,
§ 10):** the `exports` tuple names `isGateBearing`, and an undeclared reach
past that tuple is a refusal (extending the RECOMMENDED text below, which
named the tuple but not this consequence); the composed deployment assembles
the bundle, a contributed GET route kept as the hosted fallback; the CSS
travels with the binding, in its own sheet, against openDox's declared design
tokens as the one stable styling surface.

### 6.2 `views/dispose.js` — 427 lines

| what it reaches | measured |
|---|---|
| importers | `views/wheel.js`:73–74 (**class C**) takes EIGHT names — `appliedOutcome`, `commissionedVerb`, `commissionedWorkflow`, `gateCapable`, `mountDisposeTray`, `mountProposeButton`, `mountWheelVerb`, `panelEntry`; `views/swb-create.js`:30 and `views/swb-session.js`:70 take `panelEntry` |
| mount signatures | `mountDisposeTray(container, possible, opts)` :159; `mountProposeButton(container, topic, opts)` :269; `mountWheelVerb(container, item, opts)` :382 — three, none of them the core `mount(root, snap, ctx)` |
| the container | a rail element `wheel.js` built (call at `wheel.js`:1506); no declared region is involved |
| a page-level host | `ensurePanel()` appends a singleton `aside.refusalpanel` to `document.body` — `dispose.js`:69. **No region declares it** |
| capability | `caps.actions.gate` via `gateCapable(caps)` :46–48 |
| routes | `GATE_DISPOSE_ROUTE` :28, `GATE_PROPOSE_ROUTE` :29 — and a COMPUTED one at :396, `post("/actions/gate/" + verb, …)`, whose four verbs come from `wheel.js`:140–146 (`promote-to-staging`, `research-brief`, `derive-possibles`, `demote`) |
| bundle imports | `./helpers.js` (`el`) :25; `./intent-binding.js` (`emitIntent`, `renderIntentChips`) :26 — S2's optional guard |
| page-lifetime state | module-level `applied` and commission maps, and the singleton panel |
| CSS | `.disposetray` `styles.css`:1139–1140; `.disposebtn` :1141; `.refusalpanel` :1253 and thirteen further selectors |

**Two facts here are S5's hardest.** The computed route at :396 cannot be
declared as it is written: `ViewBinding.routes` admits only literal paths rooted
at `/` (`view_extension.py`:316–320), so the binding either enumerates the four
verbs or the ownership check never sees them (**§ 8 Q12 — RULED, amendment #1
(§ 10): the binding enumerates the four as literals**). And `wheel.js` is class
C with a STATIC import of this class-B module: § 4.5 assertion 3's breach, and
the reason the student install fails to load rather than 404s. S5 must convert
that import to the `intent-binding.js` shape or a registry lookup, or the "no
404" promise is a module-graph failure instead.

**The page-level host is also settled — § 2.1 carries the prospective row.**
§ 8 Q8 — RULED, amendment #1 (§ 10): a thirteenth region, `page-overlay` (kind
`shell`), is what the ruling adds as the host for page-level panels — not yet
in § 2.1's measured `REGIONS` table, which still measures the S3 head's
twelve; `ensurePanel()`'s reach into `document.body` above is the exact case
the ruling ends.

### 6.3 `views/swb-create.js` — 372 lines

| what it reaches | measured |
|---|---|
| importers | `views/staging-workbench.js`:88 (**class C**) — `mountCreateAffordance`, `openCreateDialog`, `createGateLive` |
| mount signatures | `mountCreateAffordance(host, seed, opts)` :345; `openCreateDialog(host, seed, opts)` :367 — call sites `staging-workbench.js`:1789, :1794, :3181 |
| capability | `caps.actions.gate` via `createGateLive(caps)` :36–38; `caps.actor` at :249 and :331 |
| route | `CREATE_ROUTE = "/actions/gate/create-document"` — declared NOT here but at `views/staging-workbench-model.js`:543, a **SPLIT** file |
| bundle imports | `./helpers.js` :29; `./dispose.js` (`panelEntry`) :30; and SIX names from `./staging-workbench-model.js` :31–35 — `CONTINUATIONS`, `CREATE_ROUTE`, `consoleHeaders`, `createDocumentCommand`, `createRequest`, `withConsoleRepair` |

### 6.4 `views/swb-session.js` — 614 lines

| what it reaches | measured |
|---|---|
| importers | `views/staging-workbench.js`:90–92 (**class C**); and **`app.js`:57 (class A)** — `firstEditTransport`, used at `app.js`:1134 |
| mount signature | `mountSessionAffordances(host, ctx, opts)` :573, call site `staging-workbench.js`:1826 |
| a NON-panel export | `firstEditTransport({ fetcher, caps, repair })` :190 — a transport, not a panel, and a `ViewBinding` binds a panel at a region |
| capability | `caps.actions.session` via `sessionActionsLive` / `sessionSurfaceHidden`; `caps.console_token` via `consoleHeaders` |
| routes | `EDIT_DOCUMENT_ROUTE` :817, `OPEN_PR_ROUTE` :818, `FIRST_EDIT_ROUTE` :821, `ABANDON_SESSION_ROUTE` :822, `SHARE_SESSION_ROUTE` :826 — all declared at `views/staging-workbench-model.js`, a **SPLIT** file |
| bundle imports | `./helpers.js` :69; `./dispose.js` (`panelEntry`) :70; and EIGHTEEN names from `./staging-workbench-model.js` :71–80 |

**`app.js`:57 is the shell's remaining class-A → class-B import.** § 4.1 named
only line 43, and S3 removed it; this one is still a static `import` at the S3
head. It is not a panel, so the registry as built has no shape for it. **§ 8
Q10 — RULED, amendment #1 (§ 10):** it travels as a declared non-mount export
of the workbench's contributed binding (Q2's `exports` tuple), reached through
`resolveView` at this one call site, with a refusal-shaped fallback when the
binding is absent.

### 6.5 The thirteen route constants, and where they sit at the S3 head

openDox-spec § 1.2(c) measures thirteen gate route constants in the tree. At
`a497d715` they are exactly:

| file | lines | constants | class |
|---|---|---|---|
| `views/gate.js` | 120 | `GATE_RATIFY_ROUTE` | B |
| `views/dispose.js` | 28, 29 | `GATE_DISPOSE_ROUTE`, `GATE_PROPOSE_ROUTE` | B |
| `views/staging-workbench-model.js` | 543, 817, 818, 821, 822, 826 | `CREATE_ROUTE`, `EDIT_DOCUMENT_ROUTE`, `OPEN_PR_ROUTE`, `FIRST_EDIT_ROUTE`, `ABANDON_SESSION_ROUTE`, `SHARE_SESSION_ROUTE` | SPLIT |
| `views/repo-selector.js` | 39, 43 | `ACTIONS_CREATE_PROJECT_ROUTE`, `ACTIONS_EDIT_PROJECT_ROUTE` | SPLIT |
| `views/lens-model.js` | 1036, 1037 | `LENS_SAVE_ROUTE`, `LENS_CLUSTER_ROUTE` | SPLIT |

Three sit in class-B files; **ten sit in the three SPLIT files S4 has not split
yet**, which is precisely openDox-spec's S4 row: *"the gate loop cannot be
contributed until its route table stops living outside class B."* This note
adds one measured consequence: two of the four class-B files IMPORT their routes
from `staging-workbench-model.js` (§ 6.3, § 6.4), so S4 is not merely a
precondition for the ownership assertion — it is a precondition for the four
files being MOVABLE at all.

### 6.6 What the other side of the seam looks like

`ACTIONS_GATE_PREFIX = "/actions/gate/"` — `openXdox-code`
`src/openxdox/serve_gate.py`:55 @ `17384c07` — is contributed as
`route_extension.RouteBinding("POST", ACTIONS_GATE_PREFIX, True, …)` at :243.
When openXdox is registered, `view_manifest`'s `contributed_routes`
(`view_extension.py`:610–617) therefore carries that prefix, and the ownership
refusal (§ 5 row 9) becomes live for every non-class-B binding: a class-A or
class-C binding declaring any `/actions/gate/*` route is refused where it is
read. Class B is exempt by construction, which is the boundary working.

---

## 7. Out of scope

- **S5's code.** No binding is authored here; no file at `openDox-code` or
  `openXdox-code` moves. The four class-B files are measured, not touched.
- **The openDox-side registry itself.** `view_extension.py` and
  `views/view_extension.js` are S3's and are IN FLIGHT at PR #14. This note
  measures them and asks about the gaps; it proposes no edit to either.
- **S4.** The three SPLIT files and the ten route constants in them are S4's,
  and § 6.5 records only that S5 cannot start until they move.
- **S6.** `/source/` re-homing is RULED Q4 and belongs to `serve_projection.py`
  and `serve.py`, not to any binding.
- **S7.** The display facet, the context hop and the class-C vocabulary. This
  note's § 3 marks context fields STABLE/UNSETTLED and does not propose the
  facet's shape — `docs/domain-profile-design-note.md` already owns that.
- **The census, the classes and the four boundary assertions.** All are
  openDox-spec's, at `docs/front-end-package-boundary.md` §§ 2–4.5.
- **Whether a descendant other than openXdox contributes views.** The contract
  is stated over "a contributing column"; naming a second one is a later
  ruling's.

---

## 8. Open questions for Brett Heap — Q1–Q12 ALL RULED (amendment #1)

Twelve were asked, each a point the S3 shell had NOT fixed, each carrying a
RECOMMENDED answer. **All twelve are now RULED** — Brett Heap, 2026-09-12, by
interactive multi-choice, `opensoft/openxFactory#656` comments `5648044785`,
`5648049748`, `5648065587` and `5649094228` — the RECOMMENDED answer adopted
in every case. Q6 was the one exception at first: the sitting's closing
comment (`5648065587`) asserted all twelve were ruled, but that sitting gave
Q6 (this note's own, on bundle imports) no dedicated bullet — a gap Copilot's
review of this PR caught independently. `5649094228` corrects that
overstatement and rules Q6 on its own terms (see Q6's own note below). What
follows is the as-asked record: the measurement and the RECOMMENDED answer
stand as first written, and each ruled question now also carries the line
marking where and when it was decided. § 10 carries the amendment record.

**Q1 — Does the shell MOUNT contributed bindings, or must every one have a named
reader?** Measured: nothing generic mounts a contributed binding. The tab router
mounts only bindings that declared a `control` (`app.js`:656) and a contributed
entry declaring one is refused (`views/view_extension.js`:322–332); the one
contributed-shaped mount is `resolveView(views, "gate.bar")` BY ID at
`app.js`:980, and at this head it resolves the transitional CORE-arm binding
(`app.js`:590–599), not a contributed one. Either way the mechanism is the same:
one openDox call site per binding, named in openDox's own source. So a column
can contribute a binding today and have nothing ever call it.
**RECOMMENDED: a generic mount pass.** After `collectViewBindings`, the shell
mounts every contributed binding whose region is `dom` into that region's host,
in declaration order, and leaves `shell` regions caller-driven. *Without it every
contributed panel needs an openDox edit to become reachable, which is the fork
the seam was drawn to prevent; with it the gate bar stays the declared
exception, because its host is built per artifact and not per render.*

**RULED — the RECOMMENDED answer adopted.** Brett Heap, 2026-09-12,
opensoft/openxFactory#656 comment 5648044785, by interactive multi-choice.

**Q2 — Is a binding's contract its `entry`, or its whole module namespace?**
Measured: `resolveView` returns `{ binding, exports }` — the whole namespace
(`views/view_extension.js`:440) — and `app.js`:939 reads
`gateView.exports.isGateBearing`, an export the binding never declared and the
seam never validated. Only `entry` is checked callable (:427–439).
**RECOMMENDED: the namespace is the contract, and a binding declares it** — add
an `exports` tuple validated exactly as `entry` is, so `isGateBearing` is NAMED
rather than reached past the declaration. *The alternative — one entry only, with
`isGateBearing` folded into the mount's return — is cleaner but changes
`viewer.js`'s gate-bearing decision from a predicate into a mount, which is a
behaviour change inside a class-A file.*

**RULED — the RECOMMENDED answer adopted, and extended.** Brett Heap,
2026-09-12, opensoft/openxFactory#656 comment 5648049748, by interactive
multi-choice: *"an undeclared reach (today `isGateBearing`, app.js:939) is a
refusal"* — the ruling states this consequence explicitly; the RECOMMENDED
text above named the `exports` tuple but not this. § 6.1's restatement
carries the fuller wording.

**Q3 — What is a contributed binding's mount SIGNATURE?** Measured: two exist. A
core tab is `mount(root, snap, ctx)` (`app.js`:516 and the six after it). The one
contributed-shaped mount is `mountGateBar(container, ctx, opts)` (`gate.js`:140),
called with a host the viewer built, a per-artifact context
(`views/viewer.js`:344) and `{ caps }` (`app.js`:994) — no snapshot, and a third
argument. `dispose.js` adds three more shapes (§ 6.2).
**RECOMMENDED: one signature — `mount(host, snapshot, ctx)` — with per-invocation
data carried in `ctx`, and the gate bar's shape kept as a DECLARED exception
named in this note.** *Two undeclared signatures is how a contributing column
learns the contract by reading `app.js`, which is the coupling the registry
exists to end.*

**RULED — the RECOMMENDED answer adopted.** Brett Heap, 2026-09-12,
opensoft/openxFactory#656 comment 5648044785, by interactive multi-choice.

**Q4 — What may `requires` name, and what does the shell DO when it is unmet?**
Measured: nothing consults `requires` at the S3 head (§ 4.4); the docstring says
"capability keys … or profile facets" (`view_extension.py`:248–251) and the one
live value is the dotted path `"actions.gate"` (`app.js`:598). This is the
obligation § 5.1 names most directly, and it is the one with no code behind it.
**RECOMMENDED: `requires` names DOTTED PATHS into the `/capabilities` payload,
evaluated by the client at mount; an unmet `requires` on an `optional: true`
binding leaves the region empty with a named reason, and on a required binding
refuses, naming the binding, the unmet path and the probed value.** *That is
`view_extension.py`'s own absent/malformed posture applied one tier in, and it
makes `requires: ["actions.gate"]` — already written — correct rather than
aspirational. Profile facets would need a second namespace and no binding asks
for one yet.*

**RULED — the RECOMMENDED answer adopted.** Brett Heap, 2026-09-12,
opensoft/openxFactory#656 comment 5648049748, by interactive multi-choice.

**Q5 — Where do a contributed module's BYTES come from?** Measured, and the
sharpest gap: `_MODULE` admits only a bundle-relative `./…js`
(`view_extension.py`:193–202), `resolveView` resolves it against the bundle root
(`views/view_extension.js`:400), and `build_server` serves ONE directory
(`serve.py`:1596; default `--web-dir` at :1743). `openXdox-code` `main`
`17384c07` carries no `.js` file at all. So a module openXdox contributes has no
route into the directory the browser imports from — except that a contributed
GET route is consulted BEFORE the static fallback (`serve.py`:952–970), which
makes `GET /views/gate.js` answerable by a `RouteBinding` whose handler is a
method on the bound handler class (`serve.py`:1591–1595 refuses a build
otherwise).
**RECOMMENDED: the composed DEPLOYMENT assembles the bundle** — openXdox ships
its class-B modules as package data and the install step places them in the
served `web/` — **with the contributed-GET-route path kept as the hosted
fallback and declared here as the second lawful mechanism.** *Naming this is
S5's real precondition: the registry refuses everything that is not
bundle-relative, and nothing in either leg puts a file there today.*

**RULED — the RECOMMENDED answer adopted.** Brett Heap, 2026-09-12,
opensoft/openxFactory#656 comment 5648044785, by interactive multi-choice.

**Q6 — What may a contributed module IMPORT from the bundle?** Measured: three
of the four class-B files import `./helpers.js` (`dispose.js`:25,
`swb-create.js`:29, `swb-session.js`:69) and two of them import six and eighteen
names from `views/staging-workbench-model.js` (§ 6.3, § 6.4). `gate.js` imports
nothing and keeps its own `el()` (:105–110).
**RECOMMENDED: the contract guarantees `./views/helpers.js` and nothing else.**
*Every other openDox module a contributed binding reaches is either vendored by
the contributing column or added to a declared guarantee list by a ruling; the
`staging-workbench-model.js` names are S4's to resolve first, and `gate.js`
already shows the import-free posture is achievable.*

**RULED — the RECOMMENDED answer adopted.** Brett Heap, 2026-09-12,
opensoft/openxFactory#656 comment 5649094228, by interactive multi-choice.
*This is a dedicated ruling, not the blanket closing line in `5648065587` —
that sitting's closing comment named the BOUNDARY note's Q6 (the S8
re-destination form, ruled separately at `5648044785`), not this note's own
Q6; `5649094228` corrects the overstatement and rules this Q6 on its own
terms (§ 10).*

**Q7 — Where does a contributed binding's CSS live?** Measured: every class-B
selector sits in openDox's `styles.css` — `.viewer-gate` :771, `.gatebar*`
:772–777, `.disposetray` :1139–1140, `.disposebtn` :1141, `.refusalpanel` :1253
and thirteen more. § 4.4's vendor policy forbids a contributed binding adding to
`web/vendor/` and says nothing about styling.
**RECOMMENDED: a contributed binding's styles travel with it, in its own
stylesheet the binding loads, and openDox's design tokens (`--st-*`, `--panel`,
`--ink`, `--border`, `--faint`, `--mono`, `--sans`) are the declared stable
surface it may use.** *Leaving them in openDox's sheet ships the gate loop's
appearance to every student install, which is the same defect as shipping its
routes.*

**RULED — the RECOMMENDED answer adopted.** Brett Heap, 2026-09-12,
opensoft/openxFactory#656 comment 5648049748, by interactive multi-choice.

**Q8 — Is a page-level host inside the contract?** Measured:
`views/dispose.js`:69 appends a singleton `aside.refusalpanel` to
`document.body` — a mount point no region declares — and `panelEntry` is imported
by `wheel.js` (C), `swb-create.js` and `swb-session.js`.
**RECOMMENDED: declare a `page-overlay` region of kind `shell` that the shell
builds and hands over.** *An undeclared reach into `document.body` is exactly
the silence the `REGIONS` table exists to end, and a contributed column
appending to the body is a collision nothing can refuse.*

**RULED — the RECOMMENDED answer adopted.** Brett Heap, 2026-09-12,
opensoft/openxFactory#656 comment 5648049748, by interactive multi-choice.

**Q9 — Do the two declared-but-unhosted `shell` regions stand?** Measured:
`wheel-intent` and `dispose-intent` are declared in both halves
(`view_extension.py`:174–175, `views/view_extension.js`:80–81) and appear nowhere
else in the bundle; S2 landed instead as `views/intent-binding.js` and the chips
render into a `span.intentchips` the tray creates (`dispose.js`:212–214).
**RECOMMENDED: keep both declared, and record here that they are unhosted and
unread.** *The registry's own argument — "declaring a region costs nothing and
refuses nothing; an undeclared one costs a slice" — holds, and S5 is not the
slice to retire S2's provision. But a contributed binding naming one today
mounts into nothing, and that must be written down rather than discovered.*

**RULED — the RECOMMENDED answer adopted.** Brett Heap, 2026-09-12,
opensoft/openxFactory#656 comment 5648065587, by interactive multi-choice.

**Q10 — How does the shell's remaining class-A → class-B import travel?**
Measured: `app.js`:57 statically imports `firstEditTransport` from
`views/swb-session.js` (class B) and calls it at :1134. § 4.1 named only line 43,
which S3 removed. A transport is not a panel, and a `ViewBinding` binds a panel
at a region.
**RECOMMENDED: it travels as a declared non-mount export (Q2) of the workbench's
contributed binding, reached by `resolveView` at that one call site, with the
doxBench Save falling back to a refusal-shaped transport when no gate column is
registered.** *A second, region-free extension point for contributed FUNCTIONS
would work and would be a second seam, which § 4.1's whole argument is against.*

**RULED — the RECOMMENDED answer adopted.** Brett Heap, 2026-09-12,
opensoft/openxFactory#656 comment 5648065587, by interactive multi-choice.

**Q11 — What does a human see when the registry refuses?** Measured: every
`ViewBindingError` from `collectViewBindings` (`app.js`:976) or `resolveView`
(:980) is caught by `render()`'s handler at :1276–1279 and reported as *"Could
not load the snapshot (…). The renderer reads a single generated snapshot;
regenerate it and reload."* A refused assembly is shown to the human as a
snapshot defect.
**RECOMMENDED: catch `ViewBindingError` separately and report it as an assembly
refusal, naming the binding.** *The seam already composes the right sentence;
only the frame around it is wrong, and a column debugging its own contribution
is currently told to regenerate a snapshot that is fine.*

**RULED — the RECOMMENDED answer adopted, and extended.** Brett Heap,
2026-09-12, opensoft/openxFactory#656 comment 5648065587, by interactive
multi-choice: *"shows a registry refusal naming the binding, the rule and the
value"* — the ruling names all three; the RECOMMENDED text above named only
the binding. § 5's restatement carries the fuller wording.

**Q12 — How does a binding declare a route it COMPUTES?** Measured:
`views/dispose.js`:396 posts to `"/actions/gate/" + verb`, with the four verbs
supplied by its caller (`views/wheel.js`:140–146: `promote-to-staging`,
`research-brief`, `derive-possibles`, `demote`). `ViewBinding.routes` admits only
literal paths rooted at `/` (`view_extension.py`:316–320), and the ownership
refusal matches a declared route against a contributed pattern, with prefix
semantics on the CONTRIBUTED side only (:419–428). So a computed route is
invisible to the check that exists to catch exactly this.
**RECOMMENDED: the binding ENUMERATES the four, as literals.** *They are a closed
set the caller already spells out, and enumerating them keeps `routes` a
declaration of ownership rather than a pattern language. Admitting a prefix on
the DECLARING side would let one binding claim a whole namespace, which is the
property the contributed side's `is_prefix` is carefully limited to.*

**RULED — the RECOMMENDED answer adopted.** Brett Heap, 2026-09-12,
opensoft/openxFactory#656 comment 5648065587, by interactive multi-choice.

---

## 9. Corrections

None. This note is at its first revision; corrections to it are recorded here,
in the shape `docs/domain-profile-design-note.md` § 9 uses — what was asserted,
what was true, who caught it, where the retraction is on the record, and what
the error did and did not damage.

---

## 10. Amendments

**Amendment #1 — 2026-09-12 — § 8's twelve open questions: ALL TWELVE
RULED.** Brett Heap ruled all twelve, by interactive multi-choice, across
four comments on `opensoft/openxFactory#656` — three in one sitting and a
fourth, corrective one after this PR's third Copilot review:
[`5648044785`](https://github.com/opensoft/openxFactory/issues/656#issuecomment-5648044785)
(Q1, Q3, Q5, and separately the boundary note's own Q6 — a different document's
question of the same number, not this note's),
[`5648049748`](https://github.com/opensoft/openxFactory/issues/656#issuecomment-5648049748)
(Q2, Q4, Q7, Q8),
[`5648065587`](https://github.com/opensoft/openxFactory/issues/656#issuecomment-5648065587)
(Q9, Q10, Q11, Q12, and a closing line that OVERSTATED coverage of this
note's own Q6 — see below), and
[`5649094228`](https://github.com/opensoft/openxFactory/issues/656#issuecomment-5649094228)
(Q6, this note's own, on bundle imports, correcting that overstatement).

- **Q6 was the exception, and is now corrected.** `5648065587`'s closing
  line says *"All twelve counterpart questions ... are now RULED,"* but none
  of the sitting's three comments gave this note's own Q6 (bundle imports) a
  dedicated bullet or selected among its options the way Q1–Q5 and Q7–Q12
  each were — Copilot's third review of this PR (discussion `r3997363266`,
  thread `PRRT_kwDOUPv77M6hzBPy`) caught the same gap independently and
  disputed the "left open" framing this amendment first recorded, asking
  either for Q6 to be ruled or for an explicit correction. `5649094228` —
  **CORRECTION + RULING, 2026-09-12, by interactive multi-choice** —
  supplies both: it names what `5648065587`'s closing line actually
  overstated (that line closed the BOUNDARY note's Q6, the S8 re-destination
  form, ruled separately at `5648044785` — not this note's), and it rules
  this note's own Q6 on its own terms: **a contributed module may import
  `./views/helpers.js` and nothing else.** § 8 Q6 now reads RULED, citing
  `5649094228`; the amendment title above reads ALL TWELVE.
- **What changed, at this amendment's original commit.** § 8: each of Q1–Q5
  and Q7–Q12 gained a `RULED` line naming the ruling and its comment id; Q6
  gained an explicit open note instead — superseded by the Q6 bullet above,
  so § 8 now reads Q1–Q12 RULED throughout. §§ 1–6: every place that framed
  one of those eleven questions as still open or undecided — the mount pass
  (Q1), the `requires` refusal semantics (Q4, § 1 and § 4.4), the
  mount-signature count (Q3, § 3), the STABLE/UNSETTLED cross-reference
  (Q3/Q4, § 3), the unhosted `shell` regions (Q9, § 2.1), the
  unmet-`requires` refusal row and the snapshot-defect framing (Q4/Q11, § 5),
  the gate.js exports/bytes/CSS trio (Q2/Q5/Q7, § 6.1), the page-level host
  and the computed route (Q8/Q12, § 6.2), and the `firstEditTransport` shape
  (Q10, § 6.4) — was restated as settled, with the ruling cited in place. §§
  1–6 carry no Q6-specific SETTLED/RULING prose to restate (§§ 6.1–6.4's own
  bundle-import MEASUREMENT rows are untouched by this amendment, same as
  every other measurement) — Q6's only settled-wording home is § 8 — so
  there was nothing to restate there for Q6, then or since.
  The measurements themselves (what the S3 shell actually does today) are
  untouched throughout; only what was said to be open moved to what is now
  decided. § 9's "None" stands for THIS NOTE'S own assertions: nothing here
  has ever corrected an error this note made, and every RECOMMENDED answer
  it already carried — Q6's included — was adopted as written. What
  `5649094228` corrects is `5648065587`'s own closing line, on the issue
  thread, not anything this note asserted.
- **Fix round 1 (same PR, after Copilot's first review)** sharpened two of
  the new restatements: the Q9 note no longer says a `shell`-region binding
  "mounts into nothing" — it now separates the two true facts (Q1's mount
  pass never reaches a `shell` region; `regionHost()` REFUSES for one rather
  than no-opping) — and § 2.1 gained the Q8 cross-reference (a ruled
  thirteenth region, `page-overlay`, not yet in the measured twelve), matched
  in the README's doc-index row.
- **Fix round 2 (same PR, after Copilot's second review)** made three more
  corrections: reversed Q6 from RULED to open, pending a dedicated ruling
  (subsequently supplied by `5649094228` — see the Q6 bullet above);
  reworded the Q4
  restatements so "empties the region" cannot be read as clearing a SHARED
  region against § 2.2's no-emptying rule — a binding with an unmet optional
  `requires` contributes no content of its own, nothing else in the region is
  touched; completed the Q11 restatement, which had dropped two of the three
  things the ruling names (the shell now names the binding, the rule AND the
  probed value, not the binding alone); and completed the Q2 restatement to
  say what the ruling adds beyond the original recommendation — an
  undeclared reach past the `exports` tuple is a refusal. § 2.1 also gained
  an explicit prospective row for `page-overlay`, kept out of the measured
  `REGIONS` table.
- **What did not change.** The `Status: draft` header, the § 8 questions'
  MEASURED/RECOMMENDED text (kept verbatim as the as-asked record), and every
  citation's underlying line numbers and shas.
- **Consequences, per the ruling comments.** These twelve rulings are now
  S5's and S8's design inputs; S5 (§ 3.4, contributing the gate loop) is
  authored on top of S4's leg under this contract, and the Q5
  package-data/composed-assembly seam binds the S5 brief. S5 can now also
  rely on Q6's import guarantee as settled: `./views/helpers.js` and
  nothing else.
