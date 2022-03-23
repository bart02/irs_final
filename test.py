from libs.Camera import DummyCamera
from libs.UR10E import UR10E

robot = UR10E('localhost')

def main():
    robot.initPos()
    robot.setAng(47.22, 30)
    robot.initAng(5)
    robot.close()

if __name__ == '__main__':
    main()
