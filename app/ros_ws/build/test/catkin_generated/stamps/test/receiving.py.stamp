
from serial import *
import rospy
from std_msgs.msg import String

class Receiving:

    def __init__(self):
        rospy.init_node('receiving', anonymous = True)
        rospy.loginfo('"receiving" node has been created')

        rospy.Subscriber('/remotepub', String, self.callback)
     
    def callback(self, data):
        rospy.loginfo(f"data received from the sender: {data}")

        with Serial(port = "/dev/ttyUSB0", baudrate = 9600, timeout = 1, writeTimeout = 1) as port_serie:
            
            if port_serie.isOpen():
                
                while True:
                    ligne = port_serie.readline()
                    print(str(ligne))

                    port_serie.write(data.data.encode('utf-8'))
    
if __name__ == '__main__':
    receiver = Receiving()
    rospy.spin()
    