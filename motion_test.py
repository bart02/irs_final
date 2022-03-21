import time
from math import pi

from OperateCamera import OperateCamera
from OperateRobot import OperateRobot

# Connection to the robot
rob = OperateRobot("172.31.1.25")

# Taking global linear position of arm
pos = rob.getl()

print(pos)

