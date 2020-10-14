#####################################################################################################################################################

# @project        https://gitlab.com/5eti_proto_2021/sujet_4__bob_le_nettoyage.git
# @file           app/ros_ws/src/detection/scripts/vide_detection.py
# @author         Pauline Odet && Antoine Passemard && Jules Graeff && Guillaume Bernard
# @license        ???

######################################################################################################################################################

from serial import *
import rospy
from std_msgs.msg import String
from detection.msg import Vide

######################################################################################################################################################

class VideDetection:

    def __init__ (self):

        rospy.init_node('vide_detection', anonymous = True)
        rospy.loginfo('"vide_detection" node has been created')

        self._publisher = rospy.Publisher('/vide_detection', Vide, queue_size = 10)

        with Serial(port = "/dev/ttyUSB0", baudrate = 9600, timeout = 1, writeTimeout = 1) as port_serie:
            
            if port_serie.isOpen():

                while not rospy.is_shutdown():

                    try:
                        self._listen_arduino_capteur(port_serie)

                    except rospy.ROSInterruptException:
                        break

    def _listen_arduino_capteur (self, port_serie):

        try:

            ligne = port_serie.readline().decode('utf-8').replace('\r', '').replace('\n', '')
                
            if ligne == 'Table':
                self._publisher.publish(False)

            elif ligne == 'Vide':
                self._publisher.publish(True)

            else:
                rospy.logwarn('There is a problem.')

        except UnicodeDecodeError as e:
            
            rospy.logwarn('UnicodeDecodeError')
            pass

######################################################################################################################################################
    
if __name__ == '__main__':

    vide_detection = VideDetection()
    rospy.spin()

######################################################################################################################################################
    