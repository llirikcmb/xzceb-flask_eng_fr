import unittest
from translator import englishToFrench, frenchToEnglish


class TestEngToFr(unittest.TestCase): 
    
    def test_en_null(self): 
        self.assertEqual(englishToFrench(''), '') 

    def test_en_hello(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    
    def test_en_hello_reverse(self): 
        self.assertNotEqual(englishToFrench('Bonjour'), 'Hello')



class TestFrToEng(unittest.TestCase): 
    
    def test_fr_null(self): 
        self.assertEqual(frenchToEnglish(''), '') 

    def test_fr_hello(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    
    def test_fr_hello_reverse(self): 
        self.assertNotEqual(frenchToEnglish('Hello'), 'Bonjour')

unittest.main()
