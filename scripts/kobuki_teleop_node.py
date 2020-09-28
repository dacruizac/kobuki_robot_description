#!/usr/bin/python

import rospy
import keyboard
import getch
from teleop_logic import teleop_kobuki

# Init of program
if __name__ == '__main__':

    rospy.init_node('kobuki_teleop', anonymous=True)

    rospy.loginfo("Node teleop")

    teleop_kobuki()

    rospy.spin()