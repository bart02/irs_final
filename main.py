from libs.UR10E import UR10E

robot = UR10E("172.31.1.25")


def main():
    x = -176 / 1000
    y = -95 / 1000
    robot.setPos(x, y, 0)
    robot.close()


if __name__ == "__main__":
    main()
