#pruebas del adafruit

#ruta para el paquete
import sys
sys.path.append('.')

from time import sleep
from ADS1x15.Adafruit_ADS1x15 import ADS1x15
import logging
logging.basicConfig(level=logging.ERROR)

logger = logging.getLogger(__name__)

ADS1015 = 0x00  
ADS1115 = 0x01 

ads = ADS1x15(address=0x48, ic=ADS1115)

def readData():
    d= ads.readADCSingleEnded()
    print(f"v: {d/1000}", end='\r')


def loop():
    while True:

        
        readData()
        sleep(0.2)

if __name__ == '__main__':     # Program start from here
	try:
		loop()
	except KeyboardInterrupt:  # 
		print('fin')

