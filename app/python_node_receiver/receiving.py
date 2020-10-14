#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class receiving :

    def __init__(self):
        rospy.init_node('receiving', anonymous=True)
        rospy.Subscriber('/remotepub', String, self.callback)
     
     def callback(self,data):
         rospy.loginfo("data received from the sender:")
         rospy.loginfo(data)

if __name__ == '__main__':
    c = sending()
    rospy.spin()
    