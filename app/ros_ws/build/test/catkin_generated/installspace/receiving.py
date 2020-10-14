#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class Receiving:

    def __init__(self):
        rospy.init_node('receiving', anonymous=True)
        rospy.Subscriber('/remotepub', String, self.callback)
     
     def callback(self,data):
        rospy.loginfo(f"data received from the sender: {data}")

if __name__ == '__main__':
    c = Receiving()
    rospy.spin()
    