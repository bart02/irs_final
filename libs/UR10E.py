from libs.OperateRobot import OperateRobot
from math import radians

class UR10E(OperateRobot):
    BASE = {"x": -790.4 / 1000, "y": -172.3 / 1000, "z": 700 / 1000, "rx": 1.487, "ry": 3.536, "rz": -0.669}
    OFFSET = [-70 / 1000, 15 / 1000, -362.5 / 1000]

    def __init__(self, ip):
        super().__init__(ip)

    def moveTool(self, *xyz):
        t = self.getl()
        if len(xyz) == 3:
            t[0] = xyz[0] + self.OFFSET[0] + self.BASE["x"]
            t[1] = xyz[1] + self.OFFSET[1] + self.BASE["y"]
            t[2] = xyz[2] + self.OFFSET[2] + self.BASE["z"]
        else: t[2] = xyz[0] + self.OFFSET[2] + self.BASE["z"]
        r = {"x": t[0], "y": t[1], "z": t[2], "rx": t[3], "ry": t[4], "rz": t[5]}
        self.movel(r)

    def initTool(self):
        self.movel(self.BASE)

    def rotateTool(self, a, b):
        joint = self.getj()
        if a: joint[3] = radians(a)
        if b: joint[5] = radians(-b - 44.32)
        self.movej(joint)
