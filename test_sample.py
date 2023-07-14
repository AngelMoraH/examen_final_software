import unittest
from routes import get_contactos,get_historial,pagar

class Test(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_get_contactos(self):
        self.assertEqual(get_contactos("918273475"),{"contactos": ["456789123:Jean"] })
        self.assertNotEqual(get_contactos("456789123"),{"contactos": [] })
    
    def test_failed_get_contactos(self):
        self.assertEqual(get_contactos("123456789"),None)
        self.assertEqual(get_contactos(),{"message": "Faltan datos"})
    
    def test_failed_pagar(self):
        self.assertEqual(pagar(minumero="12312312312351263",numerodestino="123123",valor=134.84),{"mensaje":"Operacion no realizada"})
        self.assertEqual(pagar(),{"message": "Faltan datos"})
    
    def test_failed_get_historial(self):
        self.assertEqual(get_historial(),{"message": "Faltan datos"})
        self.assertEqual(get_historial("123123123123123"),{"message": "cuenta no encontrada"})
        
    
    def tearDown(self) -> None:
        return super().tearDown()
        
        

