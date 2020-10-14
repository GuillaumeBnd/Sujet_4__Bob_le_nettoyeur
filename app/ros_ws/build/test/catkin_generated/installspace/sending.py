import rospy
from std_msgs.msg import String

class Sending :

    def __init__(self):
        rospy.init_node('sending', anonymous = True)
        rospy.loginfo('"sending" node has been created')

        self.pub_remote = rospy.Publisher('/remotepub', String, queue_size = 10)
    
        rate = rospy.Rate(1) # 10hz

        while not rospy.is_shutdown():
            self.pub_remote.publish("test")
            rate.sleep()

if __name__ == '__main__':
    c = Sending()
    rospy.spin()
    