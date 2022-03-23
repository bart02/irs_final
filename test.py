from libs.Camera import DummyCamera
from libs.UR10E import UR10E

robot = UR10E('localhost')

def main():
    robot.pushHeap(0.12, 0.2, [0.4, 0.6], 0.05)
    robot.close()

if __name__ == '__main__':
    main()
