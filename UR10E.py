from OperateRobot import OperateRobot
import time


class UR10E(object):
    startPos = {"x": -0.810440, "y": -0.172290, "z": 0.908820, "rx": 1.487, "ry": 3.536, "rz": -0.669}

    def __init__(self):
        self.robot = OperateRobot("172.31.1.25")
        self.robot.movel(self.startPos)
        time.sleep(2)

    def setPos(self, dx, dy, dz):
        pos = {"x": self.startPos[0] + dx,
               "y": self.startPos[1] + dy,
               "z": self.startPos[2] + dz,
               "rx": 1.487,
               "ry": 3.536,
               "rz": -0.669}
        self.robot.movel(pos)
        time.sleep(2)

    def initPos(self):
        self.robot.movel(self.startPos)
        time.sleep(2)

    def close(self):
        self.robot.close()

