#####################################################################################################################################################

# @project        https://gitlab.com/5eti_proto_2021/sujet_4__bob_le_nettoyage.git
# @file           app/ros_ws/src/detection/scripts/master.py
# @author         Pauline Odet && Antoine Passemard && Jules Graeff && Guillaume Bernard
# @license        ???

######################################################################################################################################################

from serial import *
import rospy
from std_msgs.msg import String
from detection.msg import Vide

######################################################################################################################################################

class Master:

    def __init__ (self):

        rospy.init_node('master', anonymous = True)
        rospy.loginfo('"master" node has been created')

        rospy.Subscriber('/vide_detection', Vide, self._vide_detection_callback)
        rospy.Subscriber('/command_mode', String, self._command_mode_callback)
        rospy.Subscriber('/command_roues', String, self._command_roues_callback)
        rospy.Subscriber('/command_spray', Bool, self._command_command_spray_callback)
        rospy.Subscriber('/command_eponge', Bool, self._command_command_eponge_callback)

        if self._mode == 'auto':
            pass

        elif self._mode == 'control':
            pass

        else:
            raise Exception('Issue with the mode value.')


    def _vide_detection_callback (self, data):

        rospy.loginfo(f"Vide Detection = {bool(data.detected)}")

    def _command_mode_callback (self, data):

        self._mode = data.data
        rospy.loginfo(f"Command sent via BLE = {bool(data.data)}")

######################################################################################################################################################

if __name__ == '__main__':
    master = Master()
    rospy.spin()

######################################################################################################################################################