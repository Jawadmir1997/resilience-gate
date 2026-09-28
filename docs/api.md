# ResilienceGate Module Interface Reference

This document describes the planned interfaces between the major ResilienceGate prototype modules.

The interfaces are part of an early-stage prototype and may change as implementation and testing progress.

## Shared Data Models

`src/resilience_gate/models.py`

Shared structures provide a consistent representation for:

- telemetry metric points
- detected anomalies
- dependency vulnerability findings
- deployment gate decisions
- severity levels
- ALLOW / WARN / BLOCK decisions

## Telemetry Ingestion

`src/resilience_gate/telemetry/ingest.py`

Planned interfaces:

### `load_json(path)`

Loads telemetry records from a JSON file and returns normalized metric points.

### `load_csv(path)`

Loads telemetry records from a CSV file and returns normalized metric points.

### `normalize(raw)`

Converts one raw telemetry record into the internal `MetricPoint` representation.

## Synthetic Telemetry Generation

`src/resilience_gate/telemetry/generate.py`

Planned interfaces:

### `generate_normal(service, count)`

Generates synthetic stable telemetry for prototype demonstrations and testing.

### `generate_incident(service, count)`

Generates synthetic telemetry containing a simulated operational incident.

No real employer or production telemetry is required for these demonstrations.

## Baseline Anomaly Detection

`src/resilience_gate/detection/baseline.py`

Planned interfaces:

### `calculate_baseline(points)`

Calculates baseline statistics from normalized telemetry.

### `detect_anomalies(points, baseline)`

Evaluates telemetry against an established baseline and returns detected anomalies.

## Software Bill of Materials

`src/resilience_gate/supplychain/sbom.py`

Planned interfaces:

### `load_sbom(path)`

Loads dependency information from a CycloneDX SBOM.

### `normalize_components(components)`

Normalizes SBOM components into package and version pairs.

## Vulnerability Analysis

`src/resilience_gate/supplychain/osv.py`

Planned interfaces:

### `check_dependency(package, version)`

Evaluates one declared dependency for known vulnerability findings.

### `check_dependencies(dependencies)`

Evaluates multiple dependencies and returns combined findings.

## Policy Engine

`src/resilience_gate/policy/engine.py`

Planned interface:

### `evaluate_policy(anomalies, findings, policy)`

Combines operational anomalies, software supply-chain findings, and configured policy rules to produce a `GateDecision`.

Possible decisions are:

- `ALLOW`
- `WARN`
- `BLOCK`

## Explainability

`src/resilience_gate/explain/narrate.py`

Planned interface:

### `narrate_decision(decision)`

Produces a human-readable explanation of a deployment gate decision.

## HTML Reporting

`src/resilience_gate/report/html.py`

Planned interfaces:

### `render_html(decision)`

Renders a gate decision as an HTML document.

### `save_html(decision, path)`

Saves the rendered HTML report to local storage.

## Command-Line Interface

`src/resilience_gate/cli.py`

The planned command-line interface provides an entry point for running the prototype against telemetry and policy inputs.

Example planned usage:

```text
resilience-gate --metrics sample_data/metrics_incident.json --policy policy.yaml
```

## Current Implementation Status

These interfaces currently document the intended prototype boundaries. Several modules remain scaffolds and are not yet represented as fully implemented or production-ready.

Implementation status is maintained in the repository `README.md`.
