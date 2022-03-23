from libs.UR10E import UR10E

robot = UR10E('localhost')

def main():
    robot.initPos()
    robot.setPos(-0.755, 0.26, 0.7, True)
    robot.close()

if __name__ == '__main__':
    main()
