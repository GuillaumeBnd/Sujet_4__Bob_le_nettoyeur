#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class Sending :

    def __init__(self):
        rospy.init_node('sending', anonymous=True)
        self.pub_remote = rospy.Publisher('/remotepub', String, queue_size = 10)
        self.pub_remote.publish("test")


if __name__ == '__main__':
    c = Sending()
    rospy.spin()
    