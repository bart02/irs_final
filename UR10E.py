import OperateRobot

x = -810.440/1000
y = -172.290/1000
z = 908.820/1000

class UR10E:
    def __init__(self):
        self.robot = OperateRobot("172.31.1.25")
        self.robot.movel(x, y, z)


    def setPos(self, dx, dy, dz):
        self.robot.movel(x + dx, y + dy, z + dz)

    def initPos(self):
        self.robot.movel(x, y, z)




    def close(self):
        self.robot.close()
