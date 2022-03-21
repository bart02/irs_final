import cv2

from libs.OperateCamera import OperateCamera

point = (400, 300)

def show_distance(event, x, y, args, params):
    global point
    point = (x, y)

# Initialize Camera Intel Realsense
dc = OperateCamera()

# Create mouse event
cv2.namedWindow("Color frame")
cv2.setMouseCallback("Color frame", show_distance)

contin = True
one_frame = False

while True:
    if contin:
        ret, _depth_frame, _color_frame = dc.get_color_depth_frame()
        contin = False if one_frame else True
    color_frame = _color_frame.copy()
    depth_frame = _depth_frame.copy()

    # Show distance for a specific point
    cv2.circle(color_frame, point, 4, (0, 0, 255))
    distance = depth_frame[point[1], point[0]]

    cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    depth_frame *= int(depth_frame.max() / 255)

    cv2.imshow("depth frame", depth_frame)
    cv2.imshow("Color frame", color_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break