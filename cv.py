import cv2
import numpy as np

COEFF = 50 / 41

im = cv2.imread('clouds/1647865824.5085747.jpg')
im = cv2.rotate(im, cv2.ROTATE_180)

frame_center = np.array((im.shape[1] // 2, im.shape[0] // 2))

hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

blue = cv2.inRange(hsv, (100,0,0), (180,255,255))

cnt, _ = cv2.findContours(blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnt:
    if cv2.contourArea(c) > 100:
        (x, y), (w, h), angle = rect = cv2.minAreaRect(c)

        center = np.array((int(x), int(y)))
        center_from_frame = center - frame_center
        mm = center_from_frame * COEFF

        box = cv2.boxPoints(rect)  # cv2.boxPoints(rect) for OpenCV 3.x
        box = np.int0(box)

        print(rect, center_from_frame, mm, frame_center)

        cv2.drawContours(im, [box], 0, (0, 0, 255), 2)
        cv2.circle(im, center, 1, (0,255,0), -1)
        cv2.circle(im, frame_center, 5, (0, 255, 0), -1)



        cv2.imshow("im", im)
        cv2.imshow("i", blue)
        cv2.waitKey()


print(len(cnt))

