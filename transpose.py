def encrypt_transpose(plaintext, key):
    # Hilangkan karakter spasi dari plaintext
    plaintext = plaintext.replace(" ", "")
   
    # Hitung panjang pesan dan kunci
    n_plaintext = len(plaintext)
    n_key = len(key)
   
    # Tambahkan karakter padding "x" jika panjang pesan tidak habis dibagi oleh panjang kunci
    if n_plaintext % n_key != 0:
        num_padding = n_key - (n_plaintext % n_key)
        plaintext += "x" * num_padding
        n_plaintext += num_padding
   
    # Hitung jumlah baris tabel grid
    n_row = n_plaintext // n_key
   
    # Inisialisasi tabel grid dengan karakter "-1"
    grid = [["-1" for j in range(n_key)] for i in range(n_row)]
   
    # Isi tabel grid dengan karakter-karakter pesan
    for i in range(n_row):
        for j in range(n_key):
            grid[i][j] = plaintext[(i * n_key) + j]
   
    # Susun indeks kolom dalam urutan alfabetis berdasarkan karakter-karakter pada kunci
    sorted_key = "".join(sorted(key))
    col_indices = [key.index(sorted_key[i]) for i in range(n_key)]
   
    # Baca tabel grid dari atas ke bawah dengan urutan indeks kolom yang telah diurutkan
    ciphertext = ""
    for i in range(n_key):
        for j in range(n_row):
            ciphertext += grid[j][col_indices[i]]
        # Tambahkan spasi pada setiap kelompok huruf sesuai dengan panjang kunci
    text=''
    for i,j in enumerate(ciphertext) :
        if (i+1)%(n_row) == 0 :
            text+=j
            text+=" "
           
        else :
            text+=j
    return text

# plaintext = "Hello World"
# key = "UGM"
# ciphertext = encrypt_transpose(plaintext, key)
# print(ciphertext)

def decrypt_transpose(ciphertext, key):
    # Hilangkan karakter spasi dari ciphertext
    ciphertext = ciphertext.replace(" ", "")
   
    # Hitung panjang pesan dan kunci
    n_ciphertext = len(ciphertext)
    n_key = len(key)
   
    # Hitung jumlah baris tabel grid
    n_row = n_ciphertext // n_key
   
    # Inisialisasi tabel grid dengan karakter "-1"
    grid = [["-1" for j in range(n_key)] for i in range(n_row)]
   
    # Susun indeks kolom dalam urutan alfabetis berdasarkan karakter-karakter pada kunci
    sorted_key = "".join(sorted(key))
    col_indices = [key.index(sorted_key[i]) for i in range(n_key)]
   
    # Isi tabel grid dengan karakter-karakter pesan
    for i in range(n_key):
        for j in range(n_row):
            grid[j][col_indices[i]] = ciphertext[(i * n_row) + j]
   
    # Baca tabel grid dari atas ke bawah
    plaintext = ""
    for i in range(n_row):
        for j in range(n_key):
            plaintext += grid[i][j]
   
    # Hilangkan karakter padding "x" jika ada
    plaintext = plaintext.replace("x", "")
   
    return plaintext

# def decrypt_transpose(ciphertext, key):
#     # Determine the number of rows and columns in the grid
#     num_cols = len(ciphertext) // len(key)
#     num_rows = len(key)

#     # Check if there is an incomplete row at the bottom of the grid
#     if len(ciphertext) % len(key) != 0:
#         num_cols += 1

#     # Create the grid
#     grid = [[''] * num_cols for _ in range(num_rows)]

#     # Populate the grid with the ciphertext
#     index = 0
#     for col in range(num_cols):
#         for row in range(num_rows):
#             if index < len(ciphertext):
#                 grid[row][col] = ciphertext[index]
#                 index += 1

#     # Determine the order in which to read the columns based on the key
#     column_order = [0] * num_cols
#     for i in range(num_cols):
#         column_order[i] = key.index(str(i % num_rows))

#     # Read the plaintext from the grid
#     plaintext = ''
#     for row in range(num_rows):
#         for col in range(num_cols):
#             plaintext += grid[row][column_order[col]]

#     return plaintext


# print(decrypt_transpose(ciphertext, key))