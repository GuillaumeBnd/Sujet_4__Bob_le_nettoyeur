
from serial import *
import rospy
from std_msgs.msg import String, Bool

class Master:

    def __init__(self):
        rospy.init_node('master', anonymous = True)
        rospy.loginfo('"master" node has been created')

        rospy.Subscriber('/vide_detection', Bool, self.callback)
     
    def callback(self, data):
        rospy.loginfo(f"Vide Detection = {data.data}")
    
if __name__ == '__main__':
    master = Master()
    rospy.spin()
    