#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from dynamixel_msgs.msg import MotorStateList

class gestion_roue:

    def __init__(self):

        rospy.init_node('gestion_speed_roues', anonymous=True)
        self.speed_roue_gauche = rospy.Publisher('/joint1_controller/command', Float64, queue_size=10)
        self.speed_roue_droite = rospy.Publisher('/joint2_controller/command', Float64, queue_size=10)
        self.position_eponge = rospy.Publisher('/joint3_controller/command', Float64, queue_size=10)
        self.speed_motor = rospy.Publisher('/motor_states/pan_tilt_port', MotorStateList, queue_size=10)
        rospy.sleep(10)
        rospy.loginfo("changemement de vitesse")
        self.speed_roue_gauche.publish(-3)
        self.speed_roue_droite.publish(-7)
        rospy.sleep(10)
        self.speed_roue_gauche.publish(0)
        self.speed_roue_droite.publish(0)
        rospy.loginfo("changemement de position")
        self.position_eponge.publish(5)

if __name__ == '__main__':
    c = gestion_roue()
    rospy.spin()

