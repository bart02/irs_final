import math

import cv2


from libs.CVProcessImage import CVProcessImage
from libs.UR10E import UR10E

robot = UR10E("localhost")
#robot = UR10E("172.31.1.25")

cam = cv2.VideoCapture(0)


blueZone = [-0.89409, 0.26178, 0.33163]
redZone = [-0.705, 0.260930, 0.332240]
# docker
# run - d - -name = "dockursim" - e
# ROBOT_MODEL = UR10 - p
# 8080: 8080
# -p
# 29999: 29999 - p
# 30001 - 30004: 30001 - 30004 - v / mnt / c / Users / Viktor / PycharmProjects / irs_final: / ursim / programs - v
# dockursim: / ursim - -privileged - -cpus = 1 - -gpus = all
# arranhs / dockursim: latest
def main():
    cur = 'blue'
    while True:
        # detect cube
        ret, frame = cam.read()
        im = CVProcessImage(frame = frame)
        rects = im.get_rects(im.blue_thresh if cur == 'blue' else im.red_thresh)
        if len(rects) == 0:
            break

        # pick cube
        ZERO = -44.32 * ( math.pi/ 180)
        robot.open_gripper()
        x = rects[0][0][0]
        y = rects[0][0][1]
        robot.setTool(math.radians(-100), -(ZERO + rects[0][1]))
        robot.setPos(x, y, 0)
        robot.close_gripper()

        # place cube to zone
        robot.setPos(0, 0, 0.2)
        robot.setTool(None, ZERO)
        r = robot.getl()
        if cur == 'blue': zone = blueZone
        else: zone = redZone
        for i in range(3): r[i] = zone[i]
        robot.movel_list(zone)
        robot.open_gripper()
        robot.setPos(0, 0, 0.2)

        # switch zone
        if cur == 'blue': cur = 'red'
        else: cur = 'blue'
    ######
    # end main
    robot.close()



if __name__ == "__main__":
    main()
