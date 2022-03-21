import time
from math import pi

from OperateCamera import OperateCamera


cam = OperateCamera()
# Taking data frame from camera (RGBD format)
frame = cam.catch_frame()

# Printing x y z of some point
print(frame.points[0])
# Printing r g b color of some point
print(frame.colors[0])

lihgsd = "data_set/test11.ply"

# Saving test data frame from camera (RGBD format)
cam.save(lihgsd)

# Loading test data frame from file (RGBD format)
pcd = cam.open(lihgsd)

# Visualizing test data frame
cam.visualization_of_points(pcd)