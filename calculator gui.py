from tkinter import *
import tkinter.messagebox
import tkinter as tk

root = Tk()
root.geometry('315x290')
root.title("Calculator")
root.resizable(False, False)


def call(var):
    global entry
    if var == '0' and entry.get() == '':
        pass
    entry.insert(END, var)


def solve(var):
    global result
    if var != '':
        try:
            ans = eval(var)
            result.delete(0, END)
            result.insert(END, ans)
        except SyntaxError:
            tkinter.messagebox.showerror('Syntax error', 'Remove the leading zeros')


def clear():
    global entry
    entry.delete(0, END)


def delete():
    global entry
    entry.delete(len(entry.get()) - 1)


operators = ['+', '-', '*', '/', '.', '^']

entry = Entry(root, width=50)
entry.place(x=5, y=10, height=30)

count_x = 10
count_y = 10
number = 0

for i in range(0, 10):
    if number % 3 == 0:
        count_x = 10
        count_y += 40
    b = tk.Button(root, text=i, width=6)
    b.config(command=lambda t=i, b=b: call(t))
    b.place(x=count_x, y=count_y)
    number += 1
    count_x += 60

b = tk.Button(root, text=0, width=6)
b.config(command=lambda t=0, b=b: call(t))
b.place(x=70, y=count_y)

b = tk.Button(root, text='=', width=6, command=lambda: solve(entry.get()))
b.place(x=130, y=count_y)

count_x = 10
count_y = 10
number = 0

for i in operators:
    if number % 2 == 0:
        count_x = 190
        count_y += 40
    b = tk.Button(root, text=i, width=6)
    b.config(command=lambda t=i, b=b: call(t))
    b.place(x=count_x, y=count_y)
    number += 1
    count_x += 60

count_y += 40

b = tk.Button(root, text='Del', width=6, command=delete)
b.place(x=190, y=count_y)

p = tk.Button(root, text='Clear', width=6, command=clear)
p.place(x=250, y=count_y)

Label(text='Result:').place(x=5, y=220)

result = Entry(root, width=50)
result.place(x=5, y=240, height=30)

root.mainloop()
