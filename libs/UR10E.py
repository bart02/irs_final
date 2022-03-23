from libs.OperateRobot import OperateRobot
from math import radians, sqrt
from shapely.geometry import LineString
from shapely.geometry import Point

BASE = {'x': -790.4 / 1000,
        'y': -172.3 / 1000,
        'z':  700.1 / 1000,
        'rx':  1.487,
        'ry':  3.536,
        'rz': -0.669}

OFFSET = {'x': -55 / 1000,
          'y':  15 / 1000,
          'z': -362 / 1000}

VELOCITY = 0.2
HEAP_SCALE_SCALE = 1

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

    def pushHeap(self, width, height, dxy, pushHeight):
        table = Point(BASE['x'], BASE['y'])
        heap = Point(dxy[0] + BASE['x'], dxy[1] + BASE['y'])

        r = sqrt(width ^ 2 + height ^ 2) / 2 * HEAP_SCALE_SCALE
        c = heap.buffer(r).boundary
        l = LineString([table, heap])
        i = c.intersection(l)

        start = i.geoms[0].coords[0]
        end = i.geoms[1].coords[0]

        self.setPos(*start, pushHeight)
        self.setPos(*end, pushHeight)
