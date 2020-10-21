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

class SendMessageEsp32:

    def __init__ (self):

        rospy.init_node('send_message_to_esp32', anonymous = True)

        rospy.Subscriber('/send_to_esp32', String, self._sendToEsp32)
        self.port_serie = serial.Serial(port = "/dev/ttyUSB0", baudrate = 115200, timeout = 1, writeTimeout = 1)




    def _sendToEsp32(self,message):
       

   
        if port_serie.isOpen():

            try:
                port_serie.write(message)
             
                  

            except rospy.ROSInterruptException:
                break






    





######################################################################################################################################################
    
if __name__ == '__main__':

    sendMessageEsp32 = SendMessageEsp32()
    rospy.spin()

######################################################################################################################################################
    