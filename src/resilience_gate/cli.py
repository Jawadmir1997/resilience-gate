"""Command-line interface for the ResilienceGate prototype."""

import argparse

from resilience_gate.detection.baseline import build_baseline, detect_anomalies
from resilience_gate.explain.narrate import narrate
from resilience_gate.policy.engine import evaluate
from resilience_gate.telemetry.ingest import load_json


def run_gate(baseline_path: str, current_path: str) -> int:
    """Run the operational-resilience deployment gate."""
    baseline_points = load_json(baseline_path)
    current_points = load_json(current_path)

    baseline_mean, baseline_std = build_baseline(baseline_points)

    anomalies = detect_anomalies(
        current_points,
        baseline_mean,
        baseline_std,
    )

    decision = evaluate(
        anomalies=anomalies,
        findings=[],
    )

    explanation = narrate(decision)

    print(f"Decision: {decision.decision.value.upper()}")
    print(explanation)

    if decision.decision.value == "block":
        return 2

    if decision.decision.value == "warn":
        return 1

    return 0


def main() -> None:
    """Run ResilienceGate from the command line."""
    parser = argparse.ArgumentParser(
        description="Evaluate operational telemetry before deployment."
    )

    parser.add_argument(
        "--baseline",
        required=True,
        help="Path to baseline telemetry JSON.",
    )

    parser.add_argument(
        "--current",
        required=True,
        help="Path to current telemetry JSON.",
    )

    args = parser.parse_args()

    exit_code = run_gate(
        baseline_path=args.baseline,
        current_path=args.current,
    )

    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
