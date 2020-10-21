#!/usr/bin/env python2

#####################################################################################################################################################

# @project        https:# gitlab.com/5eti_proto_2021/sujet_4__bob_le_nettoyage.git
# @file           app/ros_ws/src/detection/scripts/vide_detection.py
# @author         Pauline Odet && Antoine Passemard && Jules Graeff && Guillaume Bernard
# @license        ???

######################################################################################################################################################

from serial import *
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
from detection.msg import Vide

######################################################################################################################################################

class GetMessageEsp32:

    def __init__ (self):

        rospy.init_node('get_message_from_esp32', anonymous = True)
        rospy.loginfo('"get_message_from_esp32" node has been created')

        self._publisherVide = rospy.Publisher('/vide_detection', Vide, queue_size = 10)
        self._publisherMode = rospy.Publisher('/command_mode', String, queue_size = 10)
        self._publisherRoues = rospy.Publisher('/command_roues', String, queue_size = 10)
        self._publisherSpray = rospy.Publisher('/command_spray', Bool, queue_size = 10)
        self._publisherEponge = rospy.Publisher('/command_eponge', Bool, queue_size = 10)

        with Serial(port = "/dev/ttyUSB0", baudrate = 115200, timeout = 1, writeTimeout = 1) as port_serie:
            
            if port_serie.isOpen():

                while not rospy.is_shutdown():

                    try:
                        self._listen_esp32(port_serie)

                    except rospy.ROSInterruptException:
                        break

    def _listen_esp32 (self, port_serie):

        try:

            receiv = port_serie.readline()
            # print(receiv)
            stringReceived = receiv.decode('utf-8').replace('\r', '').replace('\n', '')
                
            # CAPTEUR
            if stringReceived == 'CAPTEUR/table':
                self._publisherVide.publish(False)

            elif stringReceived == 'CAPTEUR/vide':
                self._publisherVide.publish(True)

            # MODE
            elif stringReceived == 'BLE/auto':
            	self._publisherMode.publish("auto")

            elif stringReceived == 'BLE/control':
            	self._publisherMode.publish("control")

            # ROUES
            elif stringReceived == 'BLE/avant':
                self._publisherRoues.publish("avant")

            elif stringReceived == 'BLE/arriere':
                self._publisherRoues.publish("arriere")
            
            elif stringReceived == 'BLE/gauche':
                self._publisherRoues.publish("gauche")
			
            elif stringReceived == 'BLE/droite':
                self._publisherRoues.publish("droite")

            # SPRAY
            elif stringReceived == 'BLE/spray':
                self._publisherSpray.publish(True)

		   	# EPONGE
            elif stringReceived == 'BLE/epongebas':
                self._publisherEponge.publish(True)

            elif stringReceived == 'BLE/epongehaut':
                self._publisherEponge.publish(False)

            else:

                if len(stringReceived) != 0:
                    rospy.logwarn('There is a problem. Data (type ' + str(type(stringReceived)) + ') <' + str(stringReceived) + '>')
                    rospy.logwarn(stringReceived == 'BLE/control')

        except UnicodeDecodeError as e:
            
            rospy.logwarn('UnicodeDecodeError')
            pass

        except Exception as e:
            rospy.logwarn(str(e))
            pass


######################################################################################################################################################
    
if __name__ == '__main__':

    get_message_from_esp32 = GetMessageEsp32()
    rospy.spin()

######################################################################################################################################################
    