"""Tests for ResilienceGate telemetry ingestion."""

import pytest

from resilience_gate.telemetry.ingest import normalize


def test_normalize_valid_metric():
    """A valid raw metric should normalize into the expected structure."""
    pytest.skip("Ingestion implementation is not complete yet.")


def test_normalize_rejects_invalid_metric():
    """Malformed telemetry should be rejected rather than silently ignored."""
    pytest.skip("Ingestion implementation is not complete yet.")
