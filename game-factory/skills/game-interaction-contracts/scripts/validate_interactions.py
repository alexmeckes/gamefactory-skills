#!/usr/bin/env python3
"""Validate game interaction contracts, flows, bindings, and indexes."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import deque
from pathlib import Path
from typing import Any


ID_RE = re.compile(r"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)+$")
FLOW_NODE_TYPES = {"entry", "interaction", "decision", "wait", "prompt", "exit"}
FLOW_EDGE_EVENTS = {
    "entered",
    "succeeded",
    "failed",
    "blocked",
    "cancelled",
    "interrupted",
    "invalidated",
    "timed_out",
}
FLOW_EDGE_PREFIXES = ("choice.", "event.", "condition.", "prompt.")
SUPPORTED_SUFFIXES = (
    ".interaction.yaml",
    ".interaction.yml",
    ".interaction.json",
    ".flow.yaml",
    ".flow.yml",
    ".flow.json",
    ".binding.yaml",
    ".binding.yml",
    ".binding.json",
    "interaction-index.yaml",
    "interaction-index.yml",
    "interaction-index.json",
)


def discover(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(
        candidate
        for candidate in path.rglob("*")
        if candidate.is_file() and candidate.name.endswith(SUPPORTED_SUFFIXES)
    )


def load_record(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        data = json.loads(text)
    else:
        try:
            import yaml  # type: ignore
        except ImportError as exc:
            raise RuntimeError(
                "YAML validation requires PyYAML. Use JSON records or install PyYAML."
            ) from exc
        data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise ValueError("top-level value must be an object")
    return data


def require(record: dict[str, Any], keys: list[str], errors: list[str]) -> None:
    for key in keys:
        if key not in record or record[key] in (None, "", [], {}):
            errors.append(f"missing or empty required field: {key}")


def validate_id(value: Any, label: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not ID_RE.fullmatch(value):
        errors.append(f"{label} must be a namespaced lowercase ID: {value!r}")


def object_ids(items: Any, label: str, errors: list[str]) -> list[str]:
    if not isinstance(items, list):
        errors.append(f"{label} must be a list")
        return []
    values: list[str] = []
    for index, item in enumerate(items):
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            errors.append(f"{label}[{index}] must be an object with an id")
            continue
        values.append(item["id"])
    duplicates = sorted({item for item in values if values.count(item) > 1})
    for duplicate in duplicates:
        errors.append(f"duplicate {label} id: {duplicate}")
    return values


def validate_acceptance(record: dict[str, Any], errors: list[str], strict: bool) -> None:
    cases = record.get("acceptance")
    ids = object_ids(cases, "acceptance", errors)
    if strict and len(ids) < 2:
        errors.append("strict mode requires at least two acceptance scenarios")
    if isinstance(cases, list):
        for index, case in enumerate(cases):
            if not isinstance(case, dict):
                continue
            for key in ("given", "when", "then"):
                if not case.get(key):
                    errors.append(f"acceptance[{index}] missing {key}")


def acceptance_coverage(record: dict[str, Any]) -> set[str]:
    coverage: set[str] = set()
    cases = record.get("acceptance", [])
    if isinstance(cases, list):
        for case in cases:
            if not isinstance(case, dict):
                continue
            values = case.get("covers", [])
            if isinstance(values, list):
                coverage.update(value for value in values if isinstance(value, str))
    return coverage


def validate_interaction(record: dict[str, Any], errors: list[str], strict: bool) -> None:
    require(
        record,
        [
            "schema_version",
            "kind",
            "id",
            "version",
            "status",
            "maturity",
            "intent",
            "participants",
            "trigger",
            "states",
            "transitions",
            "failure",
            "feedback",
            "acceptance",
        ],
        errors,
    )
    validate_id(record.get("id"), "id", errors)
    if not isinstance(record.get("participants"), dict) or not record.get("participants"):
        errors.append("participants must be a non-empty role mapping")

    states = record.get("states")
    state_ids = object_ids(states, "states", errors)
    state_set = set(state_ids)
    initial = []
    terminal = []
    if isinstance(states, list):
        initial = [state.get("id") for state in states if isinstance(state, dict) and state.get("initial")]
        terminal = [state.get("id") for state in states if isinstance(state, dict) and state.get("terminal")]
    if len(initial) != 1:
        errors.append(f"exactly one initial state is required; found {len(initial)}")
    if not terminal:
        errors.append("at least one terminal state is required")

    transitions = record.get("transitions")
    object_ids(transitions, "transitions", errors)
    adjacency: dict[str, list[str]] = {state: [] for state in state_ids}
    if isinstance(transitions, list):
        for index, transition in enumerate(transitions):
            if not isinstance(transition, dict):
                continue
            for key in ("from", "to", "event"):
                if not transition.get(key):
                    errors.append(f"transitions[{index}] missing {key}")
            source, target = transition.get("from"), transition.get("to")
            if source not in state_set:
                errors.append(f"transitions[{index}] references unknown from state: {source}")
            if target not in state_set:
                errors.append(f"transitions[{index}] references unknown to state: {target}")
            if source in adjacency and target in state_set:
                adjacency[source].append(target)
            if transition.get("interruptible") and not transition.get("cancel_to"):
                errors.append(f"transitions[{index}] is interruptible but has no cancel_to")
            cancel_to = transition.get("cancel_to")
            if cancel_to and cancel_to not in state_set:
                errors.append(f"transitions[{index}] references unknown cancel_to state: {cancel_to}")
            elif source in adjacency and cancel_to in state_set:
                adjacency[source].append(cancel_to)

    if len(initial) == 1:
        reached = {initial[0]}
        queue = deque([initial[0]])
        while queue:
            source = queue.popleft()
            for target in adjacency.get(source, []):
                if target not in reached:
                    reached.add(target)
                    queue.append(target)
        for state in sorted(state_set - reached):
            errors.append(f"state is unreachable from initial state: {state}")

    validate_acceptance(record, errors, strict)
    if strict:
        require(record, ["bindings_required", "persistence", "network", "accessibility"], errors)
        if record.get("maturity") == "concept":
            errors.append("strict mode does not accept concept maturity")
        coverage = acceptance_coverage(record)
        if isinstance(transitions, list):
            for transition in transitions:
                if not isinstance(transition, dict) or not transition.get("id"):
                    continue
                label = f"transition.{transition['id']}"
                if label not in coverage:
                    errors.append(f"acceptance does not cover {label}")
                if transition.get("interruptible") and f"{label}.cancel" not in coverage:
                    errors.append(f"acceptance does not cover {label}.cancel")
        failure_cases = record.get("failure", {}).get("cases", []) if isinstance(record.get("failure"), dict) else []
        if isinstance(failure_cases, list):
            for case in failure_cases:
                if isinstance(case, dict) and case.get("id"):
                    label = f"failure.{case['id']}"
                    if label not in coverage:
                        errors.append(f"acceptance does not cover {label}")
        persistence = record.get("persistence")
        if isinstance(persistence, dict) and persistence.get("save_policy") != "none":
            for key in ("schema_version", "saved_fields", "resume_policy", "load_conflicts", "migration_policy"):
                if key not in persistence:
                    errors.append(f"persistence missing {key}")
            if "persistence.save-load" not in coverage:
                errors.append("acceptance does not cover persistence.save-load")


def validate_flow(record: dict[str, Any], errors: list[str], strict: bool) -> set[str]:
    require(record, ["schema_version", "kind", "id", "version", "status", "maturity", "intent", "nodes", "edges", "acceptance"], errors)
    validate_id(record.get("id"), "id", errors)
    node_ids = object_ids(record.get("nodes"), "nodes", errors)
    node_set = set(node_ids)
    refs: set[str] = set()
    entries = 0
    exits = 0
    if isinstance(record.get("nodes"), list):
        for index, node in enumerate(record["nodes"]):
            if not isinstance(node, dict):
                continue
            node_type = node.get("type")
            if node_type not in FLOW_NODE_TYPES:
                errors.append(f"nodes[{index}] has unsupported type: {node_type!r}")
            entries += node_type == "entry"
            exits += node_type == "exit"
            if node_type == "interaction":
                interaction_id = node.get("interaction_id")
                validate_id(interaction_id, f"nodes[{index}].interaction_id", errors)
                if isinstance(interaction_id, str):
                    refs.add(interaction_id)
            elif node_type == "decision" and not node.get("decision_id"):
                errors.append(f"nodes[{index}] decision missing decision_id")
            elif node_type == "wait" and not (node.get("wait_for") or node.get("duration_ms") is not None):
                errors.append(f"nodes[{index}] wait missing wait_for or duration_ms")
            elif node_type == "prompt" and not node.get("prompt_id"):
                errors.append(f"nodes[{index}] prompt missing prompt_id")
            elif node_type == "exit" and not node.get("outcome"):
                errors.append(f"nodes[{index}] exit missing outcome")
    if entries != 1:
        errors.append(f"exactly one entry node is required; found {entries}")
    if exits < 1:
        errors.append("at least one exit node is required")
    object_ids(record.get("edges"), "edges", errors)
    if isinstance(record.get("edges"), list):
        for index, edge in enumerate(record["edges"]):
            if not isinstance(edge, dict):
                continue
            for key in ("from", "to", "on"):
                if not edge.get(key):
                    errors.append(f"edges[{index}] missing {key}")
            event = edge.get("on")
            if isinstance(event, str) and event not in FLOW_EDGE_EVENTS and not event.startswith(FLOW_EDGE_PREFIXES):
                errors.append(f"edges[{index}] has unsupported event vocabulary: {event}")
            for key in ("from", "to"):
                if edge.get(key) not in node_set:
                    errors.append(f"edges[{index}] references unknown {key} node: {edge.get(key)}")
    validate_acceptance(record, errors, strict)
    if strict:
        coverage = acceptance_coverage(record)
        for edge in record.get("edges", []):
            if isinstance(edge, dict) and edge.get("id"):
                label = f"edge.{edge['id']}"
                if label not in coverage:
                    errors.append(f"acceptance does not cover {label}")
    return refs


def validate_binding(record: dict[str, Any], errors: list[str], strict: bool) -> str | None:
    require(record, ["schema_version", "kind", "id", "version", "status", "contract_id", "contract_version", "context", "role_bindings", "hook_bindings"], errors)
    validate_id(record.get("id"), "id", errors)
    validate_id(record.get("contract_id"), "contract_id", errors)
    if strict:
        require(record, ["validation"], errors)
    return record.get("contract_id") if isinstance(record.get("contract_id"), str) else None


def validate_index(record: dict[str, Any], errors: list[str]) -> set[str]:
    require(record, ["schema_version", "kind"], errors)
    refs: set[str] = set()
    for section in ("interactions", "flows", "bindings"):
        items = record.get(section, [])
        if not isinstance(items, list):
            errors.append(f"{section} must be a list")
            continue
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                errors.append(f"{section}[{index}] must be an object")
                continue
            validate_id(item.get("id"), f"{section}[{index}].id", errors)
            if not item.get("path"):
                errors.append(f"{section}[{index}] missing path")
            if isinstance(item.get("id"), str):
                refs.add(item["id"])
    return refs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Interaction file or directory")
    parser.add_argument("--strict", action="store_true", help="Require implementation-handoff fields")
    args = parser.parse_args()

    files = discover(args.path)
    if not files:
        print(f"No interaction records found under {args.path}", file=sys.stderr)
        return 2

    records: list[tuple[Path, dict[str, Any]]] = []
    problems: dict[Path, list[str]] = {}
    for path in files:
        try:
            records.append((path, load_record(path)))
        except (OSError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
            problems.setdefault(path, []).append(str(exc))

    ids: dict[str, Path] = {}
    interaction_ids: set[str] = set()
    interaction_records: dict[str, dict[str, Any]] = {}
    flow_refs: list[tuple[Path, str]] = []
    binding_refs: list[tuple[Path, str]] = []
    binding_records: list[tuple[Path, dict[str, Any]]] = []
    index_refs: list[tuple[Path, str]] = []

    for path, record in records:
        errors = problems.setdefault(path, [])
        kind = record.get("kind")
        record_id = record.get("id")
        if isinstance(record_id, str):
            if record_id in ids:
                errors.append(f"duplicate record id also found in {ids[record_id]}")
            else:
                ids[record_id] = path
        if kind == "interaction":
            validate_interaction(record, errors, args.strict)
            if isinstance(record_id, str):
                interaction_ids.add(record_id)
                interaction_records[record_id] = record
        elif kind == "interaction_flow":
            for ref in validate_flow(record, errors, args.strict):
                flow_refs.append((path, ref))
        elif kind == "interaction_binding":
            ref = validate_binding(record, errors, args.strict)
            if ref:
                binding_refs.append((path, ref))
                binding_records.append((path, record))
        elif kind == "interaction_index":
            for ref in validate_index(record, errors):
                index_refs.append((path, ref))
        else:
            errors.append(f"unsupported kind: {kind!r}")

    for path, ref in flow_refs + binding_refs:
        if ref not in interaction_ids:
            problems[path].append(f"unresolved interaction reference: {ref}")
    if args.strict:
        for path, binding in binding_records:
            contract_id = binding.get("contract_id")
            contract = interaction_records.get(contract_id)
            if not contract:
                continue
            if binding.get("contract_version") != contract.get("version"):
                problems[path].append(
                    f"contract_version {binding.get('contract_version')!r} does not match "
                    f"loaded contract version {contract.get('version')!r}"
                )
            participants = contract.get("participants", {})
            role_bindings = binding.get("role_bindings", {})
            if isinstance(participants, dict) and isinstance(role_bindings, dict):
                required_roles = {
                    role
                    for role, spec in participants.items()
                    if not isinstance(spec, dict) or not spec.get("optional", False)
                }
                for role in sorted(required_roles - set(role_bindings)):
                    problems[path].append(f"binding missing required participant role: {role}")
            required_hooks = contract.get("bindings_required", {})
            hook_bindings = binding.get("hook_bindings", {})
            if isinstance(required_hooks, dict) and isinstance(hook_bindings, dict):
                for group, required in required_hooks.items():
                    if not isinstance(required, list):
                        continue
                    binding_group = group.removesuffix("_hooks")
                    provided = hook_bindings.get(binding_group, {})
                    if isinstance(provided, dict):
                        provided_names = set(provided)
                    elif isinstance(provided, list):
                        provided_names = {value for value in provided if isinstance(value, str)}
                    else:
                        provided_names = set()
                    for hook in sorted(set(required) - provided_names):
                        problems[path].append(
                            f"binding missing required {binding_group} hook: {hook}"
                        )
    for path, ref in index_refs:
        if ref not in ids:
            problems[path].append(f"index references an unloaded record: {ref}")

    failures = {path: errors for path, errors in problems.items() if errors}
    if failures:
        for path, errors in failures.items():
            for error in errors:
                print(f"{path}: {error}", file=sys.stderr)
        print(f"Validation failed: {sum(map(len, failures.values()))} issue(s) in {len(failures)} file(s).", file=sys.stderr)
        return 1

    print(f"Validated {len(records)} interaction record(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
