class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26  # Ensure the shift is always between 0 and 25
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def _shift_alphabet(self):
        # Adjust the shift to wrap around alphabet
        shifted_alphabet = self.alphabet[self.shift:] + self.alphabet[:self.shift]
        return dict(zip(self.alphabet, shifted_alphabet))

    def encrypt(self, plaintext):
        shifted_alphabet = self._shift_alphabet()
        encrypted = []
        
        for char in plaintext.upper():
            if char in self.alphabet:
                encrypted.append(shifted_alphabet[char])
            else:
                encrypted.append(char)  # preserve spaces and punctuation
        
        return ''.join(encrypted)

    def decrypt(self, ciphertext):
        shifted_alphabet = self._shift_alphabet()
        reverse_shifted_alphabet = {v: k for k, v in shifted_alphabet.items()}
        decrypted = []
        
        for char in ciphertext.upper():
            if char in self.alphabet:
                decrypted.append(reverse_shifted_alphabet[char])
            else:
                decrypted.append(char)  # preserve spaces and punctuation
        
        return ''.join(decrypted)
