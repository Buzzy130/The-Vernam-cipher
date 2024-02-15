import random
import tkinter as tk
from tkinter import messagebox

def generate_key(length):
    key = ""
    for _ in range(length):
        key += random.choice(".,-")
    return key

def encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        char = message[i]
        key_char = key[i % len(key)]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        encrypted_message += encrypted_char
    return encrypted_message



def decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        key_char = key[i % len(key)]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        decrypted_message += decrypted_char
    return decrypted_message

def calculate_encrypt():
    message = weight_tf.get()
    key_length = len(message)
    key = generate_key(key_length)
    encrypted_message = encrypt(message, key)
    with open('encrypt.txt', 'a', encoding='utf-8') as f:
        f.truncate(0)
        data = encrypted_message
        f.write(data)
    with open('key.txt', 'a', encoding='utf-8') as f1:
        data1 = key
        f1.truncate(0)
        f1.write(data1)
    messagebox.showinfo('Зашифрованное сообщение', encrypted_message)
    messagebox.showinfo('Сгенерированный ключ', key)

def calculate_decrypt():
    encrypted_message = weight_tf.get()
    with open('key.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        key = data
    key = key
    decrypted_message = decrypt(encrypted_message, key)
    messagebox.showinfo('Расшифрованное сообщение', decrypted_message)


def copy_text():
    window.clipboard_clear()
    window.clipboard_append(weight_tf.get())

def paste_text():
    weight_tf.delete(0, tk.END)
    weight_tf.insert(tk.END, window.clipboard_get())

window = tk.Tk()
window.title('')
window.geometry('400x300')

frame = tk.Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

height_lb = tk.Label(
    frame,
    text="Введите сообщение  "
)
height_lb.grid(row=4, column=1)

weight_tf = tk.Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

cal_btn_encrypt = tk.Button(
    frame,
    text='Зашифровать',
    command=calculate_encrypt
)
cal_btn_encrypt.grid(row=5, column=2)

cal_btn_decrypt = tk.Button(
    frame,
    text='Расшифровать',
    command=calculate_decrypt
)
cal_btn_decrypt.grid(row=5, column=1)

copy_btn = tk.Button(
    frame,
    text='Копировать',
    command=copy_text
)
copy_btn.grid(row=6, column=1)

paste_btn = tk.Button(
    frame,
    text='Вставить',
    command=paste_text
)
paste_btn.grid(row=6, column=2)

window.mainloop()