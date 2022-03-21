import time
from math import pi

from OperateCamera import OperateCamera
import UR10E
from OperateRobot import OperateRobot

# Connection to the robot

rob = OperateRobot("172.31.1.25")

# Taking global linear position of arm
pos = rob.getl()
x = -810.440/1000
y = -172.290/1000
z = 908.820/1000
rx = 1.487
ry = 3.536
rz = -0.669

moving_coordinates = {"x": x, "y": y, "z": z, "rx": rx, "ry": ry, "rz": rz}
rob.movel(moving_coordinates)
time.sleep(2)

print(pos)
rob.close()