from enum import Enum
import numpy as np

PIXEL_TO_M_COEFF = 0.00082


class DetailType(Enum):
    HEAP = -1
    LONG = 0
    DEFAULT = 1
    SQUARE = 2


class Detail:
    def __init__(self, type: DetailType, center_px: np.ndarray, width: int, height: int, angle: float, z: float):
        self.type = type
        self.center_px = center_px
        self.center_m = self.center_px * PIXEL_TO_M_COEFF
        self.width = width
        self.height = height
        self.width_m = width * PIXEL_TO_M_COEFF
        self.height_m = height * PIXEL_TO_M_COEFF
        self.angle = angle
        self.z = z

    def __repr__(self):
        return str(self.__dict__)

