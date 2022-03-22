from typing import Union

import urx

class OperateRobot:
    # common
    def __init__(self, ip):
        self.rob = urx.Robot(ip)

    def open_gripper(self):
        self.rob.send_program('set_tool_digital_out(0, True)')
        self.rob.send_program('set_tool_digital_out(1, False)')

    def close_gripper(self):
        self.rob.send_program('set_tool_digital_out(0, False)')
        self.rob.send_program('set_tool_digital_out(1, True)')

    def close(self):
        self.rob.close()

    # for coordinates
    def movel(self, point: Union[dict, list]):
        if isinstance(point, dict):
            self.rob.movel((point["x"], point["y"], point["z"], point["rx"], point["ry"], point["rz"]), 0.2, 0.2)
        else:
            self.rob.movel(point, 0.2, 0.2)

    def getl(self):
        return self.rob.getl()

    # for joints
    def getj(self):
        return self.rob.getj()

    def movej(self, j):
        self.rob.movej(j, vel=0.6)
