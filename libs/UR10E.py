from libs.OperateRobot import OperateRobot
from math import radians

class UR10E(OperateRobot):
    BASE = {'x': -790.4 / 1000, 
            'y': -172.3 / 1000, 
            'z': 700 / 1000, 
            'rx': 1.487, 
            'ry': 3.536, 
            'rz': -0.669}
    OFFSET = {'x': -70 / 1000,
              'y': 15 / 1000,
              'z': -362 / 1000}

    def __init__(self, ip):
        super().__init__(ip)

    def moveTool(self, xyz, abc=False):
        t = self.getl()
        if len(xyz) == 2:
            t[0] = xyz[0] + ((self.OFFSET['x'] + self.BASE['x']) if not abc else 0)
            t[1] = xyz[1] + ((self.OFFSET['y'] + self.BASE['y']) if not abc else 0)
        else:
            t[2] = xyz[0] + ((self.OFFSET['z'] + self.BASE['z']) if not abc else 0)
        print(t)
        self.movel(t)

    def initTool(self):
        self.movel(self.BASE)

    def rotateTool(self, a, b):
        joint = self.getj()
        if a: joint[3] = radians(a)
        if b: joint[5] = radians(-b - 44.32)
        self.movej(joint)
