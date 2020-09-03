#pep guidelines
#imports of seperate lines unless they are from the same module
import os
import sys
from MyModule import fop, bar, foobar

def my_function(one, two,
                three, four, 
                five, six):
    print("Hello World")

#two bank lines to seperate functions
def second_function():
    print("Second function")


my_list = [1, 2,
            3, 4,
            5, 6]