#!/usr/bin/env python3
"""Perform structural checks on Markdown game design specifications."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


PRODUCTION_FILES = {
    "GAME_DESIGN.md": [
        "one-sentence concept",
        "player fantasy",
        "audience",
        "design pillars",
        "non-goals",
        "document map",
        "scope",
    ],
    "CORE_LOOP.md": ["loop hierarchy", "progression", "difficulty", "acceptance criteria"],
    "SYSTEMS.md": ["system map", "requirements", "tuning", "cross-system rules"],
    "CONTENT_PLAN.md": ["content principles", "budget", "progression placement", "cut"],
    "UX_FLOW.md": ["input model", "screen", "onboarding", "accessibility", "acceptance criteria"],
    "PRODUCTION_SCOPE.md": ["constraints", "milestone scope", "performance", "risks", "exit criteria", "cut"],
    "DECISIONS.md": ["active assumptions", "decision record", "resolved index"],
}

MODE_HEADINGS = {
    "concept": [
        "one-sentence concept",
        "player fantasy",
        "audience",
        "design pillars",
        "non-goals",
        "core loop",
        "scope",
        "assumptions",
    ],
    "prototype": [
        "prototype question",
        "hypothesis",
        "test loop",
        "prototype systems",
        "instrumentation",
        "success",
        "scope",
        "assumptions",
    ],
    "vertical-slice": [
        "slice promise",
        "audience",
        "design pillars",
        "core and slice loops",
        "system requirements",
        "content",
        "ux",
        "cross-discipline acceptance",
        "scope",
        "risks",
        "exit criteria",
    ],
}

PLACEHOLDER_RE = re.compile(r"\{\{[^{}\n]+\}\}")
LOOSE_PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|TK)\b", re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


@dataclass(frozen=True)
class Issue:
    severity: str
    path: Path
    line: int | None
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="Markdown spec file or production-spec directory")
    parser.add_argument(
        "--mode",
        choices=("auto", "concept", "prototype", "vertical-slice", "production"),
        default="auto",
        help="Specification depth; inferred by default",
    )
    parser.add_argument("--strict", action="store_true", help="Return failure when warnings are present")
    return parser.parse_args()


def markdown_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target] if target.suffix.lower() == ".md" else []
    if target.is_dir():
        return sorted(path for path in target.glob("*.md") if path.is_file())
    return []


def infer_mode(target: Path, files: list[Path], texts: dict[Path, str]) -> str:
    names = {path.name for path in files}
    if set(PRODUCTION_FILES).issubset(names):
        return "production"

    combined = "\n".join(texts.values()).lower()
    label = f"{target.name.lower()}\n{combined[:1000]}"
    if "vertical slice" in label or "vertical-slice" in label:
        return "vertical-slice"
    if "prototype" in label:
        return "prototype"
    return "concept"


def headings(text: str) -> list[tuple[int, int, str]]:
    result: list[tuple[int, int, str]] = []
    for line_no, line in enumerate(text.splitlines(), 1):
        match = HEADING_RE.match(line)
        if match:
            title = re.sub(r"[`*_]", "", match.group(2)).strip().lower()
            result.append((line_no, len(match.group(1)), title))
    return result


def has_heading(actual: list[tuple[int, int, str]], expected: str) -> bool:
    return any(expected in title for _, _, title in actual)


def check_required_headings(path: Path, text: str, expected: list[str]) -> list[Issue]:
    actual = headings(text)
    return [
        Issue("ERROR", path, None, f"missing section heading containing '{name}'")
        for name in expected
        if not has_heading(actual, name)
    ]


def check_empty_sections(path: Path, text: str) -> list[Issue]:
    lines = text.splitlines()
    found = headings(text)
    issues: list[Issue] = []
    for index, (line_no, level, title) in enumerate(found):
        end_line = len(lines)
        for next_line, next_level, _ in found[index + 1 :]:
            if next_level <= level:
                end_line = next_line - 1
                break
        body = [line.strip() for line in lines[line_no:end_line] if line.strip()]
        if not body:
            issues.append(Issue("WARNING", path, line_no, f"section '{title}' has no content"))
    return issues


def check_placeholders(path: Path, text: str) -> list[Issue]:
    issues: list[Issue] = []
    for line_no, line in enumerate(text.splitlines(), 1):
        placeholders = PLACEHOLDER_RE.findall(line)
        if placeholders:
            preview = ", ".join(placeholders[:3])
            issues.append(Issue("ERROR", path, line_no, f"unfilled template placeholder: {preview}"))
        if LOOSE_PLACEHOLDER_RE.search(line):
            issues.append(Issue("WARNING", path, line_no, "loose TODO/TBD/TK marker; move uncertainty to the decision log"))
    return issues


def check_quality_terms(path: Path, text: str, mode: str) -> list[Issue]:
    lowered = text.lower()
    issues: list[Issue] = []
    if mode != "concept" and "acceptance" not in lowered:
        issues.append(Issue("WARNING", path, None, "no acceptance criteria language found"))
    if mode in {"vertical-slice", "production"} and "edge case" not in lowered:
        issues.append(Issue("WARNING", path, None, "no edge-case coverage found"))
    if mode in {"vertical-slice", "production"} and "failure" not in lowered:
        issues.append(Issue("WARNING", path, None, "no failure or recovery coverage found"))
    if "initial tuning" not in lowered and mode != "concept":
        issues.append(Issue("WARNING", path, None, "no initial-tuning label found; avoid presenting untested values as final"))
    return issues


def validate(target: Path, mode: str) -> tuple[str, list[Issue]]:
    files = markdown_files(target)
    if not files:
        return mode, [Issue("ERROR", target, None, "no Markdown specification files found")]

    texts: dict[Path, str] = {}
    issues: list[Issue] = []
    for path in files:
        try:
            texts[path] = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            issues.append(Issue("ERROR", path, None, f"could not read UTF-8 Markdown: {exc}"))

    selected = infer_mode(target, files, texts) if mode == "auto" else mode

    for path, text in texts.items():
        issues.extend(check_placeholders(path, text))
        issues.extend(check_empty_sections(path, text))

    if selected == "production":
        by_name = {path.name: path for path in files}
        for name, expected in PRODUCTION_FILES.items():
            if name not in by_name:
                issues.append(Issue("ERROR", target, None, f"missing production document '{name}'"))
                continue
            path = by_name[name]
            issues.extend(check_required_headings(path, texts[path], expected))

        combined = "\n".join(texts.values())
        synthetic_path = target if target.is_dir() else files[0]
        issues.extend(check_quality_terms(synthetic_path, combined, selected))
    else:
        if len(files) > 1:
            issues.append(Issue("WARNING", target, None, f"{selected} mode usually uses one canonical Markdown document"))
        primary = files[0]
        issues.extend(check_required_headings(primary, texts[primary], MODE_HEADINGS[selected]))
        issues.extend(check_quality_terms(primary, texts[primary], selected))

    return selected, issues


def display_path(path: Path, target: Path) -> str:
    try:
        base = target if target.is_dir() else target.parent
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def main() -> int:
    args = parse_args()
    selected, issues = validate(args.target, args.mode)
    errors = [issue for issue in issues if issue.severity == "ERROR"]
    warnings = [issue for issue in issues if issue.severity == "WARNING"]

    print(f"Mode: {selected}")
    for issue in sorted(issues, key=lambda item: (str(item.path), item.line or 0, item.severity)):
        location = display_path(issue.path, args.target)
        if issue.line is not None:
            location = f"{location}:{issue.line}"
        print(f"{issue.severity}: {location}: {issue.message}")

    print(f"Result: {len(errors)} error(s), {len(warnings)} warning(s)")
    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
