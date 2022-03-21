from OperateRobot import OperateRobot
from math import pi
import time


class UR10E(object):
    startPos = {"x": 0.17916, "y": 0.75838, "z": 0.33674, "rx": 1.487, "ry": 3.536, "rz": -0.669}

    def __init__(self, ip):
        self.robot = OperateRobot(ip)
        self.robot.movel(self.startPos)
        time.sleep(2)


    def setAng(self, ang):
        t = self.robot.getl()
        t[4] = ang
        self.robot.movel(t)
        time.sleep(2)

    def setPos(self, dx, dy, dz):
        if self.startPos[2] + dz < 0.07:
            raise NameError('you are dumb')
        t = self.robot.getl()
        t[0] = self.startPos[0] + dx
        t[1] = self.startPos[1] + dy
        t[2] = self.startPos[2] + dz
        t[5] = 0
        self.robot.movel(t)
        time.sleep(2)

    def initPos(self):
        self.robot.movel(self.startPos)
        time.sleep(2)

    def close(self):
        self.robot.close()
