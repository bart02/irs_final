from libs.UR10E import UR10E

robot = UR10E("localhost")
#robot = UR10E("172.31.1.25")

# docker
# run - d - -name = "dockursim" - e
# ROBOT_MODEL = UR10 - p
# 8080: 8080
# -p
# 29999: 29999 - p
# 30001 - 30004: 30001 - 30004 - v / mnt / c / Users / Viktor / PycharmProjects / irs_final: / ursim / programs - v
# dockursim: / ursim - -privileged - -cpus = 1 - -gpus = all
# arranhs / dockursim: latest
def main():


    robot.open_gripper()
    # get z off-set pose
    x = 0
    y = 0
    z = -362.5/1000 #z off-set
    robot.setPos(x, y, z)
    robot.close_gripper()

    # end main
    robot.close()



if __name__ == "__main__":
    main()
