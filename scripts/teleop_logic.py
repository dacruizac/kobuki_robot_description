import rospy
#import keyboard
import getch
from geometry_msgs.msg import Twist
from rospy.numpy_msg import numpy_msg  
import numpy as np
#from Tkinter import Tk,StringVar,Label
#import os

def h():
    rospy.loginfo(2)

class teleop_kobuki:
    
    def __init__(self):
        self.linear_vel=0
        self.is_working=True
        self.angular_vel=0
        self.nameTopicPub = "/kobuki/teleop_vel"
        self.new_msg = Twist()
        self.pub_vel = rospy.Publisher(self.nameTopicPub, numpy_msg(Twist), queue_size=10)
        rate = rospy.Rate(10) # 20 Hz
        while (not rospy.is_shutdown() and self.is_working):
            #self.read_keyboard()
            k=ord(getch.getch())# this is used to convert the keypress event in the keyboard or joypad , joystick to a ord value
            #if ((k>=65)&(k<=68)|(k==115)|(k==113)|(k==97)|(k==112)):# to filter only the up , dowm ,left , right key /// this line can be removed or more key can be added to this
            #    rospy.loginfo(str(k))# to print on  terminal 

            if ((k>=65) and (k<=68)):
                #rospy.loginfo(str(k))# to print on  terminal 
                if (k==65):
                    self.new_msg.linear.x=1
                    self.new_msg.angular.z=0
                elif (k==66):
                    self.new_msg.linear.x=-1
                    self.new_msg.angular.z=0
                elif (k==67):
                    self.new_msg.linear.x=0
                    self.new_msg.angular.z=-np.pi
                else:
                    self.new_msg.linear.x=0
                    self.new_msg.angular.z=np.pi
                self.pub_vel.publish(self.new_msg)
            


            #self.pub_vel.publish(self.new_msg)
            if (k==ord('p')):
                self.new_msg.linear.x=0
                self.new_msg.angular.z=0
                self.pub_vel.publish(self.new_msg)
            if (k==ord('q')):
                rospy.loginfo("fin")
                self.is_working=False
                rospy.signal_shutdown("Request shutdown")
            rate.sleep()


    #def read_keyboard(self):
    #    if keyboard.is_pressed('p'):
    #        rospy.loginfo("pressed")



#class teleop_kobuki(Tk,object):
    
#    def __init__(self):
#        print(1)
#        super(teleop_kobuki,self).__init__()
#        self.geometry("100x100")
#        self.bind("<KeyPress>", self.keydown)
#        self.bind("<KeyRelease>", self.keyup)
#        self.sensorText = StringVar()
#        self.sensorLabel = Label(self, textvariable=self.sensorText)
#        self.sensorLabel.pack()
#        self.mainloop()
    
#    def keydown(self,event):
#        rospy.loginfo("pressed")

#    def keyup(self,event):
#        rospy.loginfo("relesed")