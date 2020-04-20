# Compiled by Salman Qureshi
github: hotheadhacker
web: salmanually.com
Socials: salmanually

# Compiled by Salman Qureshi
# github: hotheadhacker
# web: salmanually.com
# Socials: salmanually

# Variables
# Variables do not need to be declared with any particular type and can even change type after they have been set.
# String variables can be declared either by using single or double quotes:
x = 5
y = "Salman"
print(x)
print(y)


"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)

"""


# Assign Value to Multiple Variables

# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Output Variables
# The Python print statement is often used to output variables.
# To combine both text and a variable, Python uses the + character:

x = "Cool"
print("Python is " + x)

# You can also use the + character to add a variable to another variable:
x = "Python is "
y = "Cool"
z = x + y
print(z)

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

# If you try to combine a string and a number, Python will give you an error:
x = 5
y = "Salman"
# print(x + y)


# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
# Create a variable outside of a function, and use it inside the function
x = "amazing"
def myFunction():
    print("Python is " + x)
myFunction()

"""
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
The global variable with the same name will remain as it was, global and with the original value.
"""

# Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myFunction2():
    x = "fantastic"
    print("Python is " + x)

myFunction2()
print("Python is " + x)


# The global Keyword
"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

"""
# If you use the global keyword, the variable belongs to the global scope:

~~~
def myFunction3():
    global x1
    x1 = "fantastic"
myFunction3()
print("Python is " + x1)
~~~
# Also, use the global keyword if you want to change a global variable inside a function.
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
~~~
x2 = "awesome"

def myFunction4():
    global x2
    x2 = "fantastic"
myFunction4()
print("Python is " + x2)
~~~