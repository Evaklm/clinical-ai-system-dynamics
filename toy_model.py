"""Small, transparent toy model of post-deployment clinical AI dynamics.

This is an educational companion to the protected research model. It is not a
clinical forecasting tool and does not reproduce the unpublished Model v2.
"""

from dataclasses import asdict, dataclass
from typing import Iterable


def clamp(value: float) -> float:
    """Restrict a normalized state to the interval [0, 1]."""
    return max(0.0, min(1.0, value))


@dataclass(frozen=True)
class State:
    performance: float = 0.90
    trust: float = 0.75
    use: float = 0.70
    support: float = 0.65
    maintenance: float = 0.60
    concern: float = 0.10


@dataclass(frozen=True)
class Parameters:
    drift: float = 0.018
    monitoring: float = 0.12
    correction: float = 0.10
    workflow_burden: float = 0.04
    trust_adjustment: float = 0.15
    use_adjustment: float = 0.14
    support_adjustment: float = 0.08


def step(state: State, params: Parameters, dt: float = 1.0) -> State:
    """Advance the normalized system by one Euler integration step."""
    detected_gap = params.monitoring * max(0.0, 1.0 - state.performance)
    repair = params.correction * state.maintenance * state.concern

    d_performance = repair - params.drift
    d_concern = detected_gap - 0.10 * state.concern
    d_trust = params.trust_adjustment * (state.performance - state.trust) - (
        params.workflow_burden * state.use
    )
    d_use = params.use_adjustment * (state.trust - state.use)
    realized_benefit = state.performance * state.use
    d_support = params.support_adjustment * (realized_benefit - state.support)
    d_maintenance = 0.10 * (state.support - state.maintenance)

    return State(
        performance=clamp(state.performance + dt * d_performance),
        trust=clamp(state.trust + dt * d_trust),
        use=clamp(state.use + dt * d_use),
        support=clamp(state.support + dt * d_support),
        maintenance=clamp(state.maintenance + dt * d_maintenance),
        concern=clamp(state.concern + dt * d_concern),
    )


def simulate(
    months: int = 60,
    initial: State = State(),
    params: Parameters = Parameters(),
) -> list[dict[str, float]]:
    """Return a monthly trajectory, including the initial state."""
    if months < 0:
        raise ValueError("months must be non-negative")

    trajectory: list[dict[str, float]] = [{"month": 0, **asdict(initial)}]
    state = initial
    for month in range(1, months + 1):
        state = step(state, params)
        trajectory.append({"month": month, **asdict(state)})
    return trajectory


def write_csv(rows: Iterable[dict[str, float]], path: str) -> None:
    import csv

    rows = list(rows)
    if not rows:
        raise ValueError("rows must not be empty")
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    write_csv(simulate(), "toy_trajectory.csv")
    print("Wrote toy_trajectory.csv")

