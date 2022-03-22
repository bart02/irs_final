import cv2
from libs.CVProcessImage import CVProcessImage

cam = cv2.VideoCapture(0)
ret, frame = cam.read()



im = CVProcessImage(fn='../data_set/img.png')
im.show('w')
cv2.imshow("l", im.blue_thresh)
cv2.waitKey()

rects = im.get_rects(im.blue_thresh)

print(rects)


# [-115 -222]
# [-112  163]
# [(array([-0.09583333, -0.185     ]), 1.5707963267948966), (array([-0.09333333,  0.13583333]), -0.0)]

print(-0.09583333/-0.95417)
print(-0.185/-0.350140)