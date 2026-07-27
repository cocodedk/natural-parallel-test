#!/usr/bin/env python3
"""Validate the natural-parallel-test plugin repository.

Checks manifest correctness, frontmatter parseability, and the editorial rules
the framework depends on — chiefly that every analogue-library entry states
where it stops being valid.

Run from the repository root:  python3 scripts/validate-plugin.py
Exit code 0 = clean, 1 = errors found.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required:  pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "npt"
SKILL_DIR = PLUGIN / "skills" / "natural-parallel-test"
REFERENCES = SKILL_DIR / "references"
LIBRARY = REFERENCES / "03-analogue-library.md"

# `fable` is deliberate — the auditor must not run on the model that generated
# the candidate. It is not in the documented set, so it is allowed but noted.
DOCUMENTED_MODELS = {"sonnet", "opus", "haiku", "inherit"}
ALLOWED_MODELS = DOCUMENTED_MODELS | {"fable"}

errors: list[str] = []
warnings: list[str] = []


def error(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def split_frontmatter(path: Path) -> dict | None:
    """Return parsed frontmatter, or None if it is missing or unparseable."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        error(f"{rel(path)}: no YAML frontmatter block")
        return None
    end = text.find("\n---", 3)
    if end == -1:
        error(f"{rel(path)}: frontmatter block is not terminated")
        return None
    raw = text[4:end]
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        # This is the failure mode that bit us: an unquoted `[a] [b]` value is
        # two juxtaposed flow sequences, and the runtime drops the whole block
        # silently rather than complaining.
        error(f"{rel(path)}: frontmatter does not parse as YAML — {exc}")
        return None
    if not isinstance(data, dict):
        error(f"{rel(path)}: frontmatter is not a mapping")
        return None
    return data


