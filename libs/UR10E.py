from libs.OperateRobot import OperateRobot

class UR10E(OperateRobot):
    startPos = {"x": -0.790450, "y": -0.172270, "z": 0.7, "rx": 1.487, "ry": 3.536, "rz": -0.669}

    def __init__(self, ip):
        super().__init__(ip)
        self.initPos()

    def setPos(self, dx, dy, dz, ang):
        if self.startPos['z'] - dz < 0.07:
            raise Exception('you are dumb')
        t = self.getl()
        offset = [0, 0, 362.5/1000]
        t[0] = self.startPos['x'] + dx + offset[0]
        t[1] = self.startPos['y'] + dy + offset[1]
        t[2] = self.startPos['z'] - dz + offset[2]
        t[3] = 3.015
        t[4] = -0.906
        t[5] = ang
        self.movel_list(t)

    def initPos(self):
        self.movel(self.startPos)

