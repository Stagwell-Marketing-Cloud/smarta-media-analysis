from enum import Enum

class PointOfViewPattern(Enum):
    POV = "pov"


POINT_OF_VIEW_PATTERNS = {
    PointOfViewPattern.POV: [
        "POV", "point of view", "pointofview"
    ]
}

ALL_POV_PHRASES = set().union(*POINT_OF_VIEW_PATTERNS.values())
