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
        robot.initTool()

        # detect cube
        frame = camera.take_photo()
        details = frame.find_str_details(current_color)
        if len(frame.find_all_details()) == 0:
            break
        if len(details) == 0:
            current_color = 'blue' if current_color == 'red' else 'red'
            continue
        detail = details[0]
        print(detail)

        # dick cube
        robot.open_gripper()
        robot.rotateTool(-100, detail.angle)
        robot.moveTool(*detail.center_m, 0)
        robot.close_gripper()

        # go upper and rotate
        robot.moveTool(0.1)
        robot.rotateTool(None, 0)

        # place cube to zone
        z = ZONE[current_color].copy()
        z[2] += len(towers[current_color]) * HEIGHT
        print(z)
        robot.moveTool(*z, True)
        robot.open_gripper()
        robot.moveTool(0.1)

        towers[current_color].append(detail)

        # switch zone
        current_color = 'blue' if current_color == 'red' else 'red'

    robot.close()


if __name__ == '__main__':
    main()
