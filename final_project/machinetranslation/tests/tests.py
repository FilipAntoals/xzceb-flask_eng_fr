import unittest
from translator import english_to_french, french_to_english

class Test_englishToFrench(unittest.TestCase):
    def test_Noneinput(self):
        self.assertRaises(ValueError,english_to_french,None)

    def test_Frenchtranslation(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Hello'),'Hello')

class Test_frenchToEnglish(unittest.TestCase):
    def test_Englishtranslation(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')

    def test_Noneinput(self):
        self.assertRaises(ValueError,french_to_english,None)
        

unittest.main()