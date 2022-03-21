from libs.OperateRobot import OperateRobot
import time


class UR10E:
    startPos = {"x": -0.790440, "y": -0.172290, "z": 0.7, "rx": 1.487, "ry": 3.536, "rz": -0.669}

    def __init__(self, ip):
        self.robot = OperateRobot(ip)
        self.robot.movel(self.startPos)
        time.sleep(2)

    def setPos(self, dx, dy, dz, ang):
        if self.startPos['z'] + dz < 0.07:
            raise Exception('you are dumb')
        t = self.robot.getl()
        t[0] = self.startPos['x'] + dx
        t[1] = self.startPos['y'] + dy
        t[2] = self.startPos['z'] + dz
        t[3] = 3.015
        t[4] = -0.906
        t[5] = ang
        self.robot.movel_list(t)
        time.sleep(2)

    def initPos(self):
        self.robot.movel(self.startPos)
        time.sleep(2)

    def close(self):
        self.robot.close()
