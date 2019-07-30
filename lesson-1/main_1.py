# For your first python lesson: 
# Go the website below and read through this then I will have you try couple of things to start programming
# https://www.tutorialspoint.com/python/python_variable_types.htm

# Variables:
# In programming, it is used for storing a value in the memory so that it can be used or reused.
# For instance, in python you can just do: 

myName = "Michelle Obama" # The name on the right is stored on the variable on the left
print(myName) # This will print out 'Michelle Obama'
num = 10000
print(num)
num1 = 100.0
print(num1)

# Control statement: This is how you can create logics to do simple or complex desicions


# Method
def check(message):
    if message < 17:
        print("Younger")
    elif message >= 17:
        print("You are too old")

print("The awesome program")
check(22)
check(10)

