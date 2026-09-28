"""Shared data structures for ResilienceGate."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class Severity(str, Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Decision(str, Enum):
    ALLOW = "allow"
    WARN = "warn"
    BLOCK = "block"


@dataclass
class MetricPoint:
    """A single normalized observation of one metric for one service."""
    timestamp: datetime
    service: str
    metric: str
    value: float
    unit: str = ""


@dataclass
class Anomaly:
    """A scored deviation from a service's established baseline."""
    timestamp: datetime
    service: str
    metric: str
    observed: float
    baseline: float
    deviation_sigma: float
    score: float
    severity: Severity
    explanation: str = ""


@dataclass
class DependencyFinding:
    """A known vulnerability affecting one declared dependency."""
    package: str
    version: str
    vulnerability_id: str
    severity: Severity
    summary: str
    fixed_version: str | None = None
    explanation: str = ""


@dataclass
class GateDecision:
    """The outcome of evaluating policy against current signals."""
    decision: Decision
    rules_fired: list[str] = field(default_factory=list)
    anomalies: list[Anomaly] = field(default_factory=list)
    findings: list[DependencyFinding] = field(default_factory=list)
    explanation: str = ""
    evaluated_at: datetime = field(default_factory=datetime.utcnow)
