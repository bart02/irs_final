import time
from libs.Camera import Camera, DummyCamera
from libs.Detail import Detail
from libs.UR10E import UR10E

# robot initialization
try:
    robot = UR10E('172.31.1.25')
    camera = Camera()
except ConnectionError:
    robot = UR10E('localhost')
    camera = DummyCamera(fn='data_set/1647866163.3144376.jpg')

ZONE = {'blue': [-0.89409, 0.26178, 0.33163],
        'red':  [-0.70500, 0.26093, 0.33224]}

HEIGHT = 0.025

TOWER_PICTURE_OFFSET = 30 / 1000

def main():
    towers: dict[str, list[Detail]] = {'blue': [], 'red': []}
    current_color = 'blue'
    while True:
        # move to init state to take picture
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


        if (detail.type == "HEAP"):
            robot.pushHeap(detail.height_m, detail.width_m, detail.center_m, 0.005)
            continue
        while (detail.type=="LONG"):
            details.pop(0)
            detail = details[0]

        visota = max(0, (530 - detail.z) // 20 * 0.025)
        print(visota)

        print(detail)
        # pick detail
        robot.open_gripper()
        robot.setAng(-100.0, detail.angle)
        robot.setPos(*detail.center_m, visota)
        robot.close_gripper()

        # lift and rotate the detail
        robot.setPos(len(towers[current_color]))
        robot.initAng()

        # place detail in current_color zone
        z = ZONE[current_color].copy()
        z[2] += len(towers[current_color]) * HEIGHT
        robot.setPos(*z, True)
        robot.open_gripper()
        time.sleep(1)
        robot.setPos(-790.4 / 1000, -172.3 / 1000 + TOWER_PICTURE_OFFSET, 700.1 / 1000, True)

        # add new detail in current_color tower and switch zone
        towers[current_color].append(detail)
        current_color = 'blue' if current_color == 'red' else 'red'

    robot.close()


if __name__ == '__main__':
    main()
