import time

import cv2 as cv

cap=cv.VideoCapture(2)
while(True):
  ret,frame=cap.read()
  cv.imshow("frame",frame)
#  print(frame)
  if cv.waitKey(1)==ord("q"):
      cv.imwrite(f'{time.time()}.jpg', frame)
      break
cap.release()
cv.destroyAllWindows()
