"""End-to-end tests for the ResilienceGate CLI."""

from pathlib import Path

from resilience_gate.cli import run_gate


def test_incident_telemetry_blocks_deployment():
    """Incident telemetry should produce a blocking deployment decision."""
    root = Path(__file__).resolve().parents[1]

    baseline = root / "sample_data" / "metrics_normal.json"
    incident = root / "sample_data" / "metrics_incident.json"

    exit_code = run_gate(
        baseline_path=str(baseline),
        current_path=str(incident),
    )

    assert exit_code == 2
