import sys
import time
sys.path.insert(0, '..')

from p2psecure.securenode import SecureNode

node1 = SecureNode("localhost", 10001)

plaintext = b"Hoi daar!"
ciphertext = node1.encrypt_aes(plaintext, b"this is the key1")

print(plaintext)
print(ciphertext)
print(node1.decrypt_aes(ciphertext, b"this is the key1"))

print("End")