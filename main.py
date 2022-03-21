import time
from math import pi
import cv2 as cv
from OperateCamera import OperateCamera
from UR10E import UR10E


robot = UR10E("172.31.1.25")
cam = OperateCamera()



def catch_img():
    data = "data_set/test5.ply"
    frame = cam.catch_frame()
    cam.save(data)
    pcd = cam.open(data)
    cam.visualization_of_points(pcd)
    return frame

def main():
    frame = catch_img()
    print(frame.points[0])
    print(frame.colors[0])
    robot.close()

if __name__ == "__main__":
    main()
