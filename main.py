import time

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
    robot = UR10E('localhost')
    camera = DummyCamera(fn='data_set/1647866163.3144376.jpg')

ZONE = {'blue': [-0.89409, 0.26178, 0.33163],
        'red': [-0.70500, 0.26093, 0.33224]}

UPPER_ZONE = [-0.755, 0.26, 0.7, 1.487, 3.536,  -0.669]

HEIGHT = 0.025

TABLE_HEIGHT = 520

TOWER_PICTURE_OFFSET = 200 / 1000
flag = False

def main():
    towers: dict[str, list[Detail]] = {'blue': [], 'red': []}
    tower_height = {'blue': 0, 'red': 0}
    current_color = 'blue'
    while True:
        # move to init state to take picture
        print("cycle")
        heaps = 0
        robot.initPos()

        # detect current_color detail position
        frame = camera.take_photo()
        if len(frame.find_all_details()) == 0:
            break

        details = frame.find_str_details(current_color)
        if len(details) == 0:
            current_color = 'blue' if current_color == 'red' else 'red'
            continue

        # get detail
        if len(list(filter(lambda x: x.type == DetailType.SQUARE, towers['blue']))) < 2:  # get heaps if it hasn't got squares
            try:
                detail = list(filter(lambda x: x.type == DetailType.SQUARE, details))[0]
            except IndexError:
                detail = list(filter(lambda x: x.type == DetailType.HEAP, details))[0]
        else:
            detail = details[0]

        print(detail)

        if detail.type == DetailType.HEAP:
            # 1th varioant
            print("push heap")

            robot.close_gripper()
            robot.setAng(47.22, detail.angle)
            robot.pushHeap(detail.height_m, detail.width_m, detail.center_m, 0.005, flag)
            if not(flag) : flag= True
            else: flag = False
            continue
        while detail.type == DetailType.LONG:
            details.pop(0)
            detail = details[0]

        visota = max(0, (TABLE_HEIGHT - detail.z) // 20 * 0.025)
        print(visota, detail)

        # pick detail
        robot.open_gripper()
        robot.setAng(47.22, detail.angle)
        robot.setPos(*detail.center_m, visota)
        robot.close_gripper()

        # lift and rotate the detail
        robot.setPos(0.1 + tower_height[current_color])
        robot.initAng(5)

        # place detail in current_color zone
        z = ZONE[current_color].copy()
        z[2] += tower_height[current_color]
        robot.setPos(*z, True)
        robot.open_gripper()
        time.sleep(1)
        robot.setPos(0.1 + tower_height[current_color])

        # add new detail in current_color tower and switch zone
        robot.movel(UPPER_ZONE, 0.4)  # robot.setPos(-0.755, 0.26, 0.7, True)
        tower_frame = camera.take_photo()
        towers[current_color].append(detail)

        dep = tower_frame.depth
        d = 350 < dep < 600
        tower_height['red'] = (TABLE_HEIGHT - tower_frame.depth[20:200, 200:400].min())
        tower_height['blue'] = (TABLE_HEIGHT - tower_frame.depth[220:400, 200:400].min())
        print('Tower height', tower_height)

        current_color = 'blue' if current_color == 'red' else 'red'

    robot.close()


if __name__ == '__main__':
    main()
