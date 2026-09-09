"""Asserts the bootstrap posture of this leg (openXdox-spec) is in place.

This is the required pytest suite `.github/workflows/validate.yml` runs on
every pull request. It checks the files that must exist at creation for a
public repository (LICENSE, SECURITY.md, CODEOWNERS), this leg's own role
directory (`requirements/`), and — because this is the SPEC leg — that an
OpenSpec instance exists under `openspec/` and validates strictly when the
CLI is on PATH.
"""

from __future__ import annotations

import shutil
import subprocess
import os
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    ".gitignore",
    "LICENSE",
    "SECURITY.md",
    ".github/CODEOWNERS",
]


@pytest.mark.parametrize("relpath", REQUIRED_FILES)
def test_required_file_exists(relpath: str) -> None:
    path = ROOT / relpath
    assert path.is_file(), f"required posture file {relpath!r} is missing"


def test_license_is_apache_2_0() -> None:
    text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert "Apache License" in text


def test_role_directory_exists() -> None:
    # This leg's role, per the assembly root's project.yaml (`legs[].role:
    # spec`), is `requirements/`. project.yaml itself lives in the assembly
    # root (opensoft/openXdox), not in this leg.
    assert (ROOT / "requirements").is_dir()


def test_openspec_instance_exists() -> None:
    assert (ROOT / "openspec").is_dir()
    assert (ROOT / "openspec" / "specs").is_dir()
    assert (ROOT / "openspec" / "changes").is_dir()


def test_openspec_validate_all_strict() -> None:
    openspec = shutil.which("openspec")
    if openspec is None:
        pytest.skip("openspec CLI is not on PATH in this environment")
    env = dict(os.environ)
    env["OPENSPEC_TELEMETRY"] = "0"
    proc = subprocess.run(
        [openspec, "validate", "--all", "--strict"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )
    assert proc.returncode == 0, (
        f"openspec validate --all --strict exited {proc.returncode}\n"
        f"stdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
    )


def test_branch_protection_evidence_exists() -> None:
    # tasks.md § 1.5's evidence line: a ruleset is a repository SETTING, so
    # the only thing a tree can assert is that the evidence file naming it is
    # present. Levelled across all six repositories by the OQ-O pass
    # (openxFactory#656).
    assert (ROOT / "docs" / "branch-protection.md").is_file()


def test_openspec_project_md_exists() -> None:
    # The instance's own conventions file. openXdox-spec had no
    # openspec/project.md until the OQ-O levelling pass (openxFactory#656);
    # this test is what keeps both spec legs level from here on.
    assert (ROOT / "openspec" / "project.md").is_file()
