import tkinter as tk
from random import randint
import sys, os
from tkinter import messagebox
import codecs

# ГЕНЕРИРУЕТ ШИФР ИСХОДЯ ИЗ САМОГО КЛЮЧА

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
    keyFlag = False
    keyWord = ""
    keyCounter = 0
    encryptLine = ""
    cryptSum = 0

    for i in line:

        if not keyFlag and i != "_":
            keyWord += i

        elif i == "_" and not keyFlag:
            keyFlag = True
            for j in keyWord:
                cryptSum += ord(j)
                keyCounter += 1

        else:
            newChar = ord(i)
            encryptLine += chr(newChar)
    

    if not keyFlag:
        return messagebox.showerror("KEY", "NO KEY FOUND")
    

    encryptLineCopy = encryptLine
    encryptLine = ""

    for i in encryptLineCopy:
        newo = ord(i) + (cryptSum // keyCounter)
        encryptLine += chr(newo)
        
    answer = messagebox.askyesno("Encrypt?", f"Результат = {encryptLine}\nПродолжить?")

    if answer:

        # encryptKeyValue[1] = encryptLine
        encryptFile = open("Encrypt.txt", "w+", encoding="utf-8")
        encryptFile.write(encryptLine)
        encryptFile.close()

    print(keyWord)
    print(encryptLine)

def Decrypt():
    decryptLine = entryDecryptPhrase.get()
    encryptLine = decryptLine
    decryptLine = ""
    keyWord = entryKey.get()
    cryptSum = 0
    keyCounter = 0

    for i in keyWord:
        cryptSum += ord(i)
        keyCounter += 1

    for i in encryptLine:
        decChar = ord(i) - (cryptSum // keyCounter)
        decryptLine += chr(decChar)
    decryptLine = decryptLine[1:]
    
    answer = messagebox.askyesno("Decrypt?", f"Результат = {decryptLine}\nПродолжить?")
    if answer:
        with codecs.open("Decrypt.txt", "w", "utf-16") as stream:
            stream.write(decryptLine)
        # decryptFile.write(decryptLine)
        # decryptFile.close()

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
    else:
        messagebox.showinfo("Info", "No files found")
    



    



window.mainloop()