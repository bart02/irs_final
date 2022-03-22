import cv2
from libs.CVProcessImage import CVProcessImage

cam = cv2.VideoCapture(0)
ret, frame = cam.read()


im = CVProcessImage(frame = frame)
im.show('w')
cv2.imshow("l", im.blue_thresh)
cv2.waitKey()

rects = im.get_rects(im.blue_thresh)

print(rects)
