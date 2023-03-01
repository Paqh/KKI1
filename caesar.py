# Fungsi untuk melakukan enkripsi dengan Caesar Cipher
def caesar_cipher(plaintext):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha() and char.isupper():
            # Shift 3 posisi ke kanan dalam alfabet
            shifted_char = chr((ord(char) - 65 + 3) % 26 + 65)
            ciphertext += shifted_char
        elif char.isalpha() and char.islower():
            if ord(char)<120 :
                ciphertext+=chr(ord(char)+3)
            else :
                shifted_char = chr(ord(char)%26 + 81)
                ciphertext+=shifted_char
        else :
            ciphertext+=char


    return ciphertext


# Contoh penggunaan
# plaintext = "Hello World"
# ciphertext = caesar_cipher(plaintext)
# print(ciphertext)

def decrypt_caesar(ciphertext):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha() and char.isupper():
            # Shift 3 posisi ke kanan dalam alfabet
            shifted_char = chr((ord(char) - 65 - 3) % 26 + 65)
            plaintext += shifted_char
        elif char.isalpha() and char.islower():
            if ord(char)>100 :
                plaintext+=chr(ord(char)-3)
            else :
                shifted_char = chr(ord(char)%26 + 81)
                plaintext+=shifted_char
        else :
            plaintext+=char


    return plaintext

# print(decrypt_caesar(ciphertext))