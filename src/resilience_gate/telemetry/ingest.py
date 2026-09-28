"""Ingest raw service metrics and normalize them to MetricPoint records.

Layer 1 of the ResilienceGate architecture: the data foundation.
Raw operational telemetry arrives in inconsistent shapes from different
sources; everything downstream assumes a single normalized form.
"""

import csv
import json
from datetime import datetime

from resilience_gate.models import MetricPoint


def load_json(path: str) -> list[MetricPoint]:
    """Read metrics from a JSON file and return normalized points.

    Raises ValueError on malformed rows rather than dropping them silently —
    silent data loss in a monitoring tool is itself a reliability failure.
    """
    with open(path, "r", encoding="utf-8") as file:
        records = json.load(file)

    return [normalize(record) for record in records]


def load_csv(path: str) -> list[MetricPoint]:
    """Read metrics from a CSV file and return normalized points."""
    with open(path, "r", encoding="utf-8", newline="") as file:
        records = csv.DictReader(file)
        return [normalize(record) for record in records]


def normalize(raw: dict) -> MetricPoint:
    """Convert one raw record to a MetricPoint, coercing units."""
    timestamp = datetime.fromisoformat(raw["timestamp"])
    value = float(raw["value"])
    service = str(raw["service"]).strip()
    metric = str(raw["metric"]).strip()
    unit = str(raw.get("unit", "")).strip()

    return MetricPoint(
        timestamp=timestamp,
        service=service,
        metric=metric,
        value=value,
        unit=unit,
    )
