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
    def movel(self, point: Union[dict, list], velocity):
        if isinstance(point, dict):
            self.rob.movel((point["x"], point["y"], point["z"], point["rx"], point["ry"], point["rz"]), 0.2, velocity)
        else:
            self.rob.movel(point, 0.2, velocity)

    def getl(self):
        return self.rob.getl()

    # for joints
    def movej(self, j, velocity):
        self.rob.movej(j, 0.2, velocity)

    def getj(self):
        return self.rob.getj()
