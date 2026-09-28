"""Tests for ResilienceGate telemetry ingestion."""

import json

from resilience_gate.telemetry.ingest import load_csv, load_json


def test_load_json(tmp_path):
    """JSON telemetry should be converted into MetricPoint records."""
    path = tmp_path / "metrics.json"

    path.write_text(
        json.dumps(
            [
                {
                    "timestamp": "2026-09-28T10:00:00",
                    "service": "checkout",
                    "metric": "latency_ms",
                    "value": 120,
                    "unit": "ms",
                }
            ]
        ),
        encoding="utf-8",
    )

    points = load_json(str(path))

    assert len(points) == 1
    assert points[0].service == "checkout"
    assert points[0].metric == "latency_ms"
    assert points[0].value == 120.0
    assert points[0].unit == "ms"


def test_load_csv(tmp_path):
    """CSV telemetry should be converted into MetricPoint records."""
    path = tmp_path / "metrics.csv"

    path.write_text(
        "timestamp,service,metric,value,unit\n"
        "2026-09-28T10:00:00,checkout,latency_ms,125,ms\n",
        encoding="utf-8",
    )

    points = load_csv(str(path))

    assert len(points) == 1
    assert points[0].service == "checkout"
    assert points[0].metric == "latency_ms"
    assert points[0].value == 125.0
    assert points[0].unit == "ms"
