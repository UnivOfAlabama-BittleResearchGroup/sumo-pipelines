from dataclasses import dataclass, field
from typing import Any, List, Tuple

from sumo_pipelines.blocks.simulation.config import SimulationConfig


@dataclass
class ComplexSimulationConfig(SimulationConfig):
    vehicle_state_output: str = "${Metadata.cwd}/traj.out.parquet"


@dataclass
class IntersectionWeights:
    mainline_a: float = 1.0
    mainline_b: float = 0.7290
    mainline_c: float = 0.0045
    mainline_d: float = 0 # Please keep this as 0
    mainline_e: float = 0 # Please keep this as 0

    side_a: float = 0.5197
    side_b: float = 0.3635
    side_c: float = 0.0093
    side_d: float = 0 # Please keep this as 0

    truck_waiting_time_factor: float = 2.0
    truck_speed_factor: float = 7.0


ControlledIntersections = List[
    Tuple[str, str, str]
]  # List of tuples of (junction, traffic light id)


@dataclass
class PriorityTrafficLightsRunnerConfig(SimulationConfig):
    intersection_weights: IntersectionWeights = field(
        default_factory=IntersectionWeights
    )
    fcd_output: Any = ""
    controlled_intersections: list = field(default_factory=list)
    crop_polygon: Any = ""
    action_step: int = 2
