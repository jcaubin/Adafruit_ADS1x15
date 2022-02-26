#pruebas del adafruit

from time import sleep
import Adafruit_ADS1x15 as adf

ADS1015 = 0x00  
ADS1115 = 0x01 

ads = adf.ADS1x15(address=0x48, ic=ADS1115)

def readData():
    d= ads.readADCSingleEnded()
    print(f"v: {d/1000}", end='\r')


def loop():
    while True:
        readData()
        sleep(0.5)

if __name__ == '__main__':     # Program start from here
	try:
		loop()
	except KeyboardInterrupt:  # 
		print('fin')

