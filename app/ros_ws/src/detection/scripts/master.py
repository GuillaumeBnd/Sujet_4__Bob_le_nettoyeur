#!/usr/bin/env python

#####################################################################################################################################################

# @project        https://gitlab.com/5eti_proto_2021/sujet_4__bob_le_nettoyage.git
# @file           app/ros_ws/src/detection/scripts/master.py
# @author         Pauline Odet && Antoine Passemard && Jules Graeff && Guillaume Bernard
# @license        ???

######################################################################################################################################################

from serial import *
import rospy
from std_msgs.msg import String, Float64, Bool
from detection.msg import Vide

######################################################################################################################################################

class Master:

    def __init__ (self):

        rospy.init_node('master', anonymous = True)
        rospy.loginfo('"master" node has been created')

        self.tick_rotation = 0.1
        self.mode = 'control'
        self.low_spong = False
        self.vide_detected = False
        self.spray_triggered = Fa

        rospy.Subscriber('/vide_detection', Vide, self._vide_detection_callback)
        rospy.Subscriber('/command_mode', String, self._command_mode_callback)
        rospy.Subscriber('/command_roues', String, self._command_roues_callback)
        rospy.Subscriber('/command_spray', Bool, self._command_spray_callback)
        rospy.Subscriber('/command_eponge', Bool, self._command_eponge_callback)

        self._pub_servo_bob_move = rospy.Publisher('/servo_bob_move', Vide, queue_size = 10)
        self._pub_sevo_bob_eponge = rospy.Publisher('/servo_bob_eponge', Vide, queue_size = 10)

        if self.mode == 'auto':
            rospy.loginfo('Bob is working in "auto" mode')

        elif self.mode == 'control':
            rospy.loginfo('Bob is working in "control" mode')

        else:
            raise ValueError('Issue with the mode value.')


    def _vide_detection_callback (self, data):

        self.vide_detected = bool(data.detected)
        rospy.loginfo("Vide Detection =" + str(self.vide_detected))

        # Generer un recul de plusieurs ticks

    def _command_mode_callback (self, data):

        self.mode = data.data
        rospy.loginfo("Mode sent via BLE = " + str(self.mode))

    def _command_roues_callback (self, data):

        self.roues_action = data.data
        rospy.loginfo("Command roues sent via BLE = " + str(self.roues_action))

        if self.mode == 'control' and not self.vide_detected:

            if self.roues_action == 'avant':

                # Publish on servo to drive front
                rospy.loginfo('avant')


            elif self.roues_action == 'arriere':

                # Publish on servo to drive back
                rospy.loginfo('arriere')


            elif self.roues_action == 'gauche':

                # Publish on servo to turn left of one tick
                rospy.loginfo('gauche')


            elif self.roues_action == 'droite':

                # Publish on servo to turn left of one tick
                rospy.loginfo('droite')


            else:
                raise ValueError('Issue with the roues action value.')


    def _command_spray_callback (self, data):

        self.spray_triggered = bool(data.data)

        rospy.loginfo("Command spray sent via BLE =" + str(spray_triggered))

        if self.mode == 'control' and not self.vide_detected:

            if self.spray_triggered:

                rospy.loginfo('spray_triggered')

                # TBD

    def _command_eponge_callback (self, data):

        assert self.low_spong != bool(data.data)

        self.low_spong = bool(data.data)
        rospy.loginfo("Command eponge low sent via BLE =" + str(self.low_spong))

        if self.mode == 'control' and not self.vide_detected:

            if self.low_spong:

                rospy.loginfo('low_spong')

                # Move low epong

            else:

                rospy.loginfo('high_spong')

                # Move high spong


######################################################################################################################################################

if __name__ == '__main__':
    master = Master()
    rospy.spin()

######################################################################################################################################################