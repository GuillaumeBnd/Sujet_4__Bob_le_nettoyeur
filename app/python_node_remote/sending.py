#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class sending :

    def __init__(self):
        self.pub_remote = rospy.Publisher('/remotepub', String, queue_size =1)
        self.pub_remote.publish("test")


if __name__ == '__main__':
    c = sending()
    rospy.spin()
    