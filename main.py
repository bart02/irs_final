from libs.UR10E import UR10E

robot = UR10E("localhost")


def main():

    #
    x = -176 / 1000
    y = -95 / 1000
    z = -400/1000
    robot.setPos(x, y, z)
    robot.close()



if __name__ == "__main__":
    main()
