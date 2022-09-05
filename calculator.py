# functions: add, sub, mul   and div
# print options for the users
# ask for values
# call the functions

from multiprocessing.connection import answer_challenge


def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")
    #the result will show the values of a and b and the value of the add

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")
    #the result will show the values of a and b and the value of the sub

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
    #the result will show the values of a and b and the value of the mul


def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")
    #the result will show the values of a and b and the value of the div


print("A. Addtion")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")

choice = input("input your choice: ")

while True:                                     # this while will show the options till the user choice Exit
    if choice == "a" or choice == "A":
        print("Addtion")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input first number: "))  
        b = int(input("input second number: "))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("program ended")
        quit()