import cv2

# connect to robot
from libs.CVProcessImage import CVProcessImage
from libs.UR10E import UR10E

# robot initialization
try: robot = UR10E("localhost")
except ConnectionError: robot = UR10E("172.31.1.25")
cam = cv2.VideoCapture(0)

ZONE = {'blue': [-0.89409, 0.26178, 0.33163],
        'red': [-0.705, 0.260930, 0.332240]}

def main():
    height = {'blue': 0, 'red': 0}
    cur = 'blue'
    while True:
        # move to init state to take picture
        robot.initTool()

        # detect cube
        ret, frame = cam.read()
        im = CVProcessImage(fn='data_set/img.png')
        rects = im.get_rects(im.blue_thresh if cur == 'blue' else im.red_thresh)
        if len(rects) == 0: break

        # pick cube
        robot.open_gripper()
        robot.rotateTool(-100, rects[0][1])
        robot.moveTool(rects[0][0][0], rects[0][0][1], 0)
        robot.close_gripper()

        # place cube to zone
        robot.moveTool(0.1)
        robot.rotateTool(None, 0)
        z = ZONE[cur]
        z[2] += height[cur]
        height[cur] += 0.026
        robot.moveTool(z[0], z[1], z[2])
        robot.open_gripper()
        robot.moveTool(0.1)

        # switch zone
        cur = 'blue' if cur == 'red' else 'blue'

    robot.close()

if __name__ == "__main__":
    main()
