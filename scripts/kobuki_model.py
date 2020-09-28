import rospy
import numpy as np
from geometry_msgs.msg import Twist
from rospy.numpy_msg import numpy_msg
from std_msgs.msg import Float64

class kobuki_model_V1:

    def __init__(self):
        radius = 0.035

        alpha_right =  -np.pi/2
        beta_right  =  np.pi 
        l_right     =  0.150#0.115

        alpha_left = np.pi/2
        beta_left  = 0
        l_left     = 0.080#0.115

        J1 = np.array( [( np.sin(alpha_right+beta_right), -l_right*np.cos(beta_right)),
                        ( np.sin(alpha_left+beta_left)  , -l_left*np.cos(beta_left))])

        J2 = radius*np.identity(2)

        self.Jacobian = np.matmul( np.linalg.pinv(J2) , J1 )

        self.cmd_vel_sub_ = rospy.Subscriber("/kobuki/teleop_vel", Twist, self.cmd_vel_cb, queue_size=10)
        
        
        #----- Publishers
        self.pub_right_wheel  = rospy.Publisher("/right_wheel_controller/command", Float64 , queue_size=10)
        self.pub_left_wheel = rospy.Publisher("/left_wheel_controller/command", Float64 , queue_size=10)

        rospy.spin()


    def cmd_vel_cb(self,msg):
        command = np.array([0,0] , dtype=np.float)

        command[0] = msg.linear.x
        command[1] = msg.angular.z

        #print("Command : ", command)

        result = np.matmul( self.Jacobian, command)

        #print("Result : ", result)

        # Front wheel
        msgFloat = Float64()
        msgFloat.data = result[0]
        self.pub_right_wheel.publish(msgFloat)

        # Left Wheel
        msgFloat = Float64()
        msgFloat.data = result[1]
        self.pub_left_wheel.publish(msgFloat)