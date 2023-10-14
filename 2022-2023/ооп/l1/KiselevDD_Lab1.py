import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from turtle import onclick

def calculate():
    result = int(eval(f'{firstNumberEntry.get()} {chooseOperationCB.get()} {secondNumberEntry.get()}'))
    answer = mb.showinfo("Ответ", f"{int(result)}\n{bin(int(result))}\n{oct(int(result))}\n{hex(int(result))}")

window = tk.Tk()
window.title('Калькулятор')
window.geometry('800x50')

firstNumberEntry = tk.Entry(window, relief='groove')
firstNumberEntry.grid(row=0, column=0)

secondNumberEntry = tk.Entry(window, relief='groove')
secondNumberEntry.grid(row=0, column=2)

operations = ['+', '-', '*', '/']
chooseOperationCB = ttk.Combobox(window, values=operations, state='readonly')
chooseOperationCB.grid(row=0, column=1)

resultBttn = ttk.Button(window, text='=', command=lambda: calculate())
resultBttn.grid(row=0, column=3)

result_label = ttk.Label(text="ответ в новом окне").grid(column=4, row=0)

window.mainloop()