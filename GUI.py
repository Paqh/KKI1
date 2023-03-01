import tkinter as KKI
from mixed import mixed
from mixed import decrypt_mixed

# Create a window
window = KKI.Tk()

# Add a label
label = KKI.Label(window, text="Enter text and key then choose:")
label.pack()
# Add a label


# Add a text input field
text_input = KKI.Entry(window)
key_input = KKI.Entry(window)
text_input.pack()
key_input.pack()

# Function to display the input text
def display_encrypt_text():
    input_text = text_input.get()
    input_key = key_input.get()
    encrypted = mixed(input_text, input_key)
    display_label.config(text="encrypted: " + encrypted)

def display_decrypt_text():
    input_text = text_input.get()
    input_key = key_input.get()
    decrypted = decrypt_mixed(input_text, input_key)
    display_label.config(text="decrypted: " + decrypted)

# Add a submit button
encrypt_button = KKI.Button(window, text="encrypt", command=display_encrypt_text)
decrypt_button = KKI.Button(window, text="decrypt", command=display_decrypt_text)
encrypt_button.pack()
decrypt_button.pack()

# Add a label to display the input text
display_label = KKI.Label(window)
display_label.pack()

# Run the window
window.mainloop()
