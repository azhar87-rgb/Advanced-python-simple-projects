from numpy import *
def addition(a,b):
    return add(a,b)
def sub(a,b):
    return subtract()
def mul(a,b):
    return multiply(a,b)
num1=int(input("Enter the  first number: "))
num2=int(input("Enter the  second number: "))
calc=input("Enter what you want to perform: ")
if calc=="+":
    print(f'The sum of {num1} + {num2} = {addition(num1,num2)}')
elif calc=="-":
    print(f'The diference of {num1} - {num2} = {sub(num1,num2)}')
elif calc=="x":
    print(f'The product of {num1} x {num2} = {mul(num1,num2)}')
