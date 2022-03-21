from OperateRobot import OperateRobot
from math import pi
import time


class UR10E(object):
    startPos = {"x": -0.790440, "y": -0.172290, "z": 0.7, "rx": 1.487, "ry": 3.536, "rz": -0.669}

    def __init__(self, ip):
        self.robot = OperateRobot(ip)
        self.robot.movel(self.startPos)
        time.sleep(2)

    def setAng(self, ang):
        t = self.robot.getl()
        t['z'] = ang
        self.robot.movel(t)
        time.sleep(2)

    def setPos(self, dx, dy, dz):
        if self.startPos['z'] + dz < 0.07:
            raise NameError('you are dumb')
        t = self.robot.getl()
        t['x'] = self.startPos['x'] + dx
        t['y'] = self.startPos['y'] + dy
        t['z'] = self.startPos['z'] + dz
        t['rx'] = 3.015
        t['ry'] = -0.906
        t['rz'] = 0
        self.robot.movel(t)
        time.sleep(2)

    def initPos(self):
        self.robot.movel(self.startPos)
        time.sleep(2)

    def close(self):
        self.robot.close()
