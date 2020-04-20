# Compiled by Salman Qureshi
# github: hotheadhacker
# web: salmanually.com
# Socials: salmanually

# For Loop
for x in range(6):
    print(x)

# array example
fruits = ['banana','orange','mango','apple']
for x in fruits:
    print(x)

# Increment the sequence with 3 (default is 1)
for x in range (2, 30, 3):
    print(x)


# Else in For Loop:
# The else keyword in a for loop specifies
# a block of code to be executed when the loop is finished:
for x in range(6):
    print(x)
else:
    print("Yes! Finally Loop Has Been Terminated")


# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
    pass

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
# Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break