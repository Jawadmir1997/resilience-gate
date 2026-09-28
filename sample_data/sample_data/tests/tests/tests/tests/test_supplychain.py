"""Tests for ResilienceGate software supply-chain analysis."""

import pytest

from resilience_gate.supplychain.sbom import (
    load_sbom,
    normalize_components,
)
from resilience_gate.supplychain.osv import (
    check_dependency,
    check_dependencies,
)


def test_load_sbom():
    """A CycloneDX SBOM should produce normalized dependency information."""
    pytest.skip("SBOM parsing implementation is not complete yet.")


def test_normalize_components():
    """SBOM components should normalize into package and version pairs."""
    pytest.skip("SBOM parsing implementation is not complete yet.")


def test_check_dependency():
    """A dependency should be checked for known vulnerability findings."""
    pytest.skip("OSV lookup implementation is not complete yet.")


def test_check_dependencies():
    """Multiple dependencies should return combined vulnerability findings."""
    pytest.skip("OSV lookup implementation is not complete yet.")
