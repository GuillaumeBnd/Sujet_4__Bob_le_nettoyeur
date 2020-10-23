#!/usr/bin/env python

#####################################################################################################################################################

# @project        https://gitlab.com/5eti_proto_2021/sujet_4__bob_le_nettoyage.git
# @file           app/ros_ws/src/detection/scripts/master.py
# @author         Pauline Odet && Antoine Passemard && Jules Graeff && Guillaume Bernard
# @license        ???

######################################################################################################################################################

import rospy
from std_msgs.msg import String, Float64, Bool
from detection.msg import Vide

from dynamixel_msgs.msg import MotorStateList

######################################################################################################################################################

class Master:

    def __init__ (self):

        rospy.init_node('master', anonymous = True)
        rospy.loginfo('"master" node has been created')

        self.speed_translation = 7
        self.speed_rotation = 5.5

        self.mode = 'control'
        self.low_spong = False
        self.vide_detected = False
        self.spray_triggered = False

        self.sens_normal = True

        rospy.Subscriber('/vide_detection', Vide, self._vide_detection_callback)
        rospy.Subscriber('/command_mode', String, self._command_mode_callback)
        rospy.Subscriber('/command_roues', String, self._command_roues_callback)
        rospy.Subscriber('/command_spray', Bool, self._command_spray_callback)
        rospy.Subscriber('/command_eponge', Bool, self._command_eponge_callback)

        self._speed_roue_gauche = rospy.Publisher('/joint1_controller/command', Float64, queue_size = 10)
        self._speed_roue_droite = rospy.Publisher('/joint2_controller/command', Float64, queue_size = 10)
        self._speed_deux_roues = rospy.Publisher('/dual_motor_controller/command', Float64, queue_size = 10)
        self._position_eponge = rospy.Publisher('/joint3_controller/command', Float64, queue_size = 10)

        self._spray = rospy.Publisher('/send_to_esp32', String, queue_size = 10)

        if self.mode == 'auto':
            rospy.loginfo('Bob is working in "auto" mode')

        elif self.mode == 'control':
            rospy.loginfo('Bob is working in "control" mode')

        else:
            raise ValueError('Issue with the mode value.')

        rate = rospy.Rate(10) # 10hz

        while not rospy.is_shutdown():

            while self.mode == 'auto':

                rospy.loginfo('"Auto" mode')

                self.low_spong = True
                self.command_eponge()

                # Cycle de nettoyage en ligne droite avant d'atteindre le bord de la table

                while not self.vide_detected:

                    self.roues_stop()

                    self.spray_triggered = True
                    self.command_spray()
                    rospy.sleep(2)     # duration of the spray
                    
                    self.spray_triggered = False

                    self.roues_avant()

                    # j'avance durant une seconde
                    for i in range (0, 10):

                        rospy.sleep(0.1)

                        if self.vide_detected:

                            self.roues_stop()
                            break

                self.roues_arriere()

                rospy.sleep(2)

                self.roues_stop()

                # Demi tour (surement lever l'eponge)
                if self.sens_normal:

                    self.roues_gauche()
                    self.roues_avant()
                    rospy.sleep(0.5)
                    self.roues_stop()
                    self.roues_gauche()

                if not self.sens_normal:

                    self.roues_droite()
                    self.roues_droite()
                
                self.sens_normal = not self.sens_normal

            rate.sleep()

    def _vide_detection_callback (self, data):

        self.vide_detected = bool(data.detected)
        rospy.loginfo("Vide Detection = " + str(self.vide_detected))

        if self.vide_detected:
            self.roues_stop()

    def _command_mode_callback (self, data):

        self.mode = data.data
        rospy.loginfo("Mode sent via BLE = " + str(self.mode))

    def _command_roues_callback (self, data):

        self.roues_action = data.data
        rospy.loginfo("Command roues sent via BLE = " + str(self.roues_action))

        if self.mode == 'control' and not self.vide_detected:

            if self.roues_action == 'avant':
                self.roues_avant()

            elif self.roues_action == 'arriere':
                self.roues_arriere()

            elif self.roues_action == 'gauche':
                self.roues_gauche()

            elif self.roues_action == 'droite':
                self.roues_droite()

            elif self.roues_action == 'stop':
                self.roues_stop()

            else:
                raise ValueError('Issue with the roues action value.')

    def _command_spray_callback (self, data):

        self.spray_triggered = bool(data.data)

        rospy.loginfo("Command spray sent via BLE =" + str(self.spray_triggered))

    def _command_eponge_callback (self, data):

       # assert self.low_spong != bool(data.data)

        self.low_spong = bool(data.data)
        rospy.loginfo("Command eponge low sent via BLE =" + str(self.low_spong))

        if self.mode == 'control':

            self.command_eponge()

    def roues_avant (self):

        rospy.loginfo('avant')
        self._speed_deux_roues.publish( - self.speed_translation)

    def roues_arriere (self):

        rospy.loginfo('avant')
        self._speed_deux_roues.publish(self.speed_translation)

    def roues_gauche (self):

        rospy.loginfo('gauche')

        self._speed_roue_gauche.publish(-self.speed_rotation)
        self._speed_roue_droite.publish(-self.speed_rotation)

        rospy.sleep(2)

        self.roues_stop()

    def roues_droite (self):

        rospy.loginfo('droite')

        self._speed_roue_gauche.publish(self.speed_rotation)
        self._speed_roue_droite.publish(self.speed_rotation)

        rospy.sleep(2)

        self.roues_stop()

    def roues_stop (self):

        self._speed_deux_roues.publish(0)

    def command_eponge (self):

        if self.low_spong:

            rospy.loginfo('low_spong')
            self._position_eponge.publish(0.3)

        else:

            rospy.loginfo('high_spong')
            self._position_eponge.publish(0.8)

    # WARNING : we need to stop the robot when spray because no sensore info can be fetch.

    def command_spray (self):

        if self.spray_triggered:

            self._spray.publish("AUTO/spray")
            rospy.loginfo('spray_triggered')

######################################################################################################################################################

if __name__ == '__main__':
    master = Master()
    rospy.spin()

######################################################################################################################################################
