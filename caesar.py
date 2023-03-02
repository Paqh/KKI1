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


# def decrypt_caesar(ciphertext):
#     plaintext = ""
#     for char in ciphertext:
#         if char.isalpha() and char.isupper():
#             # Shift 3 posisi ke kanan dalam alfabet
#             shifted_char = chr((ord(char) - 65 - 3) % 26 + 65)
#             plaintext += shifted_char
#         elif char.isalpha() and char.islower()  and ord(char)>97:
#             shifted_char = chr((ord(char) - 97 - 3) % 26 + 97)
#         else :
#             plaintext+=char
#     return plaintext

def decrypt_caesar(ciphertext):
    plaintext = ''
    for char in ciphertext:
        if char.islower():
            # memindahkan huruf kecil dengan jumlah shift 3
            # memutari alphabet menggunakan modulo
            char = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
        elif char.isupper():
            # memindahkan huruf kapital dengan jumlah shift 3
            char = chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
        plaintext += char
    return plaintext



# Contoh penggunaan
# ciphertext = "Hello World"
# print(ciphertext)
# a = caesar_cipher(ciphertext)
# print(a)
# print(decrypt_caesar(a))
# print(decrypt_caesar(ciphertext))