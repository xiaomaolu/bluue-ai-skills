#!/usr/bin/env python3
"""Validate every top-level Codex skill in this repository."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install it with: python -m pip install -r requirements-validation.txt")
    raise SystemExit(2)


ALLOWED_FRONTMATTER_KEYS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
}
MAX_SKILL_NAME_LENGTH = 64


def validate_skill(skill_path: Path) -> tuple[bool, str]:
    """Apply the Codex quick-validation rules plus repository invariants."""

    skill_md = skill_path / "SKILL.md"
    if not skill_md.is_file():
        return False, "SKILL.md not found"

    try:
        content = skill_md.read_text(encoding="utf-8").replace("\r\n", "\n")
    except (OSError, UnicodeError) as exc:
        return False, f"Cannot read SKILL.md as UTF-8: {exc}"

    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
    if not match:
        return False, "Invalid or missing YAML frontmatter"

    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return False, f"Invalid YAML in frontmatter: {exc}"

    if not isinstance(frontmatter, dict):
        return False, "Frontmatter must be a YAML dictionary"

    unexpected_keys = set(frontmatter) - ALLOWED_FRONTMATTER_KEYS
    if unexpected_keys:
        unexpected = ", ".join(sorted(unexpected_keys))
        allowed = ", ".join(sorted(ALLOWED_FRONTMATTER_KEYS))
        return False, f"Unexpected frontmatter key(s): {unexpected}. Allowed: {allowed}"

    name = frontmatter.get("name")
    if not isinstance(name, str) or not name.strip():
        return False, "Frontmatter 'name' must be a non-empty string"
    name = name.strip()

    if not re.fullmatch(r"[a-z0-9-]+", name):
        return False, f"Name '{name}' must use lowercase letters, digits, and hyphens only"
    if name.startswith("-") or name.endswith("-") or "--" in name:
        return False, f"Name '{name}' cannot start/end with a hyphen or contain consecutive hyphens"
    if len(name) > MAX_SKILL_NAME_LENGTH:
        return False, f"Name is {len(name)} characters; maximum is {MAX_SKILL_NAME_LENGTH}"
    if name != skill_path.name:
        return False, f"Frontmatter name '{name}' must match directory '{skill_path.name}'"

    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        return False, "Frontmatter 'description' must be a non-empty string"
    description = description.strip()

    if description.startswith("[TODO:"):
        return False, "Description contains an unfinished TODO placeholder"
    if "<" in description or ">" in description:
        return False, "Description cannot contain angle brackets"
    if len(description) > 1024:
        return False, f"Description is {len(description)} characters; maximum is 1024"

    body = content[match.end() :]
    fence_marker: str | None = None
    fence_length = 0

    for line in body.splitlines():
        fence = re.match(r"^[ \t]*(?:(?:[-+*]|\d+[.)])[ \t]+)?(`{3,}|~{3,})(.*)$", line)
        if fence:
            marker = fence.group(1)
            if fence_marker is None:
                fence_marker = marker[0]
                fence_length = len(marker)
            elif marker[0] == fence_marker and len(marker) >= fence_length and not fence.group(2).strip():
                fence_marker = None
                fence_length = 0
            continue

        if fence_marker is None and re.fullmatch(r"[ ]{0,3}\[TODO:[^\n]*\][ \t]*", line):
            return False, "Skill instructions contain an unfinished TODO placeholder"

    return True, "Skill is valid"


def discover_skills(root: Path) -> list[Path]:
    return sorted(path.parent for path in root.glob("*/SKILL.md") if path.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        default=Path(__file__).resolve().parents[1],
        type=Path,
        help="Repository root (defaults to the parent of scripts/)",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    skills = discover_skills(root)

    if not skills:
        print(f"No top-level skills found under {root}")
        return 1

    failures = 0
    for skill in skills:
        valid, message = validate_skill(skill)
        status = "PASS" if valid else "FAIL"
        print(f"[{status}] {skill.name}: {message}")
        failures += 0 if valid else 1

    if failures:
        print(f"Validation failed for {failures} of {len(skills)} skill(s).")
        return 1

    print(f"Validated {len(skills)} skill(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
