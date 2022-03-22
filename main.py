from libs.Camera import Camera, DummyCamera
from libs.Detail import Detail
from libs.UR10E import UR10E

# robot initialization
try:
    robot = UR10E('localhost')
    camera = DummyCamera(fn='data_set/1647866163.3144376.jpg')
except ConnectionError:
    robot = UR10E('172.31.1.25')
    camera = Camera()


ZONE = {'blue': [-0.89409, 0.26178, 0.33163],
        'red': [-0.705, 0.260930, 0.332240]}

HEIGHT = 0.26

def main():
    towers: dict[str, list[Detail]] = {'blue': [], 'red': []}
    current_color = 'blue'

    # sbivalka
    frame = camera.take_photo()
    details = frame.find_str_details(current_color)
    details = list(filter(lambda x: x.z > 5, details))
    print(details)
    for d in details:
        pass
        # sbit()

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
        print(detail)

        # pick detail
        robot.open_gripper()
        robot.setAng(-100.0, detail.angle)
        robot.setPos(*detail.center_m, 0)
        robot.close_gripper()

        # lift and rotate the detail
        robot.setPos(0.1)
        robot.initAng()

        # place detail in current_color zone
        z = ZONE[current_color].copy()
        z[2] += len(towers[current_color]) * HEIGHT
        robot.setPos(*z, True)
        robot.open_gripper()
        robot.setPos(0.1)

        # add new detail in current_color tower and switch zone
        towers[current_color].append(detail)
        current_color = 'blue' if current_color == 'red' else 'red'

    robot.close()


if __name__ == '__main__':
    main()
