from math import *
from tkinter import *
from typing import Collection

root = Tk()
root.title("Simple Calculator")

root.configure(background = "#282a36")
e = Entry(root, width = 50, borderwidth = 5, background = "#44475a", foreground = "#f8f8f2")
e.grid(row=0, column = 0, columnspan = 4, padx = 15, pady = 10)

# button action functions 
def button_click(num):
    curr = e.get()
    if len(curr) != 0:
        if curr[len(curr)-1].isalpha():
            e.delete(0, END)
    e.insert(len(e.get()), num)

def button_dot():
    if "." not in e.get():
        e.insert(len(e.get()), ".")

def button_clear():
    e.delete(0, END)

def button_op(operation):
    try: 
        first_num = float(e.get())
        global f_num 
        global op
        f_num = first_num
        op = operation
        e.delete(0, END)
    except ValueError:
        curr = e.get()
        e.delete(0, END)
        if "ERROR" in curr:
            e.insert(0, "ERROR: INSERT A NUMBER")
        else:
            e.insert(0, "ERROR: <" + curr + "> IS NOT A NUMBER")
        # button_clear.bg

def button_equal():
    try:
        second_num = float(e.get())
        e.delete(0, END)
        if op == "addition":
            answer = f_num + second_num
        elif op == "subtraction":
            answer = f_num - second_num
        elif op == "multiplication":
            answer = f_num * second_num
        elif op == "division":
            answer = f_num / second_num
        elif op == "exponent":
            answer = pow(f_num, second_num)
        else:
            e.insert(0, "ERROR")
            return 
        if int(answer) == answer:
            answer = int(answer)
        e.insert(0, answer)
    except OverflowError:
        e.insert(0, "ERROR: OVERFLOW")
    except ZeroDivisionError:
        e.insert(0, "ERROR: CANNOT DIVIDE BY ZERO")
    except ValueError:
        e.delete(0, END)
        e.insert(0, "ERROR: INSERT A NUMBER")

# define buttons 
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1), background = "#282a36", foreground = "#f8f8f2", activebackground = "#44475a")
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2), background = "#282a36", foreground = "#f8f8f2", activebackground = "#44475a")
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3), background = "#282a36", foreground = "#f8f8f2", activebackground = "#44475a")
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4), background = "#282a36", foreground = "#f8f8f2", activebackground = "#44475a")
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5), background = "#282a36", foreground = "#f8f8f2", activebackground = "#44475a")
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6), background = "#282a36", foreground = "#f8f8f2", activebackground = "#44475a")
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7), background = "#282a36", foreground = "#f8f8f2", activebackground = "#44475a")
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8), background = "#282a36", foreground = "#f8f8f2", activebackground = "#44475a")
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9), background = "#282a36", foreground = "#f8f8f2", activebackground = "#44475a")
button_0 = Button(root, text = "0", padx = 87.5, pady = 20, command = lambda: button_click(0), background = "#282a36", foreground = "#f8f8f2", activebackground = "#44475a")
button_dot = Button(root, text = ".", padx = 41, pady = 20, command = button_dot, background = "#282a36", foreground = "#f8f8f2", activebackground = "#44475a")

button_plus  = Button(root, text = "+", padx = 40, pady = 35, command = lambda: button_op("addition"), background = "#44475a", foreground = "#f8f8f2", activebackground = "#282a36")
button_minus  = Button(root, text = "-", padx = 41, pady = 36, command = lambda: button_op("subtraction"), background = "#44475a", foreground = "#f8f8f2", activebackground = "#282a36")
button_multip  = Button(root, text = "*", padx = 40, pady = 20, command = lambda: button_op("multiplication"), background = "#44475a", foreground = "#f8f8f2", activebackground = "#282a36")
button_divis  = Button(root, text = "/", padx = 40, pady = 20, command = lambda: button_op("division"), background = "#44475a", foreground = "#f8f8f2", activebackground = "#282a36")
button_exp = Button(root, text = "^", padx = 39, pady = 20, command = lambda: button_op("exponent"), background = "#44475a", foreground = "#f8f8f2", activebackground = "#282a36")
button_clear = Button(root, text = "Clear", padx = 30, pady = 20, command = button_clear, background = "#44475a", foreground = "#f8f8f2", activebackground = "#282a36")
button_equal = Button(root, text = "=", padx = 40, pady = 20, command = button_equal, background = "#44475a", foreground = "#f8f8f2", activebackground = "#282a36")

# put buttons on screen
button_1.grid(row = 8, column = 0, rowspan = 2)
button_2.grid(row = 8, column = 1, rowspan = 2)
button_3.grid(row = 8, column = 2, rowspan = 2)

button_4.grid(row = 6, column = 0, rowspan = 2)
button_5.grid(row = 6, column = 1, rowspan = 2)
button_6.grid(row = 6, column = 2, rowspan = 2)

button_7.grid(row = 4, column = 0, rowspan = 2)
button_8.grid(row = 4, column = 1, rowspan = 2)
button_9.grid(row = 4, column = 2, rowspan = 2)

button_0.grid(row = 10, column = 0, columnspan = 2, rowspan = 2)
button_dot.grid(row = 10, column = 2, rowspan = 2)

button_minus.grid(row = 4, column = 3, rowspan = 3)
button_plus.grid(row = 7, column = 3, rowspan = 3)
button_equal.grid(row = 10, column = 3, rowspan = 3)

button_exp.grid(row = 2, column = 0, rowspan = 2)
button_divis.grid(row = 2, column = 1, rowspan = 2)
button_multip.grid(row = 2, column = 2, rowspan = 2)
button_clear.grid(row = 2, column = 3, rowspan = 2)

root.mainloop()

""" Console-based calculator UI 
def calc():
    num1 = input("Enter a number: ")
    if (isinstance(num1, (int, float))):
        print("ERROR: first number is not valid")
        return
    
    num2 = input("Enter another number: ")
    if (isinstance(num2, (int, float))):
        print("ERROR: second number is not valid")
        return
    
    op = input("Enter an operator(+ - * / ^ %): ")
    if (op == "+"):
        result = float(num1) + float(num2)
    elif (op == "-"):
        result = float(num1) - float(num2)
    elif (op == "*"):
        result = float(num1) * float(num2)
    elif (op == "/"):
        result = float(num1) / float(num2)
    elif (op == "^"):
        result = pow(float(num1), float(num2))
    elif (op == "%"):
        result = float(num1) % float(num2)
    else: 
        result = "ERROR: unexpected input."

    print(result)
"""