"""Command-line interface for ResilienceGate.

The CLI provides a simple entry point for running the prototype against
telemetry and dependency inputs and displaying the resulting deployment
gate decision.
"""

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Create and return the ResilienceGate command-line parser."""
    parser = argparse.ArgumentParser(
        prog="resilience-gate",
        description="Evaluate operational and supply-chain signals before deployment.",
    )

    parser.add_argument(
        "--metrics",
        help="Path to a JSON or CSV telemetry file.",
    )

    parser.add_argument(
        "--policy",
        default="policy.yaml",
        help="Path to the deployment policy file.",
    )

    return parser


def main() -> None:
    """Run the ResilienceGate command-line interface."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
