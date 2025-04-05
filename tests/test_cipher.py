# test_cipher.py

import unittest
from cipher.cipher import CaesarCipher

class TestCaesarCipher(unittest.TestCase):
    
    def setUp(self):
        self.cipher = CaesarCipher(3)  # Creating a CaesarCipher object with a shift of 3
    
    def test_encryption(self):
        encrypted = self.cipher.encrypt("Hello World!")
        self.assertEqual(encrypted, "KHOOR ZRUOG!")
    
    def test_decryption(self):
        decrypted = self.cipher.decrypt("KHOOR ZRUOG!")
        self.assertEqual(decrypted, "HELLO WORLD!")
    
    def test_preserve_non_alpha(self):
        encrypted = self.cipher.encrypt("Hello, World?")
        self.assertEqual(encrypted, "KHOOR, ZRUOG?")
    
    def test_no_shift(self):
        cipher_no_shift = CaesarCipher(0)  # Shift by 0 (no change)
        self.assertEqual(cipher_no_shift.encrypt("Hello World!"), "HELLO WORLD!")
    
    def test_large_shift(self):
        cipher_large_shift = CaesarCipher(29)  # Same as shift by 3 (29 % 26 = 3)
        self.assertEqual(cipher_large_shift.encrypt("Hello World!"), "KHOOR ZRUOG!")

if __name__ == "__main__":
    unittest.main()
