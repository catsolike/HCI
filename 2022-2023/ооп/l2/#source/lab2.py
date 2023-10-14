import tkinter as tk
from random import randint
import sys, os
import ast
from tkinter import messagebox

# ПРИВЯЗЫВАЕТ К КЛЮЧУ РАНДОМНОЕ ЧИСЛО (СОЗДАЁТ ДОП ФАЙЛ)

window = tk.Tk()
window.geometry("450x350")
window.title("Encryption")


# Entries
entryEncryptPhrase = tk.Entry(window)
entryDecryptPhrase = tk.Entry(window)
entryKey = tk.Entry(window)

entryEncryptPhrase.grid(row=1, column=0, sticky='N')
entryDecryptPhrase.grid(row=1, column=1, padx=70)
entryKey.grid(row=3, column=1, padx=70)

# Labels
labelInsertEncrypt = tk.Label(window, text="Введите пароль для шифрования: ")
labelInsertEncrypt.grid(row=0, column=0, sticky='N', padx=10, pady=10)

labelInsertDecrypt = tk.Label(window, text="Введите зашифрованный пароль: ")
labelInsertDecrypt.grid(row=0, column=1, sticky="N", pady=10)

labelInsertKey = tk.Label(window, text="Введите ключ: ")
labelInsertKey.grid(row=2, column=1, sticky="N", pady=20)

# Buttons
btnEncrypt = tk.Button(window, text="Шифровать", command=lambda: Encrypt())
btnEncrypt.grid(row=2, column=0)

btnErase = tk.Button(window, text="Стереть данные", command=lambda: Erase())
btnErase.grid(row=3, column=0)

btnDecrypt = tk.Button(window, text="Дешифровать", command=lambda: Decrypt())
btnDecrypt.grid(row=4, column=1)

# Encryption
def Encrypt():
    line = entryEncryptPhrase.get()
    step = randint(1, 10)
    keyFlag = False
    keyWord = ""
    encryptLine = ""
    encryptKeyValue = {}

    for i in line:

        if not keyFlag and i != "_":
            keyWord += i
            newChar = ord(i) + step
            encryptLine += chr(newChar)

        elif i == "_" and not keyFlag:
            keyFlag = True
            newChar = ord(i) + step
            encryptLine += chr(newChar)
            encryptKeyValue[keyWord] = step
            
        else:
            newChar = ord(i) + step
            encryptLine += chr(newChar)
    if not keyFlag:
        return messagebox.showerror("KEY", "NO KEY FOUND")
    answer = messagebox.askyesno("Encrypt?", f"Результат = {encryptLine}\nПродолжить?")

    if answer:

        # encryptKeyValue[1] = encryptLine
        encryptFile = open("Encrypt.txt", "w+", encoding="utf-8")
        encryptFile.write(encryptLine)
        encryptFile.close()
        keyFile = open("Key.txt", "w+")
        keyFile.write(str(encryptKeyValue))
        keyFile.close()

    print(keyWord)
    print(encryptKeyValue)
    print(encryptLine)

def Decrypt():
    decryptLine = entryDecryptPhrase.get()
    encryptLine = decryptLine
    decryptLine = ""
    keyWord = entryKey.get()
    key = {}
    keyFile = open("Key.txt", "r")
    dictKey = ast.literal_eval(keyFile.read())
    keyFile.close()
    for i in encryptLine:
        decChar = ord(i) - dictKey[keyWord]
        decryptLine += chr(decChar)
    
    answer = messagebox.askyesno("Decrypt?", f"Результат = {decryptLine}\nПродолжить?")
    if answer:
        decryptFile = open("Decrypt.txt", "w+")
        decryptFile.write(decryptLine)
        decryptFile.close()

    print(dictKey[keyWord])
    print(decryptLine)

def Erase():
    entryEncryptPhrase.delete(0, 'end')
    entryDecryptPhrase.delete(0, 'end')
    entryKey.delete(0, 'end')
    pathEncrypt = "E:\College projects\Encryptor-python\Encrypt.txt"
    pathDecrypt = "E:\College projects\Encryptor-python\Decrypt.txt"
    pathKey = "E:\College projects\Encryptor-python\Key.txt"
    if os.path.exists(pathEncrypt):
        os.remove(pathEncrypt)
    if os.path.exists(pathDecrypt):
        os.remove(pathDecrypt)
    if os.path.exists(pathKey):
        os.remove(pathKey)
    else:
        messagebox.showinfo("Info", "No files found")
    

window.mainloop()