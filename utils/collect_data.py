import time
from libs.OperateCamera import OperateCamera
import cv2

depth = OperateCamera()
cam = cv2.VideoCapture(0)


def catch_cloud(fn: str):
    cloud = depth.catch_frame()
    depth.save(fn)
    return cloud


while True:
    ret, frame = cam.read()
    cv2.imshow("frame", frame)
    #  print(frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('s'):
        t = time.time()
        cv2.imwrite(f'{t}.jpg', frame)
        catch_cloud(f'{t}.ply')

cam.release()
cv2.destroyAllWindows()
