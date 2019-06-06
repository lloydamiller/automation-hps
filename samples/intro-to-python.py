# This is a comment

"""
This is a multi-line comment
"""

# import statements always go at the top of your file
import random

# use the randint method to generate a random number between 0.0 and 1.0 and assign to the variable rf
rf = random.random()

# use the randint method to generate a random integer between 0-10 and assign it to the variable ri
ri = random.randint(0,10)

# go here: https://docs.python.org/3/library/random.html for more on the random package, but you almost only ever need those two methods

# --------------------
# WORKING WITH NUMBERS

# assign an integer to the variable i
i = 10

# assign a float to the variable f
f = 10.0

# comparison operators
i == 10  # True
i < 11   # True
i >= 9   # True
i != 10  # False
i < 2    # False
i >= 10 and i != 20        # True
i >= 10 or i == 20         # False
not(i >= 10 and i != 20)   # True

# arthimetic operators
i += 1  # i now equals 11
i -= 1  # i now equals 10
i += f  # i now equals 20.0
i = int(i)    # converts i back to an integer
i = int(float(i))  # converts i into a float and then back into an integer (don't do this, it does nothing), I just wanted to show you can nest methods

# --------------------
# WORKING WITH STRINGS

s = "Hello World"

s = s + ", Everyone"
# "Hello World, Everyone"

s * 2
# 'Hello World, EveryoneHello World, Everyone'

s.count("l")
# 3

len(s)
# 21 (it counts each character in the string as a single item)

s.count("L")
# 0

s.upper()
# 'HELLO WORLD, EVERYONE'

s.lower()
# 'hello world, everyone'

s.split(" ")
# ['Hello', 'World,', 'Everyone']

# --------------------
# WORKING WITH LISTS

l = ["Item", 2, "Hello", s]

l[0]
# 'Item'

l[-1]
# 'Hello World, Everyone'

len(l)
# 4

l.append(5)
# ['Item', 2, 'Hello', 'Hello World, Everyone', 5]
# adds the parameter to the end of the list

l2 = [2,3]
l.extend(l2)
# ['Item', 2, 'Hello', 'Hello World, Everyone', 5, 2, 3]
# this is the same as doing l + l2

l.remove(5)
# ['Item', 2, 'Hello', 'Hello World, Everyone', 2, 3]
# takes one parameter, removes the first instance of that matching parameter in the list
# notice this also changes the length of the list AND the index positions for the items after the one removed

l.pop()
# same as remove, but it returns the number extracted
