from libs.OperateRobot import OperateRobot
from math import radians

class UR10E(OperateRobot):
    BASE = {"x": -790.4, "y": -172.3, "z": 700, "rx": 1.487, "ry": 3.536, "rz": -0.669}
    OFFSET = [-70, 15, -362.5]

    def __init__(self, ip):
        super().__init__(ip)

    def moveTool(self, *xyz):
        t = self.getl()
        if len(xyz) == 3:
            t['x'] = xyz[0] + (self.OFFSET[0] + self.BASE[0]) / 1000
            t['y'] = xyz[1] + (self.OFFSET[1] + self.BASE[1]) / 1000
            t['z'] = xyz[2] + (self.OFFSET[2] + self.BASE[2]) / 1000
        else: t['z'] = xyz[0] + (self.OFFSET[2] + self.BASE[2]) / 1000
        self.movel(t)

    def initTool(self):
        self.movel(self.BASE)

    def rotateTool(self, a, b):
        joint = self.getj()
        if a: joint[3] = radians(a)
        if b: joint[5] = radians(-b - 44.32)
        self.movej(joint)
