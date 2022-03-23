import time
from typing import Optional

import cv2
import numpy as np

from libs.Frame import Frame
from libs.OperateCamera import OperateCamera


class Camera:
    def __init__(self):
        self._camera = OperateCamera()

    def _take_photo(self) -> Optional[Frame]:
        ret, depth_frame, color_frame = self._camera.get_color_depth_frame()
        depth_frame = np.flip(depth_frame, 1)
        color_frame = np.flip(color_frame, 1)
        if ret:
            return Frame(depth_frame, color_frame, self)
        else:
            return None

    def take_photo(self):
        i = 0
        while True:
            frame = self._take_photo()
            if frame is not None:
                return frame
            time.sleep(0.05)
            i += 1
            if i > 20:
                raise Exception('Camera is broken')

    @property
    def frame_center(self):
        return np.array((640 // 2, 480 // 2))


class DummyCamera(Camera):
    def __init__(self, fn):
        self._image = cv2.imread(fn)
        pass

    def _take_photo(self) -> Optional[Frame]:
        return Frame(cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY), self._image, self)
