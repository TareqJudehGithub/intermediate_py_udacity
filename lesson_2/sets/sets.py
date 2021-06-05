if __name__ == "__main__":
    print("Sets", "\n")

# In order to type an empty set, we must include set() type
empty_set = set()
print(empty_set)
print(type(empty_set), "\n")

# Sets only contain UNIQUE items  (1 copy of each of the elements. no repetition in sets)
s = {1, 2, 2, 4, 5, 7}
print(s, "\n")

# Adding to sets (new items will be added at the beginning of the set.)
s.add(25)
print("s.add()")
print(s, "\n")

# Remove items from sets
s.remove(25)
print("s.remove()")
print(s, "\n")

# Remove items and make sure not throw an error in case that item does not exist:
print(s, "\n")
print("s.discard()")
s.discard(25)

# .pop() removes the FIRST item in a set:
print("s.pop()")
s.pop()
print(s, "\n")

for v in s:
    print(v)

print("\n")


# s.clear() clear the whole set:
s.clear()
print(s, "\n")

# We cannot slice and index sets  like [::-1

print("\n")

basket = {"apple", "orange", "apple", "pear", "banana"}
# Loop over basket set
for fruit in basket:
    print(fruit)

print("\n")

basket.add("water melon")
print(basket, "\n")

basket_2 = {"lemon", "kiwi", "berries", "apple", "orange"}

# Here, Python returns items in basket but not in basket_2.
new_basket = basket_2 - basket
print(new_basket, "\n")

# .issubset() returns boolean value if all items in set1 are included in set2:
is_subset = basket.issubset(basket_2)
print(is_subset, "\n")

# returns items in set1, or in set2, or both:
print("or")
print(basket or basket_2)

# Unlike subtract, & (and) returns the common items in both sets:
print(basket and basket_2)


print("\n")

EFFICIENT_LETTERS = set('BCDGIJLMNOPSUVWZ')
"""Check whether a word is 'efficient' - if each letter can be drawn by a pencil 
without lifting."""


def is_efficient(letters):
    # return set(letters) <= EFFICIENT_LETTERS
    return set(letters).issubset(EFFICIENT_LETTERS)


print(is_efficient("BOLD"))

print("\n")

"""Swap the keys and values in a mapping."""

dict_items = {"a": 1, "b": 2, "c": 3, "d": 1}


def swap_keys_and_values(d):

    # Create a new set:
    swapped = {}

    # loop over dictionary keys and values:
    for key, value in d.items():
        # Create a new dictionary, where the old dictionary value becomes the
        # new dictionary keys, and visa versa:
        if value not in swapped:
            swapped[value] = set()
        swapped[value].add(key)
    print(swapped)


print(swap_keys_and_values(dict_items))

