import cv2
from libs.CVProcessImage import CVProcessImage

cam = cv2.VideoCapture(0)
ret, frame = cam.read()


im = CVProcessImage(frame=frame)
rects = im.get_rects(im.blue_thresh)

print(rects)
