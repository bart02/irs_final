import time
from math import pi

from OperateCamera import OperateCamera
import UR10E
from OperateRobot import OperateRobot

# Connection to the robot
rob = OperateRobot("172.31.1.25")

# Taking global linear position of arm
pos = rob.getl()
x = -810.440
y = -172.290
z = 908.820
moving_coordinates = {"x": x, "y": y, "z": z, "rx": pos[3], "ry": pos[4], "rz": pos[5]}
rob.movel(moving_coordinates)
print(pos)
