## Understanding Python Oop (Object Oriented Programming)

More on datatypes:

Built in types:

Booleans
bool: Is either True or False. Bool type is a subclass of int type: True and False

not y
x or y 
x and y

issubclass(bool, int)
issubclass(True, bool)
issubclass(False, bool)

You can also do something like this. 

True + False == 1 # 1 + 0 = 1
True * True == 1 # 1 * = 1

Sequences:

Python differentiate between sequences and unordered collections: eg SET AND DICT

## tuple: A tuple is ordered collection of n values n>=0
Tuple supports indexing, immutable; hashtable if members are all hashtable
a =(1,2,3,4)
x =('a', 1, 'python', (1,2))
x[1] = 'Something'


## list: An ordered collection of values n >= 0

a = ['a', 'aa', 1231]
b = [1,2,23, 'python', (1,2,3,4), [2,44]]
b[2] = "New values"
Not hashtable, mutable


## Set: An unordered collection of unique values. must be hashtable
a = {1, 3, 'b'}

## dict: An unordered collection of unique key-value pairs; key must be hashtable
a = {1: 'one',
     2: 'two'}
b = {'a': [1, 2, 3],
     'b': 'a string'}

## An object is a hashtable if has a value which never changes during its lifetime. (it needs a __hash__() method)


You have already seen how objects are created in python. In this section, we will dive in to oop to build real world objects that you will find helpful when you are building an app etc. 

### Example:

## Undersanding Datatype deeply
Bool: 

Sets


