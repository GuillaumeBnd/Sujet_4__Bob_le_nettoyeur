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

class GetMessageEsp32:

    def __init__ (self):

        rospy.init_node('get_message_from_esp32', anonymous = True)
        //rospy.loginfo('"vide_detection" node has been created')

        self._publisherVide = rospy.Publisher('/vide_detection', Vide, queue_size = 10)
        self._publisherMode = rospy.Publisher('/command_mode', String, queue_size = 10)
        self._publisherRoues = rospy.Publisher('/command_roues', String, queue_size = 10)
        self._publisherSpray = rospy.Publisher('/command_spray', Bool, queue_size = 10)
        self._publisherEponge = rospy.Publisher('/command_eponge', Bool, queue_size = 10)

        rospy.Subscriber('/send_to_esp32', String, self._sendToEsp32)


        self.port_serie = serial.Serial('/dev/ttyUSB0', 115200 , timeout=1, writeTimeout = 1)
        if self.port_serie.isOpen():

                while not rospy.is_shutdown():

                    try:
                        self._listen_esp32(self.port_serie)

                    except rospy.ROSInterruptException:
                        break

        """
        with Serial(port = "/dev/ttyUSB0", baudrate = 115200, timeout = 1, writeTimeout = 1) as port_serie:
            
            if port_serie.isOpen():

                while not rospy.is_shutdown():

                    try:
                        self._listen_esp32(port_serie)

                    except rospy.ROSInterruptException:
                        break
        """

    def _sendToEsp32(self,message):
        self.port_serie.write(message)


    def _listen_esp32 (self, port_serie):

        try:

            stringReceived = self.port_serie.readline().decode('utf-8').replace('\r', '').replace('\n', '')
                
            //CAPTEUR
            if stringReceived == 'CAPTEUR/table':
                self._publisherVide.publish(False)

            elif stringReceived == 'CAPTEUR/vide':
                self._publisherVide.publish(True)


            //MODE
            elif stringReceived == 'BLE/auto':
            	self._publisherMode.publish("auto")

            elif stringReceived == 'BLE/control':
            	self._publisherMode.publish("control")

            //ROUES
            elif stringReceived == 'BLE/avant':
            	self._publisherRoues.publish("avant")

			elif stringReceived == 'BLE/arriere':
				self._publisherRoues.publish("arriere")

			elif stringReceived == 'BLE/gauche':
				self._publisherRoues.publish("gauche")
			
			elif stringReceived == 'BLE/droite':
				self._publisherRoues.publish("droite")

			//SPRAY : juste a titre informatif, car c'est l'esp32 qui gère la pompe
		    elif stringReceived == 'BLE/spray':
		    	self._publisherSpray.publish(True) 


		   	//EPONGE ! En mode auto, l'eponge dois descendre automatiquement après 2/3 secondes de spray
		    elif stringReceived == 'BLE/epongebas':
		    	self._publisherEponge.publish(True)

		    elif stringReceived == 'BLE/epongehaut':
		    	self._publisherEponge.publish(False)


            else:
                rospy.logwarn('string venant de BLE non recevable')

        except UnicodeDecodeError as e:
            
            rospy.logwarn('UnicodeDecodeError')
            pass





######################################################################################################################################################
    
if __name__ == '__main__':

    getMessageEsp32 = GetMessageEsp32()
    rospy.spin()

######################################################################################################################################################
