import time
import cv2

from libs.Camera import Camera, DummyCamera
from libs.Detail import Detail, DetailType
from libs.UR10E import UR10E

# robot initialization
try:
    robot = UR10E('172.31.1.25')
    print("connected to robot")
    camera = Camera()
    print("connected to cam")
except ConnectionError:
    pass
# robot = UR10E('localhost')
# camera = DummyCamera(fn='data_set/1647866163.3144376.jpg')

ZONE = {'blue': [-0.89409, 0.26178, 0.33163],
        'red': [-0.70500, 0.26093, 0.33224]}

UPPER_ZONE = [-0.755, 0.26, 0.7, 1.487, 3.536,  -0.669]

HEIGHT = 0.025

TOWER_PICTURE_OFFSET = 200 / 1000


def main():
    towers: dict[str, list[Detail]] = {'blue': [], 'red': []}
    current_color = 'blue'
    while True:
        # move to init state to take picture
        print("cycle")
        robot.initPos()

        # detect current_color detail position
        frame = camera.take_photo()
        details = frame.find_str_details(current_color)

        if len(frame.find_all_details()) == 0:
            break
        if len(details) == 0:
            current_color = 'blue' if current_color == 'red' else 'red'
            continue
        detail = details[0]

        print(detail)
        if detail.type == DetailType.HEAP:
            print("push heap")
            # robot.pushHeap(detail.height_m, detail.width_m, detail.center_m, 0.005)
            # continue
        while detail.type == DetailType.LONG:
            details.pop(0)
            detail = details[0]

        visota = max(0, (530 - detail.z) // 20 * 0.025)
        print(visota, detail)

        # pick detail
        robot.open_gripper()
        robot.setAng(-100.0, detail.angle)
        robot.setPos(*detail.center_m, visota)
        robot.close_gripper()

        # lift and rotate the detail
        robot.setPos(0.1 + len(towers[current_color]) * HEIGHT)
        robot.initAng()

        # place detail in current_color zone
        z = ZONE[current_color].copy()
        z[2] += len(towers[current_color]) * HEIGHT
        robot.setPos(*z, True)
        robot.open_gripper()
        time.sleep(1)
        robot.setPos(0.1 + len(towers[current_color]) * HEIGHT)

        # add new detail in current_color tower and switch zone
        robot.movel(UPPER_ZONE, 0.2)
        tower_frame = camera.take_photo()
        # red_h =
        # cv2.imshow("w", tower_frame.bgr)
        # cv2.waitKey()

        towers[current_color].append(detail)
        current_color = 'blue' if current_color == 'red' else 'red'

    robot.close()


if __name__ == '__main__':
    main()
