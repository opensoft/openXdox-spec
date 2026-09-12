# openXdox-spec

The **spec leg** of the `openxdox` project: requirements, decisions and
acceptance criteria. The implementation lives in
[`opensoft/openXdox-code`](https://github.com/opensoft/openXdox-code).

**Clone the assembly root, not this repository.** This leg is mounted as a
submodule at `spec/` inside
[`opensoft/openXdox`](https://github.com/opensoft/openXdox), which
is what pins the commit of this repository that the project currently is:

```sh
git clone --recurse-submodules https://github.com/opensoft/openXdox.git
cd openXdox
make bootstrap
```

Working here directly is fine — it is an ordinary repository with an ordinary
branch. What advancing this leg does NOT do is advance the project: that is a
commit in the assembly root moving the gitlink, `contracts/spec-pin.yaml` and
any workflow `@<sha>` reference together.

Being the spec leg confers no authority over specifications. The split is
navigation; authority travels in grants, and a project that keeps spec and
code in one repository is reviewed identically.

Topic: `xf-project-openxdox`.

## Posture

Contributing guidelines and the code of conduct for the `openXdox` project
live in the assembly root, not here:
[CONTRIBUTING.md](https://github.com/opensoft/openXdox/blob/main/CONTRIBUTING.md)
and
[CODE_OF_CONDUCT.md](https://github.com/opensoft/openXdox/blob/main/CODE_OF_CONDUCT.md).

Security reports for this repository go through [SECURITY.md](SECURITY.md).
The `validate` check is a required status check on `main`, enforced by a
repository ruleset — see [docs/branch-protection.md](docs/branch-protection.md).

## Documentation

The doc index for this repository. Everything under `docs/` is listed here,
and a new document is linked from this table in the same pull request that
adds it — the xFactory family's standing rule, levelled across all six
`openDox`/`openXdox` repositories by the OQ-O scaffold pass
(`opensoft/openxFactory#656`).

| document | what it is |
|---|---|
| [docs/branch-protection.md](docs/branch-protection.md) | the repository ruleset that makes `validate` a required status check on `main`, its `evaluate` → `active` history, and the one policy difference between the two families |
| [docs/domain-profile-design-note.md](docs/domain-profile-design-note.md) | `Status: draft` — the shape of the DOMAIN PROFILE the lifecycle engine reads instead of hardcoding one domain's status words (RULING C2, `split-opendox-two-layer-product` § 4.4): the five declaration axes, openxFactory's own engineering vocabulary as the worked example, the RULED lazy-proxy reach, and the per-site migration table the code half follows |
| [docs/gate-loop-view-contract.md](docs/gate-loop-view-contract.md) | `Status: draft` — the VIEW CONTRACT a contributed `ViewBinding` may assume about openDox's shell (openDox-spec `docs/front-end-package-boundary.md` § 5.1, the counterpart that note names and does not author): the twelve declared mount regions and what their hosts guarantee, the fourteen context-object fields marked STABLE or UNSETTLED, the `/capabilities` payload and its absent-vs-malformed answers, every refusal the seam composes today — and the twelve open questions S5 needs ruled before the gate loop can be contributed |
| [docs/stale-citations-erratum-2026-09-10.md](docs/stale-citations-erratum-2026-09-10.md) | BUILD-arc record: the source-path citations the carve left stale in the arrived examples README and two schemas, and their live targets, without editing the frozen files |

`openspec/project.md` is not a document in this sense — it is this leg's
OpenSpec instance file, read by the `openspec` CLI and by
`tests/test_leg_shape.py`.
