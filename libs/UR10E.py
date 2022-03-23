from libs.OperateRobot import OperateRobot
from math import radians, sqrt

BASE = {'x': -790.4 / 1000,
        'y': -172.3 / 1000,
        'z':  700.1 / 1000,
        'rx':  1.487,
        'ry':  3.536,
        'rz': -0.669}

OFFSET = {'x': -55 / 1000,
          'y':  15 / 1000,
          'z': -362 / 1000}

VELOCITY = 0.4

PUSH_HEAP_SCALE = 1.2

class UR10E(OperateRobot):
    def __init__(self, ip):
        super().__init__(ip)

    def setPos(self, *xyz):
        t = self.getl()
        if len(xyz) == 3 or len(xyz) == 1: abc = False
        else: abc = xyz[-1]
        if len(xyz) > 2:
            t[0] = xyz[0] + ((OFFSET['x'] + BASE['x']) if not abc else 0)
            t[1] = xyz[1] + ((OFFSET['y'] + BASE['y']) if not abc else 0)
            self.movel(t, VELOCITY)
            t[2] = xyz[2] + ((OFFSET['z'] + BASE['z']) if not abc else 0)
        else: t[2] = xyz[0] + ((OFFSET['z'] + BASE['z']) if not abc else 0)
        self.movel(t, VELOCITY)

    def initPos(self):
        self.movel(BASE, VELOCITY)

    def setAng(self, a, b):
        joint = self.getj()
        joint[3] = radians(a)
        joint[5] = radians(-b - 44.32)
        self.movej(joint, VELOCITY)

    def initAng(self):
        joint = self.getj()
        joint[5] = radians(-44.32)
        self.movej(joint, VELOCITY)

    def intersection(self, center, circle_radius, pt1, pt2):
        (p1x, p1y), (p2x, p2y), (cx, cy) = pt1, pt2, center
        (x1, y1), (x2, y2) = (p1x - cx, p1y - cy), (p2x - cx, p2y - cy)
        dx, dy = (x2 - x1), (y2 - y1)
        dr = (dx ** 2 + dy ** 2) ** .5
        big_d = x1 * y2 - x2 * y1
        discriminant = circle_radius ** 2 * dr ** 2 - big_d ** 2
        intersections = [
            (cx + (big_d * dy + sign * (-1 if dy < 0 else 1) * dx * discriminant ** .5) / dr ** 2,
             cy + (-big_d * dx + sign * abs(dy) * discriminant ** .5) / dr ** 2)
            for sign in ((1, -1) if dy < 0 else (-1, 1))]
        if len(intersections) == 2 and abs(discriminant) <= 1e-9: return [intersections[0]]
        else: return intersections

    def pushHeap(self, width, height, dxy, pushHeight):
        r = sqrt(width ** 2 + height ** 2) / 2 * PUSH_HEAP_SCALE
        i = self.intersection([dxy[0], dxy[1]], r, [0, 0], [dxy[0], dxy[1]])

        start = i[0]
        end = i[1]

        self.setPos(*start, pushHeight)
        self.setPos(*end, pushHeight)
