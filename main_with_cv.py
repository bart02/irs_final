import math

import cv2

from libs.CVProcessImage import CVProcessImage
from libs.UR10E import UR10E

#robot = UR10E("localhost")
robot = UR10E("172.31.1.25")

cam = cv2.VideoCapture(0)


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
        ret, frame = cam.read()
        im = CVProcessImage(frame = frame)
        rects = im.get_rects(im.blue_thresh if cur == 'blue' else im.red_thresh)
        if len(rects) == 0:
            break

        ZERO = 44.32 * ( math.pi/ 180)
        robot.open_gripper()
        # get z off-set pose
        x = rects[0][0][0]
        y = rects[0][0][1]
        robot.setAng(3, math.radians(-100))
        print(rects[0][1]*180/math.pi)
        robot.setAng(5, ZERO - rects[0][1])
        robot.setPos(x, y, 0)
        robot.close_gripper()

        #####
        robot.setPos(0, 0, 0.2)
        robot.setAng(5, -ZERO)

        t = robot.getl()
        if cur == 'blue':
            t[0] = -0.89409
            t[1] = 0.26178
            t[2] = 0.33163
        else:
            t[0] = -0.705
            t[1] = 0.260930
            t[2] = 0.332240
        robot.movel_list(t)

        robot.open_gripper()
        robot.setPos(0, 0, 0.2)
        if cur == 'blue':
            cur = 'red'
        else:
            cur = 'blue'
    ######
    # end main
    robot.close()



if __name__ == "__main__":
    main()
