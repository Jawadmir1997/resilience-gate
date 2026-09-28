"""OSV vulnerability lookup interface for ResilienceGate.

This module defines the supply-chain security interface used to evaluate
declared software dependencies against known vulnerability information.
"""

from resilience_gate.models import DependencyFinding


def check_dependency(
    package: str,
    version: str,
) -> list[DependencyFinding]:
    """Check one package version for known vulnerability findings."""
    raise NotImplementedError


def check_dependencies(
    dependencies: list[tuple[str, str]],
) -> list[DependencyFinding]:
    """Check multiple package dependencies and return combined findings."""
    raise NotImplementedError
