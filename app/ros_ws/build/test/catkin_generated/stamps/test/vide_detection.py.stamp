
from serial import *
import rospy
from std_msgs.msg import String, Bool

class VideDetection:

    def __init__(self):

        self.frequence = 1

        rospy.init_node('vide_detection', anonymous = True)
        rospy.loginfo('"vide_detection" node has been created')

        self._publisher = rospy.Publisher('/vide_detection', Bool, queue_size = 10)

        with Serial(port = "/dev/ttyUSB0", baudrate = 9600, timeout = 1, writeTimeout = 1) as port_serie:
            
            if port_serie.isOpen():

                while not rospy.is_shutdown():

                    try:
                        self.listen_arduino_capteur(port_serie)

                    except rospy.ROSInterruptException:
                        break

    def listen_arduino_capteur (self, port_serie):

        try:

            ligne = port_serie.readline().decode('utf-8').replace('\r', '').replace('\n', '')
            print(f'*{ligne}*')
                
            if ligne == 'Table':
                self._publisher.publish(False)

            elif ligne == 'Vide':
                self._publisher.publish(True)

            else:
                print('There is a problem.')

        except UnicodeDecodeError as e:
            
            print('UnicodeDecodeError')
            pass
    
if __name__ == '__main__':

    vide_detection = VideDetection()
    rospy.spin()
    