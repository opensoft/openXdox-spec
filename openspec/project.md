# openXdox-spec

This is the OpenSpec instance for the **spec leg** of the `openxdox` project.

`opensoft/openXdox-spec` holds requirements, decisions and acceptance criteria
for openXdox — openDox's openxFactory-tuned layer, split into three
repositories under the
[openRepoShape](https://github.com/opensoft/openRepoShape) standard: the
assembly root `opensoft/openXdox`, this spec leg, and the code leg
`opensoft/openXdox-code`. This repository is normally reached as the `spec/`
submodule of the assembly root; see that repository's `AGENTS-shape.md` for
the rules that span all three.

openXdox is the tuned layer over the neutral core: `opensoft/openXdox` pins
`opensoft/openDox` in `contracts/opendox-pin.yaml`, so requirements written
here describe the openxFactory-facing tuning, and requirements about the
neutral core belong in `opensoft/openDox-spec`.

## Conventions

- Proposals, specs and changes in this instance describe **this leg's**
  scope only: requirements, decisions and acceptance criteria for openXdox.
  Implementation work belongs in `opensoft/openXdox-code`.
- Follow the standard OpenSpec change lifecycle: `openspec/changes/<id>/`
  while a change is in flight, archived into `openspec/specs/` once landed.
- `OPENSPEC_TELEMETRY=0 openspec validate --all --strict` must pass before
  any change here is merged; the `validate` GitHub Actions workflow runs it
  on every pull request, and `tests/test_leg_shape.py` runs it again from
  pytest whenever the CLI is on PATH.
