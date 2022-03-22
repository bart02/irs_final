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
    robot.open_gripper()

    ret, frame = cam.read()
    im = CVProcessImage(frame=frame)
    rects = im.get_rects(im.blue_thresh)

    # get z off-set pose
    x = rects[0][0][0]
    y = rects[0][0][1]
    z = 0 #z off-set
    print(x,y)
    robot.setPos(x, y, z, 0)
    robot.close_gripper()
    #####

    robot.setPos(0, 0, 0.1, 0)

    x = -0.87409
    y = 0.25178
    z = 0.33163
    rx= 3.015
    ry = -0.906
    rz = 0
    robot.movel_list(x, y, z, 0)
    ######
    # end main
    robot.close()



if __name__ == "__main__":
    main()
