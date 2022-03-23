from libs.OperateRobot import OperateRobot
from math import radians, sqrt
from libs.AGLA import intersection

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

    j3init = -147.22
    j5init = - 44.32

    def setAng(self, a, b):
        joint = self.getj()
        joint[3] = radians(a + self.j3init)
        joint[5] = radians(-b + self.j5init)
        self.movej(joint, VELOCITY)

    def initAng(self):
        joint = self.getj()
        joint[3] = radians(self.j3init)
        joint[5] = radians(self.j5init)
        self.movej(joint, VELOCITY)

    def pushHeap(self, width, height, dxy, pushHeight, flag):
        r = sqrt(width ** 2 + height ** 2) / 2 * PUSH_HEAP_SCALE
        i = intersection([dxy[0], dxy[1]], r, [0, 0], [dxy[0], dxy[1]])

        further = i[0] if abs(i[0][0]) > abs(i[1][0]) else i[1]
        near = i[1] if further == i[0] else i[0]

        if flag:
            start = further
            end = near

        self.setPos(*start, pushHeight)
        self.setPos(*end, pushHeight)
