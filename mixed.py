from caesar import caesar_cipher
from transpose import encrypt_transpose

def mixed(plaintext,key) :
    cipher=caesar_cipher(plaintext)
    transpose=encrypt_transpose(cipher,key)
    return transpose

# plaintext="Hello World"
# key="UGM"
# a=mixed(plaintext,key)

from caesar import decrypt_caesar
from transpose import decrypt_transpose

def decrypt_mixed(ciphertext,key) :
    cipher=decrypt_transpose(ciphertext,key)
    plaintext=decrypt_caesar(cipher)
    return plaintext

# key="UGM"
# print(decrypt_mixed(a,key))
