from libs.Camera import DummyCamera
from libs.UR10E import UR10E

robot = UR10E('localhost')

ZONE = {'blue': [-0.89409, 0.26178, 0.33163],
        'red': [-0.70500, 0.26093, 0.33224]}

def main():
    robot.initPos()
    robot.setPos((ZONE['blue'][0] + ZONE['red'][0]) / 2,
                 ZONE['blue'][1],
                 0.7,
                 True)
    robot.initAng(3, 5)
    robot.close()

if __name__ == '__main__':
    main()
