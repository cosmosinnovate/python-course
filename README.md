## Python: 
From beginner to advance

This tutorial is designed for people that want to learn how to write python code quickly for fun and to building a project they have been dying to build. You will need to be a daily learner or a seasonal learner, otherwise you will waste your time. This tutorial will have a 30 second videos explaining concepts visually and with longer videos showing you the code in question.

#### Warning on the Python advantage: Python was designed to help solving problems faster cleanly.
From experience, the best way for you to learn this material better is how much time you spend experimenting with concepts provided here and other things I have NOT included here.
Increase your curiosity in order to leverage your creativity.

Writing software is another art of expressing your thoughts. Software today is being used for everything.
My hope is that by the end of this tutorial you should be equipped with knowledge you can use to build things for fun or getting that software engineer job or build your own company. 

#### What to expect
1. Learn the basics python
2. Learn advance way of processing files
3. Learn how to read and understand code 
4. Learn how to best search for something you are not sure of
5. Learn how to write small programs
6. Learn to build data scrapping from the Internet
7. Learn to build data vizualization 
8. Learn to build a simple web application
9. Learn RESTful apis
10. Learn rGPC a faster and secure way of RESTful version
11. Blockchain bonus


### Lesson 1.0 
## Setup you Mac/Linux/Windows here:        
1. [Click this link to setup your mac](https://programwithus.com/learn-to-code/install-python3-mac/)
### Install xcode
* Go here to downloan xcode: Go to App Store search xcode then download it. Follow all the instruction 

### Install Python
* To install python, go to this website and click download: 
https://www.python.org/downloads/

### Path Setup
* Next, we need to setup our path through terminal. 
* Type terminal in your mac spotlight and open terminal app
* Once you have that open, then you will need to paste this: ```export PATH="$PATH:/usr/local/bin/python"```


### Basic terminal commands: 
Open your terminal and do the following:

Create a directory for your project
```bash
mkdir project 
```
Go into the project directory you just created
```bash 
cd project
```
Open vscode with code . or just look for it in applications

Go to lession-1 to start coding. 

# Hope all went swiftly. 

2. [Click this link to setup your Linux](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04)
3. [Click this link to setup your Windows](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

### You will some IDE to use for writing your code. 
1. [Click this link to down VSCODE](https://code.visualstudio.com/Download)

####Print
Print things in  python: 

```py
print('I am a new progrommer')
print('Learninng the dangerous Python Language')
print('Next time you see me,')
print('Say hi')
```
The print() is a key work in python that tells the computer print something to the screen

### Drills
- Try printing something on the computer screen

### Lesson 1.1
####Comments

```py 
# This is a single comments you can use for shorter comments

""" This is a multi-line comments
    You can use it to write more comments
"""
```

### Lession 1.2
####Numbers and Math
* plus: +
* Multipy: * 
* Minus: - 
* Equal: =
* Greater-than-equal: =>
* less-than-equal: <=
* less-than: <
* greate-than: >
* Percent or Modulo:  %
* Slash/divide: /

### Lesson 1.3
####Calculation
### Using the math symbols

```py
# On the right is a variable

number = 1000 # Use variable whenever you can. Just good practice
print(number * number) # 1000,000
print(number == number) # True
print(number - 100) # 
print(number + number) # 
print(number / 10) # 100
print(number > 3) # Returns true if number is greater than 3
print(number < 3) # Return False
print(number % 10) """ Returns the reminder of the number 0 or 1: 0 means the number divides evenly but not 1"""

# Try some of them that I didn't include here
```

####Study drills
* Comment your code whenever you can to get familiar
* Find numbers to calculate
* Create a file name example.py and write your code on it.
* Research floating point

#### Common questions
* How does % sign work?
The % is not the percentage sign you use as in 100% etc. Instead the % is used to get the reminder of a number. 
Lets say in math, that a variable x divided by a variable k gives you j with a reminder of either 0 or numbers greater than 1. 

That is x % k = j 

Lets try this out. 

```py
k = 100
x = 1000

reminderOne = x % k
reminderTwo = x % 16
print(reminderOne) # 0
print(reminderTwo) # 8
```

Order of operations in math:
In the US we use PEMDAS while the rest of the work uses BODMAS math conventions. Remember this is just to help understand the order of operations. 

What does / sign mean? It is not a round down. The divide sign in python or any programming language basically means divide a number and take the whole number and nothing after the decimal point. Lets say 10.8, the computer will just return 10 and omit the '.8'. There are many reasons for that we don't care about that now. We will explore data types later to explain what type of things python uses to represent data in memory.

###Lesson 1.4
####Varibles and Data Types

What is a variable?
Variables are the left hand place holder for data representation to allow "lazy programmers" organize things in a readable way. Because as programmers, you going to forget things you wrote last night.

You are have already seen variables early: This is what it looks like

```py
number = 100 
name = "Awesomeness"
```

####Drill
1. Try to use variable and assign values to the right of it. 
2. Print do something with the variables through out your program

What are python data types?
Data types in computer programming it is used to represent data in memory. This is crucial for python to understand how to work with your program in write. 

Example of data types in python
1. String: 
```py 
"I am a string"
```
2. int: 
```py 
number = 100
```
3. Float: 
```py
floatNumber = 100.0
```
4. Boolean: 
```py
true_value = True
false_value = False
```

### Escape characters
Try using this characters in your print statements as an exercise

character | Meaning 
----- | ---
\\\\ | single backslash
\f  | fromfeed
\b | backspace
\r | carriage return: used for debugging code
\t | horizontal tab
\v |vertical tab
\\" | double quote
\\' | single quote 


### Regular questions
What is the difference between the '=' and ' == '?
The single equals '=' is for assigning values to variables like seen earlier in the lessons. 
```py 
my_name = 'Awesomeness' 
print(my_name) # my_name has the value in the right. 
```
The double equals '==' is used to varify if something is the same. 
```py 
print(10 == 10) # True
```

How can I write something like I'll or new line? Python has something called escape characters that will allow you to escape some character and achieve what you want. 

```py
print("I\'ll come home after I complete \nmy project at 7:00pm ") # \n = means go to next line: Try it yourself.
```


### Summary
In lesson 1 we covered what you really need to know do build simple projecgt without bogging you with too much information. 
We have system setup covered comments, print something, variables, math signs, and data types. 

If you want to learn more about each topics, you would need to just practice writing a program. Aftwerall you need to write code. 

### Lesson 2.0
#### Raw data input
In this lesson you will learn how to take user input and do something with the data. 

In the example below, we are going to use input() function to get user input and do something with it. 

```py 
print("How old are you?")
age = input()
print("How tall are you?")
height = input()
print("How much do you weigh?")
weight = input()

print("So you're %r tall and %r heavy.", (age, height, weight))
```

Fun time:

* Now go ahead and look for ways you can improve the code above online. Like how can you use the input function to do other things. Such as if you want the value to be 
* Use that make a calculator of some sort. 
* Try to use numbers. Remember that all values that you get from input is a string. You will need to convert the values. For instance, you can do type casting --this means taking a string and making it an int --we discussed what strings and ints are.

Example: 
```py
# Try this
numberA = input() # The value of the variable is a string

# Also try
number = int(input()) # The value of the variable is not a string but int which we need
```


### Lesson 2.1

#### Control statements

Control statement: This is how you can create logics to do simple or complex desicions

```PY
"""
    Using if statements for logics
    if something happens 
    then something else should 
    else nothing should happen
"""

if number > 2 or number < 10:
    print(number)
elif number < 2:
    print("number is less than 2")
else:
    print("number is greater")
```


#### Loops
Try this:

```PY
# Measure some strings:
words = ['Dog', 'Cat', 'Windows']
for w in words:
    print(w, len(w))


for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)) # Figure out what this function just did. To know this. you will need to print out words again. print(words)

for i in range(5): # The range function allows you to print values from 0 - 4
    print(i)

data = ['Mary', 'had', 'a', 'little', 'lamb'] 
for i in range(len(data)):
    print(i, data[i]) # What do you think this print before you print it out.

# Try this:
list(range(5))

# pass statement
while True:
    pass # Pass does nothing in a program it allows the python program not cause error when you are thinking of how to implement it. 

```


### Study drills:
* Create your own practice file and write something you would like to print out Or calculate. 
* Type things out. If you get stuck alwasy search online or look at the example here.


### Lesson 2.3
#### Functions
In this part of the lesson we are goong to talk about Function 
Function or functions are used to do specific things

Functions arguments: Functions can also take in arguments that will be used to do whatever in it. Look below:

Default arguments: That is when the argument has assigned value such as below. The default values is just a placeholder incase you didn't give the function the value it needs for he arguments.

```py
# This is Function that takes in two numbers and adds it together
def add(a,b): # takes to arguments a and b
    # Prints out the result
    print(a+b) 

def add(a=0,b=0): # takes to arguments with default values.
    # Prints out the result
    print(a+b) 

# Another way to do the same thing
def add(a,b): 
    c = a + b # variable c holds your answer 
    print(c) # print value in c


# Another way to do the same thing
def add(a,b): 
    return a + b # This returns value but it does not print. :hint put the method in print
    

def subtract(a,b):
    #  Todo: Subtract two numbers and add it to 
    pass # Replace the pass with your code.


def multiply(a,b):
    #  Todo: Multiply two numbers and add it to 
    pass # Replace the pass with your code.

def divide(a,b):
    #  Todo: Divide two numbers and add it to 
    pass # Replace the pass with your code.


# Call and print out the numbers
add(90, 10)

#  Todo
subtract(4,9)
# Do the same for the remaining Function

```

### For practice look into:
1. Fibonacci formula and see if you can write the code out. If not search how it is implemented in python.


### Lesson 2.3
#### Collections
1. List
2. Tuple
4. Dictionay


Using lists: 
The list data type has some more methods. Here are all of the methods of list objects:
Make sure you look at python docs to learn more lists and what you can do with them.


```py
# This allows you to put items in the back and remove it from the back as well. Last In Last Out
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop()) # Returns the value remove: Try it

# Using list as queue
from collections import deque  # this in python, imports a package that has all the things you need to do necessary things with deque
queue = deque(["Eric", "John", "Michael"]) # Deque: First item in and First Item out
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft() 


More on list: 
squares = []
for x in range(10):
    squares.append(x**2)

print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Try this
```

Tuples
A tuple consists of a number of values separated by commas, for instance:

```py
t = 12345, 54321, 'hello!'
print(t)
print(t[0])

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)


# Tuples are immutable: This means that you cannot change any values alread in there
t[0] = 88888

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

```


Sets
A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

```py
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                            # show that duplicates have been removed
print('orange' in basket )               # fast membership testing
print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                # unique letters in a
print(a - b )                           # letters in a but not in b
print(a | b   )                         # letters in a or b or both
print(a & b)                            # letters in both a and b
print(a ^ b )                           # letters in a or b but not both
```
Dictionaries

Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”.
Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys

For more information about dictionaries go to the python docs. However you will learn how to use all of this in real projects.

```py

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])
del tel['sape']

tel['irv'] = 4127
print(tel)

list(tel)
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)
```

### Lesson 3.0 

classes and objects

1. Class - tell python to make something new
2. object - Most basic of thing and any instance of something
3. instance - the thing you get when you told python to create from class
4. def - how to define a function 
5. self - inside a function and it also a class variable for the instance/object being accessed
6. inheritance - basically a concept that a class can inherit behaviors from a parent class just how how children inherit their parents traits
7. attributes - a property the class has
8. Composition - The concept that classes can be part of another class. Just like how a chair has legs
9. has-a - something is composed of other things  "Tuna has a mouth"
10. is-a something inherits from another "Tuna is a fish

# Examples ...

Before in too deep, python is an Object Oriented programming. 
Almost everything in python is object with properties and methods

Class: Is like an object constructor or blue print for creating objects.

To create a class you need to have the class keyword.
When creating your class, it must have the build int ``` __init__ ```function which is always executed when the class is being initialized. 
The ``` __init__ ``` function is used to assign values to object properties, or other operations when needed during creation of objects. 

```py
# Class 
class Person:
    def __init__(self, name, age): #
        self.name = name
        self.age = age


James = Person("James", 34)
Jamila = Person("Jamila", 28)

print("First name: ", James.name, "Age: ", James.age)

```
You might ask what is the ```self``` parameter: It is a reference to the current instance of the class, and is used to access variables that belongs to the class.
the self word can be anything you want it to be. But it is always good to use self.

A class has methods which just a function. Example below:
```py
# Class 
class Person:
    def __init__(self, name, age): #
        self.name = name
        self.age = age
    
    def full_info(self):
        return self.name + " "  + str(self.age)


James = Person("James", 34)
Jamila = Person("Jamila", 28)

print("First name: ", James.name, "Age: ", James.age)
print(James.full_info())
print(Jamila.full_info())

```

Files:
Dealing with files very easy. The python library has a function for files called open(). This will allow you to read files from the computer.


```py

# Make sure that your file in the same directory
file = open("test.txt", "r") # Load the file

# Run this then comment it out before you run the below function
print(file.read()) # Use the read() function to read the loaded files in file print it

# You can read lines from a file. 
# Uncomment this line before you can run this. 
print("\n")
print(file.readline())

# It is always good to close the file when done
file.close()```

# Projects coming soon....
```
### Projects
Write a book library program using list.
1. Store books in list
2. Make sure you can add new books to the library
3. Make sure that you can delete from the library
4. Search a if a book exists in the library
5. Accept user input
6. End program when when actions are done print out the lists. (Delete, search, add)
7. Validate inputs as a string
9. Print book not found if there is no book






