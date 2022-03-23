from libs.OperateRobot import OperateRobot
from math import radians, sqrt
from libs.AGLA import intersection
from numpy import sign

BASE = {'x': -790.4 / 1000,
        'y': -172.3 / 1000,
        'z':  700.1 / 1000,
        'rx':  1.487,
        'ry':  3.536,
        'rz': -0.669}

OFFSET = {'x': -55 / 1000,
          'y':  15 / 1000,
          'z': -362 / 1000}

VELOCITY = 0.6

PUSH_HEAP_SCALE = 1.4

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

    zero = {3: -147.22, 5: -44.32}

    def setAng(self, a, b):
        joint = self.getj()
        if a: joint[3] = radians(a + self.zero[3])
        if b: joint[5] = radians(-b + self.zero[5])
        self.movej(joint, VELOCITY)

    def initAng(self, *arg):
        joint = self.getj()
        for i in range(len(arg)): joint[arg[i]] = radians(self.zero[arg[i]])
        self.movej(joint, VELOCITY)

    def pushHeap(self, width, height, dxy, flag):
        r = sqrt(width ** 2 + height ** 2) / 2 * PUSH_HEAP_SCALE
        i = intersection([dxy[0], dxy[1]], r, [0, 0], [dxy[0], dxy[1]])
        further = i[0] if abs(i[0][0]) > abs(i[1][0]) else i[1]
        near = i[1] if further == i[0] else i[0]
        if not flag:
            x, y = dxy[0] + r * sign(dxy[0]), dxy[1]
            start, end = [x, y], [x - r * 2 * sign(r), y]
        else: start, end = further, near
        self.setPos(*start, 0.005)
        self.setPos(*end, 0.005)

