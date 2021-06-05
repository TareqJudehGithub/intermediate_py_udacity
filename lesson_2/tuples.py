# a = 1, 2, 3
# b = 4, 5, 6
#
# c = zip(a, b)
#
#
# print(tuple(c))


x = 5
y = 2

# old school:
# z = x
# x = y
# y = z

# Python tuples:
x, y = y, x

print(x, y)
print("\n")

# Fibonacci code:
"""
a, b = a, b
0, 1 = 1, 0 + 1 
1, 1 = 1, 1 + 1
1, 2 = 2, 1 + 2
2, 3 = 3, 2 + 3
3, 5 = 5, 3 + 5
5, 8 = 8, 5 + 8
8, 13 = 13, 8 + 13
13, 21 = 21, 13 + 21
21, 34 = 34, 21 + 34
34, 55 = 55, 34 + 55
55, 89 = 89, 55 + 89
89, 144 = 144, 89 + 144
144, 233 = 233, 144 + 233
233
    
"""
print("\n")
print("===============================")


def fibonacci(num1=int, num2=int):
    for index in range(13):
        num1, num2 = num2, num1 + num2
        print(index, num1)


fibonacci(0, 1)
print("\n")
print("===============================")

# all and any functions
some_list = [1, 2, 3, 4, 5, False]
print(all(some_list))
print(any(some_list))

print("\n")
print("===============================")

combine_tup = zip((1, 3, 4, 5), (8, 3, 9))
new_tup = tuple(combine_tup)

print("\n")
print("===============================")
# Filter

# Filter people with age 18 and above from age_list, and add them in a new list:
age_list = [23, 15, 18, 19, 45, 13]


def above_18(age):
    return age >= 18


adults = filter(above_18, age_list)

adults_list = [adult for adult in adults]
print(adults_list)

print("\n")
print("===============================")

# Map
fruits = ['apple', 'banana', 'cherry']
# Find out the length of each item in the fruits list:


def item_length(item):
    return len(item)


item_length = map(item_length, fruits)

result = [item for item in item_length]
print(result)

new_list = [1, 2, 3, 4, 5]


def plus(n):
    return n * 2


result = [item for item in map(plus, new_list)]
print(result)


x = ['a', 'b', 'c', 'd']
print(x[:3])

z = 'abcd'
print(z[:3])

print("\n")
print("===============================")


