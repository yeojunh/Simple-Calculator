from math import *
from tkinter import *

root = Tk()
root.title("Calculatorinator v2.0 Plus Pro")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row=0, column = 0, columnspan = 3, padx = 10, pady = 10)
root.mainloop()

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

calc()