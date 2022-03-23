import cv2
import numpy as np

# from libs.Camera import Camera
from libs.Detail import DetailType, Detail


class Frame:
    def __init__(self, depth_frame: np.ndarray, color_frame: np.ndarray, camera):
        self.depth = depth_frame
        self.bgr = color_frame
        self.camera = camera

        self.hsv = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2HSV)

    def find_details(self, hsv_lowerb: tuple[int, int, int], hsv_upperb: tuple[int, int, int]):
        binarized = cv2.inRange(self.hsv, hsv_lowerb, hsv_upperb)
        contours, _ = cv2.findContours(binarized, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        details = []

        for c in contours:
            if cv2.contourArea(c) > 100:
                rect = cv2.minAreaRect(c)

                (x, y), (w, h), angle = rect

                if w > h:
                    angle = angle - 90
                    w, h = h, w

                if cv2.contourArea(c) / (w * h):
                    type = DetailType.HEAP
                elif 3 * w < h:
                    type = DetailType.LONG
                elif abs(w - h) < 15:
                    type = DetailType.SQUARE
                elif 25 < w < 45 and 50 < h < 70:
                    type = DetailType.DEFAULT
                else:
                    type = DetailType.HEAP

                center = np.array((int(x), int(y)))
                center_from_frame: np.ndarray = center - self.camera.frame_center
                center_from_frame[1] = -center_from_frame[1]  # FIXME
                center_from_frame = np.flip(center_from_frame)

                details.append(Detail(type, center_from_frame, w, h, angle, self.depth[int(y), int(x)]))

        details.sort(key=lambda x: x.type.value)
        return details

    def find_blue_details(self):
        return self.find_details((90, 50, 50), (180, 255, 255))

    def find_red_details(self):
        return self.find_details((0, 50, 50), (40, 255, 255))

    def find_str_details(self, color: str):
        if color == 'blue':
            return self.find_blue_details()
        elif color == 'red':
            return self.find_red_details()
        else:
            raise Exception('No color')

    def find_all_details(self):
        return self.find_blue_details() + self.find_red_details()
