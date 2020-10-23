#!/usr/bin/env python

#####################################################################################################################################################

# @project        https://gitlab.com/5eti_proto_2021/sujet_4__bob_le_nettoyage.git
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

class Esp32Connexion:

    def __init__ (self):

        rospy.init_node('esp32_connexion', anonymous = True)

        self._publisherVide = rospy.Publisher('/vide_detection', Vide, queue_size = 10)
        self._publisherMode = rospy.Publisher('/command_mode', String, queue_size = 10)
        self._publisherRoues = rospy.Publisher('/command_roues', String, queue_size = 10)
        self._publisherSpray = rospy.Publisher('/command_spray', Bool, queue_size = 10)
        self._publisherEponge = rospy.Publisher('/command_eponge', Bool, queue_size = 10)

        rospy.Subscriber('/send_to_esp32', String, self._sendToEsp32)

        self.port_serie = Serial('/dev/ttyUSB0', 115200 , timeout=1, writeTimeout = 1)

        if self.port_serie.isOpen():

            while not rospy.is_shutdown():

                try:
                    self._listen_esp32(self.port_serie)

                except rospy.ROSInterruptException:
                    break

            self.port_serie.close()

    def _sendToEsp32 (self, message):

        self.port_serie.write(message.data)


    def _listen_esp32 (self, port_serie):

        try:

            stringReceived = self.port_serie.readline().decode('utf-8').replace('\r', '').replace('\n', '')
            
            # CAPTEUR
            if stringReceived == 'CAPTEUR/table':
                self._publisherVide.publish(False)

            elif stringReceived == 'CAPTEUR/vide':
                self._publisherVide.publish(True)
 
            # MODES DE FONCTIONNEMENT
            elif stringReceived == 'BLE/auto':
            	self._publisherMode.publish("auto")

            elif stringReceived == 'BLE/control':
            	self._publisherMode.publish("control")

            # DEPLACEMENT ROUES
            elif stringReceived == 'BLE/avant':
            	self._publisherRoues.publish("avant")

            elif stringReceived == 'BLE/arriere':
                self._publisherRoues.publish("arriere")

            elif stringReceived == 'BLE/gauche':
                self._publisherRoues.publish("gauche")

            elif stringReceived == 'BLE/droite':
                self._publisherRoues.publish("droite")

            elif stringReceived == 'BLE/stop':
                self._publisherRoues.publish("stop")

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

######################################################################################################################################################
    
if __name__ == '__main__':

    get_send_message_esp32 = Esp32Connexion()
    rospy.spin()

######################################################################################################################################################
