#####################################################################################################################################################

# @project        https://gitlab.com/5eti_proto_2021/sujet_4__bob_le_nettoyage.git
# @file           app/ros_ws/src/detection/scripts/master.py
# @author         Pauline Odet && Antoine Passemard && Jules Graeff && Guillaume Bernard
# @license        ???

######################################################################################################################################################

from serial import *
import rospy
from std_msgs.msg import String, Float64
from detection.msg import Vide

######################################################################################################################################################

class Master:

    def __init__ (self):

        rospy.init_node('master', anonymous = True)
        rospy.loginfo('"master" node has been created')

        rospy.Subscriber('/vide_detection', Vide, self._vide_detection_callback)

        self._pub_servo_bob_move = rospy.Publisher('/servo_bob_move', Vide, queue_size = 10)
        self._pub_sevo_bob_eponge = rospy.Publisher('/sevo_bob_eponge', Vide, queue_size = 10)

        self.mode = 'Manual'

        self.tick_rotation = 0.1

        while True:

            if not self._vide_detected:

                if mode == 'Manual':

                    action = read_bluetooth()

                    if action == 'Avant':

                        # Publish on servo to drive front

                    elif action == 'Arriere':

                        # Publish on servo to drive back

                    elif action == 'Turn_Left':

                        # Publish on servo to turn left of one tick

                    elif action == 'Turn_Right':

                        # Publish on servo to turn left of one tick

            else:

                # Stop + security actions


    def _vide_detection_callback (self, data):

        self._vide_detected = bool(data.detected)

        rospy.loginfo(f"Vide Detection = {self._vide_detected}")

######################################################################################################################################################

if __name__ == '__main__':
    master = Master()
    rospy.spin()

######################################################################################################################################################