def check_manifests() -> None:
    plugin_manifest = PLUGIN / ".claude-plugin" / "plugin.json"
    marketplace_manifest = ROOT / ".claude-plugin" / "marketplace.json"

    if not plugin_manifest.is_file():
        error(f"missing {rel(plugin_manifest)}")
        return
    if not marketplace_manifest.is_file():
        error(f"missing {rel(marketplace_manifest)}")
        return

    try:
        plugin = json.loads(plugin_manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        error(f"{rel(plugin_manifest)}: invalid JSON — {exc}")
        return
    try:
        market = json.loads(marketplace_manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        error(f"{rel(marketplace_manifest)}: invalid JSON — {exc}")
        return

    if "name" not in plugin:
        error(f"{rel(plugin_manifest)}: 'name' is required")
    for field in ("version", "description", "author", "license"):
        if field not in plugin:
            warn(f"{rel(plugin_manifest)}: '{field}' is absent")

    for field in ("name", "owner", "plugins"):
        if field not in market:
            error(f"{rel(marketplace_manifest)}: '{field}' is required")

    for entry in market.get("plugins", []):
        source = entry.get("source")
        if not isinstance(source, str):
            continue  # remote sources are not resolvable here
        target = (ROOT / source).resolve()
        if not (target / ".claude-plugin" / "plugin.json").is_file():
            error(
                f"{rel(marketplace_manifest)}: source '{source}' has no "
                ".claude-plugin/plugin.json"
            )
        entry_version = entry.get("version")
        if entry_version and entry_version != plugin.get("version"):
            error(
                f"marketplace entry version {entry_version!r} disagrees with "
                f"plugin.json version {plugin.get('version')!r}"
            )


def check_commands() -> None:
    command_dir = PLUGIN / "commands"
    files = sorted(command_dir.glob("*.md"))
    if not files:
        error(f"{rel(command_dir)}: no commands found")
    for path in files:
        data = split_frontmatter(path)
        if data is None:
            continue
        if not data.get("description"):
            error(f"{rel(path)}: 'description' is required")


def check_agents() -> None:
    agent_dir = PLUGIN / "agents"
    files = sorted(agent_dir.glob("*.md"))
    if not files:
        error(f"{rel(agent_dir)}: no agents found")
    for path in files:
        data = split_frontmatter(path)
        if data is None:
            continue
        for field in ("name", "description"):
            if not data.get(field):
                error(f"{rel(path)}: '{field}' is required")
        if data.get("name") and data["name"] != path.stem:
            error(f"{rel(path)}: name {data['name']!r} != filename {path.stem!r}")
        model = data.get("model")
        if model is not None:
            if model not in ALLOWED_MODELS:
                error(
                    f"{rel(path)}: model {model!r} is not recognised "
                    f"(allowed: {sorted(ALLOWED_MODELS)})"
                )
            elif model not in DOCUMENTED_MODELS:
                # Verified resolving on Claude Code 2.1.220, but `claude plugin
                # validate` does not check this field at all — so if it ever
                # stops resolving, it fails silently at runtime, not here.
                warn(
                    f"{rel(path)}: model {model!r} is intentional and verified "
                    "working, but is outside the documented set — re-check it "
                    "after a Claude Code upgrade"
                )


def check_skill() -> None:
    skill = SKILL_DIR / "SKILL.md"
    if not skill.is_file():
        error(f"missing {rel(skill)}")
        return
    data = split_frontmatter(skill)
    if data is not None:
        for field in ("name", "description"):
            if not data.get(field):
                error(f"{rel(skill)}: '{field}' is required")

    # Every references/... link in any skill markdown file must resolve.
    pattern = re.compile(r"\]\((?:references/)?(\d\d-[a-z0-9-]+\.md)\)")
    sources = [skill] + sorted(REFERENCES.glob("*.md"))
    for source in sources:
        text = source.read_text(encoding="utf-8")
        for name in set(pattern.findall(text)):
            if not (REFERENCES / name).is_file():
                error(f"{rel(source)}: link to missing reference '{name}'")


def check_library_limits() -> None:
    """Every analogue entry must say where it stops being valid.

    This is the framework's own rule: an entry quoted without its limit has
    been misused, so an entry shipped without one is a defect.
    """
    if not LIBRARY.is_file():
        error(f"missing {rel(LIBRARY)}")
        return

    text = LIBRARY.read_text(encoding="utf-8")
    # Entries are '### E-NN · Name'; split on them and keep each entry's body.
    parts = re.split(r"^### (E-\d+)[^\n]*$", text, flags=re.MULTILINE)
    if len(parts) < 3:
        error(f"{rel(LIBRARY)}: no 'E-NN' entries found")
        return

    ids = parts[1::2]
    bodies = parts[2::2]
    for entry_id, body in zip(ids, bodies):
        lowered = body.lower()
        if "stops being valid when" not in lowered:
            error(
                f"{rel(LIBRARY)}: entry {entry_id} has no "
                "'Stops being valid when' line"
            )
        for required in ("problem solved", "mechanism", "transferable principle"):
            if required not in lowered:
                error(f"{rel(LIBRARY)}: entry {entry_id} has no '{required}' line")

    seen = [i for i in ids]
    if len(seen) != len(set(seen)):
        duplicates = sorted({i for i in seen if seen.count(i) > 1})
        error(f"{rel(LIBRARY)}: duplicate entry ids {duplicates}")

    # The routing table must not point at entries that do not exist.
    referenced = set(re.findall(r"E-\d+", text.split("# Level 1")[0]))
    missing = sorted(referenced - set(ids))
    if missing:
        error(f"{rel(LIBRARY)}: routing table references missing entries {missing}")


def check_placeholders() -> None:
    """No template placeholders may reach a commit."""
    needles = ("<OWNER>", "[owner]", "[repo]", "[ProjectName]")
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git/" in str(path):
            continue
        if path.suffix not in {".md", ".json", ".yml", ".yaml", ".sh", ".html", ".txt"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for needle in needles:
            if needle in text:
                error(f"{rel(path)}: unsubstituted placeholder {needle!r}")


def main() -> int:
    check_manifests()
    check_commands()
    check_agents()
    check_skill()
    check_library_limits()
    check_placeholders()

    for message in warnings:
        print(f"warning: {message}")
    for message in errors:
        print(f"error: {message}", file=sys.stderr)

    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"\nvalidation passed ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
