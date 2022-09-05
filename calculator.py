# functions: add, sub, mul   and div
# print options for the users
# ask for values
# call the functions

from multiprocessing.connection import answer_challenge


def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))
    #the result will show the values of a and b and the value of the add

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))
    #the result will show the values of a and b and the value of the sub

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))
    #the result will show the values of a and b and the value of the mul
    



