# Module de lecture/ecriture du port série
from serial import *
# Port série ttyACM0
# Vitesse de baud : 9600
# Timeout en lecture : 1 sec
# Timeout en écriture : 1 sec

with Serial(port = "/dev/ttyUSB0", baudrate = 9600, timeout = 1, writeTimeout = 1) as port_serie:
    
    if port_serie.isOpen():
        
        while True:
            ligne = port_serie.readline()
            print(str(ligne))

            port_serie.write("C'est Python qui parle".encode('utf-8'))