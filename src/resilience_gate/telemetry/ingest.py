"""Ingest raw service metrics and normalize them to MetricPoint records.

Layer 1 of the ResilienceGate architecture: the data foundation.
Raw operational telemetry arrives in inconsistent shapes from different
sources; everything downstream assumes a single normalized form.
"""

from resilience_gate.models import MetricPoint


def load_json(path: str) -> list[MetricPoint]:
    """Read metrics from a JSON file and return normalized points.

    Raises ValueError on malformed rows rather than dropping them silently —
    silent data loss in a monitoring tool is itself a reliability failure.
    """
    raise NotImplementedError


def load_csv(path: str) -> list[MetricPoint]:
    """Read metrics from a CSV file and return normalized points."""
    raise NotImplementedError


def normalize(raw: dict) -> MetricPoint:
    """Convert one raw record to a MetricPoint, coercing units."""
    raise NotImplementedError
