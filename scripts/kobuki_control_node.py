#!/usr/bin/python

import rospy
from kobuki_model import kobuki_model_V1

# Init of program
if __name__ == '__main__':

    rospy.init_node('kobuki_wheels_control', anonymous=True)

    rospy.loginfo("Node control")

    kobuki_model_V1()

    #rospy.spin()