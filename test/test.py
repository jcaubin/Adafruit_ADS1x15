#ruta para el paquete
import sys
sys.path.append('.')

import unittest
import logging
from ADS1x15.Adafruit_ADS1x15 import ADS1x15

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
ADS1015 = 0x00  
ADS1115 = 0x01 


class TestADS(unittest.TestCase):
    def test_readADCSingleEnded(self):
        """
        Test lectura puntual dentro de rango
        """
        ads = ADS1x15(address=0x48, ic=ADS1115)
        result = ads.readADCSingleEnded()/1000
        self.assertGreater(result, -1.0)
        self.assertLessEqual(result, 5.5)



if __name__ == '__main__':
    unittest.main()