
from serial import *
import rospy
from std_msgs.msg import String, Bool

class VideDetection:

    def __init__(self):

        self.frequence = 1

        rospy.init_node('vide_detection', anonymous = True)
        rospy.loginfo('"vide_detection" node has been created')

        # rospy.Subscriber('/vide_detection', String, self.callback)

        self._publisher = rospy.Publisher('/vide_detection', Bool, queue_size = 10)

        rate = rospy.Rate(self.frequence) # 10hz

        while not rospy.is_shutdown():

            self.listen_arduino_capteur()
            rate.sleep()

    def callback(self, data):
        rospy.loginfo(f"data received from the sender: {data}")

    def listen_arduino_capteur (self):

        with Serial(port = "/dev/ttyUSB0", baudrate = 9600, timeout = 1, writeTimeout = 1) as port_serie:
            
            if port_serie.isOpen():
                
                while True:

                    ligne = str(port_serie.readline())
                    print(ligne)
                    
                    if ligne == 'La table est détéctée.':
                        self._publisher.publish(False)

                    elif ligne == 'Attention vide.':
                        self._publisher.publish(True)

                    else:
                        print('There is a problem.')

                    port_serie.write(data.data.encode('utf-8'))
    
if __name__ == '__main__':

    vide_detection = VideDetection()
    rospy.spin()
    