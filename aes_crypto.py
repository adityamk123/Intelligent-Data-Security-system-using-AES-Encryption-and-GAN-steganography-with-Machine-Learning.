from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

class AESCipher:
    def __init__(self, key=None):
        self.key = key or os.urandom(16)  # 128-bit key
        self.iv = os.urandom(16)

    def encrypt(self, plaintext: str) -> bytes:
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(self.iv))
        encryptor = cipher.encryptor()
        return encryptor.update(plaintext.encode()) + encryptor.finalize()

    def decrypt(self, ciphertext: bytes) -> str:
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(self.iv))
        decryptor = cipher.decryptor()
        return (decryptor.update(ciphertext) + decryptor.finalize()).decode()
