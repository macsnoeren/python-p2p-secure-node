import sys
import time
sys.path.insert(0, '..')

from p2psecure.securenode import SecureNode

node1 = SecureNode("localhost", 10001)

#node1.encrypt_aes_file_pw("test.enc", b"Hallo Maurice Snoeren", b"password123")
print(node1.decrypt_aes_file_pw("test.enc", b"password123"))

plaintext = b"Hoi daar!"
ciphertext = node1.encrypt_aes_pw(plaintext, b"this is the passwd")

print("PLAIN: ", plaintext)
print("CIPHER: ", ciphertext)
print(node1.decrypt_aes_pw(ciphertext, b"this is the passwd"))

print("End")