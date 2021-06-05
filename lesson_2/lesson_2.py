print("Representing Data")
print("""
""")

greet = "hello world!"
print(greet.strip("he"))
print(greet.strip("d!"))
print("")
print(greet.removeprefix("he"))
print(greet.removesuffix("d!"))
print(greet)
print("""

""")


def compute(a, b, c):
    return (a + b) * c


print(compute("hello, ", "world! ", 3))
print("""

""")

# Strings: index slicing (indexing)

s = "Udacity"

# reverse
print(s[::-1])

# Start from index number 1, step-size by 1 index till the end.
print(s[1::2])

# step by 2 starting from index 0
print(s[::2])

print(s[-4:])
# > city

print("TUPLES")
# tuples
# An immutable sequence of heterogeneous data.
"""
Tuples are a common data structure that appear when Python packs and unpacks 
comma-separated values. Tuples are also useful to communicate immutability in 
data structures.
"""
some_num1 = 1, 2, 3

print(some_num1)

# Tuples packing:
x, y, z = some_num1

print(x)

first, *rest = 1, 4, 3, 2, 5, 6, 7, 8, 9
print(first)
print(*rest)

a, b = 0, 1
for i in range(10):
    print(i, a)
    a, b = b, a + b

print("")
# Unpacking tuples:
# Any comma-separated values are packed into a tuple:
t = 12345, 54321, "hello"
print(t)
x, y, z = t

# Any comma-separated names unpack a tuple of values
# (which must be of the same size)
print(x, y, z)

print("")
# Swaping values to two variables

var_a = 5
var_b = 3
print(var_a, var_b)

var_c = var_a
var_a = var_b
var_b = var_c

print(var_a, var_b)

print("")

# Or we could use tuple packing and unpacking to swap values:
first_name = "John"
last_name = "Smith"
print(first_name, last_name)

first_name, last_name = last_name, first_name

print(first_name, last_name)

print("")
# Fibonacci numbers:
print("Fibonacci Numbers")
num_1, num_2 = 0, 1

for i in range(25):
    print(i, num_1)
    num_1, num_2 = num_2, num_1 + num_2

print("")
print("enumerate built-in function")

colors = ["red", "green", "blue"]
for i, color in enumerate(colors):
    print(i, color)

# In the above example, enumerate() replaces the use of
# for i in range(len(colors)):
"""Special Case: .split and .join – Converting from str to list or from an Iterable to str.
It's common that we need to convert between strings and lists. Python provides two great tools here:"""

# `split` partitions a string by a delimiter into a list
# split() converts a str into a list
'ham cheese bacon'.split()
# => ['ham', 'cheese', 'bacon']
'03-30-2016'.split(sep='-')
# => ['03', '30', '2016']

# `join` creates a string from an iterable (of strings)
# "join converts a list into a str
', '.join(['Eric', 'John', 'Michael'])
# => "Eric, John, Michael"

# Strings, lists, and tuples are all sequences, so they are ordered containers.
# Lists are mutable, whereas tuples and strings are immutable.
"""
Sequence
Any object that is a sequence is a collection, and therefore also Sized, 
Iterable, and a Container, and can be used in all of the situations described above."""

print("")
#Range
for i in range(0, 10, 2):
    print(i)

# Slicing
hello = 'Hello, world!'

a = hello[0]  # Turn me into 'H'
b = hello[-2]  # Turn me into 'd'
c = hello[1:5]  # Turn me into 'ello'
d = hello[-6:]  # Turn me into 'world!'
e = hello[::2]  # Turn me into 'Hlo ol!'
f = hello[::-1]  # Turn me into '!dlrow ,olleH'

# Manipulating Strings

def make_palindrome(s):
    """Create a palindrome with the given string as a prefix.
    
    A palindrome is text that reads the same forwards and backwards.
    
    :param s: A string to form the prefix of a new palindrome.
    """
    return s[::-1]


# Manipulating Lists and Tuples
# Write a function to produce the next layer of Pascal's triangle
# Each layer is one larger than the previous layer, and each element in
# the new layer is the sum of the two elements above it in the previous
# layer. For example, `(1, 3, 3, 1) -> (1, 4, 6, 4, 1)`.
#
# Hint: What does the expression `zip(row + (0,), (0,) + row)` produce?


def add_layer(triangle):
    # Add a layer to Pascal's triangle.
    # Each layer should be a tuple.
    pass


pascals_triangle = [
    (1, ),
    (1, 1),
    (1, 2, 1),
    (1, 3, 3, 1),
]

# Add a few layers, just to check.
for _ in range(5):
    add_layer(pascals_triangle)

