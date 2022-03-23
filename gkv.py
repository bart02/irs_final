import pickle
from time import time

import cv2

from libs.Camera import Camera

camera = Camera()
photo = camera.take_photo()



# red = photo.bgr[20:200, 200:400]
# b = photo.bgr[220:400, 200:400]

cv2.imshow("w", photo.bgr)
cv2.waitKey()

cv2.imwrite(f'{time()}.jpg', photo.bgr)
pickle.dump(photo, f'{time()}.pkl')