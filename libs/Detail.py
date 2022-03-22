from enum import Enum
import numpy as np

PIXEL_TO_M_COEFF = 0.00082


class DetailType(Enum):
    DEFAULT = 0
    SQUARE = 1
    LONG = 2


class Detail:
    def __init__(self, type: DetailType, center_px: np.ndarray, width: int, height: int, angle: float, z: float):
        self.type = type
        self.center_px = center_px
        self.center_m = self.center_px * PIXEL_TO_M_COEFF
        self.width = width
        self.height = height
        self.angle = angle
        self.z = z
