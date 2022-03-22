import math

import cv2
import numpy as np


class CVProcessImage:
    PIXEL_TO_MM_COEFF = 0.00082

    def __init__(self, fn: str = None, frame: np.ndarray = None):
        if frame is not None:
            self.im = frame.copy()
        elif fn is not None:
            self.im = cv2.imread(fn)
        else:
            raise Exception('You are pidor')
        self.im = cv2.flip(self.im, 1)

    @property
    def blue_thresh(self):
        return cv2.inRange(self.hsv, (90, 50, 50), (180, 255, 255))

    @property
    def red_thresh(self):
        return cv2.inRange(self.hsv, (0, 50, 50), (40, 255, 255))

    def get_rects(self, thresh):
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        rects = []
        for c in contours:
            if cv2.contourArea(c) > 100:
                rect = cv2.minAreaRect(c)

                (x, y), (w, h), angle = rect
                if w > h:
                    # angle = 90 - angle
                    w, h = h, w
                if 3 * w > h:
                    print("long detail")
                
                angle = math.radians(angle)

                center = np.array((int(x), int(y)))
                center_from_frame: np.ndarray = center - self.frame_center
                center_from_frame[1] = -center_from_frame[1]
                center_from_frame = np.flip(center_from_frame)

                print(center_from_frame)
                center_from_frame_mm: np.ndarray = center_from_frame * self.PIXEL_TO_MM_COEFF  # in meters

                rects.append((center_from_frame_mm, angle))
        return rects

    @property
    def hsv(self):
        return cv2.cvtColor(self.im, cv2.COLOR_BGR2HSV)

    @property
    def frame_center(self):
        return np.array((self.im.shape[1] // 2, self.im.shape[0] // 2))

    def show(self, window: str):
        cv2.imshow(window, self.im)
        cv2.waitKey()
