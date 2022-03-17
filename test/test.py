#ruta para el paquete
import sys
sys.path.append('.')

import unittest
from unittest.mock import Mock, MagicMock, patch
import logging
from ADS1x15.Adafruit_ADS1x15 import ADS1x15

logging.basicConfig(level=logging.DEBUG)
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

    def test_reasADCDiferential(self):
        """
        Test de lectura diferencial
        """
        self.assertTrue(True, "no implementado")

    def test_readADCSingleEndedMock_0(self):
        """
        Test lectura puntual dentro de rango con mock
        """
        mock = Mock()
        mock.readList.return_value = [0, 0] #valor devuento por i2c

        ads = ADS1x15(address=0x48, ic=ADS1115, i2c=mock)
        result = ads.readADCSingleEnded()/1000
        self.assertEqual(result, 0.0)
    
    def test_readADCSingleEndedMock_5(self):
        """
        Test lectura puntual dentro de rango con mock
        """
        mock = Mock()
        mock.readList.return_value = [104, 43] #valor devuento por i2c

        ads = ADS1x15(address=0x48, ic=ADS1115, i2c=mock)
        result = ads.readADCSingleEnded()/1000
        self.assertAlmostEqual(result, 5.0, delta=0.001)

    # @patch('ADS1x15.Adafruit_I2C' )
    # def test_readADCSingleEndedMockPatch(self,mockI2c):
    #     """
    #     Test lectura puntual dentro de rango con mock
    #     """
    #     mockI2c.readList.return_value = [0, 0] #valor devuento por i2c
    #     ads = ADS1x15(address=0x48, ic=ADS1115)
     
    #     result = ads.readADCSingleEnded()/1000
    #     self.assertEqual(result, 0.0)




if __name__ == '__main__':
    unittest.main()