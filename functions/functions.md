## Functions in Python

Is a rule for taking in zero to more inputs to return corresponding output.
Some function don't return anything and they are basically a modifiers. 

# passing input
def hello(param):
    return param

# no import, prints only
def hello():
    print("Hello, World")

# one line function 
def hell(): return "Hello, World"

hello("Hello") # prints out: 'Hello'

# default param

def default_function(param=False):
    if param == False:
        print("Nothing passed")
    else:
        print(param)


