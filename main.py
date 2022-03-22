from libs.Camera import Camera, DummyCamera
from libs.Detail import Detail
from libs.UR10E import UR10E

# robot initialization
try: robot = UR10E('localhost')
except ConnectionError: robot = UR10E('172.31.1.25')
camera = DummyCamera(fn='data_set/1647866163.3144376.jpg')

ZONE = {'blue': [-0.89409, 0.26178, 0.33163],
        'red': [-0.705, 0.260930, 0.332240]}
HEIGHT = 0.26

def main():
    towers: dict[str, list[Detail]] = {'blue': [], 'red': []}
    cur = 'blue'
    while True:
        # move to init state to take picture
        robot.initTool()

        # detect cube
        frame = camera.take_photo()
        details = frame.find_str_details(cur)
        if len(details) == 0:
            break
        detail = details[0]
        print(detail)

        # pick cube
        robot.open_gripper()
        robot.rotateTool(-100, detail.angle)
        robot.moveTool(detail.center_m)
        robot.moveTool([0])
        robot.close_gripper()

        # go upper and rotate
        robot.moveTool([0.1])
        robot.rotateTool(None, 0)

        # place cube to zone
        z = ZONE[cur].copy()
        z[2] += len(towers[cur]) * HEIGHT
        print(z)
        robot.moveTool(z[0:2], True)
        robot.moveTool([z[2]], True)
        robot.open_gripper()
        robot.moveTool([0.1])

        # switch zone
        cur = 'blue' if cur == 'red' else 'red'

    robot.close()


if __name__ == '__main__':
    main()
