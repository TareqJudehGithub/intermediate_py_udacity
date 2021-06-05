import collections


# Counter:  returns a dictionary with items as key and values as the quantities
# of these items.

# Counter() counts quantities of all items
list_counter = collections.Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C'])

print(list_counter)

# While list .count() method, counts a given item
new_list = [1, 2, 3, 4, 5, 5, 5]
print(new_list.count(5))

print("\n")
# Notice how in sets, items are not repeated:
set_counter = collections.Counter({'B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C'})
print(set_counter)

print("\n")
dict_counter = collections.Counter({
    "tareq": 45,
    "noor": 39,
    "dina": 14,
    "leen": 10,
})

print(dict_counter)

# OrderedDict

print("This is just a Dict: \n ")
d = dict()
d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4

for k, v in d.items():
    print(k, v)

print("\n")

# Delete 'a' from d:
d.pop("a")

print("re-insert a into d: ")
d["a"] = 1
for k, v in d.items():
    print(k, v)


print("\n")
print("This is an OrderedDict: \n")
od = collections.OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
od["d"] = 4


for k, v in od.items():
    print(k, v)

print("\n")
# del "a"
od.pop("a")

# re-insert "a"
od["a"] = 1
for k, v in od.items():
    print(k, v)

print("\n")
# DefaultDict
# A DefaultDict is also a sub-class to dictionary. It is used to provide some
# default values for the key that does not exist and never raises a KeyError.


# Example, count how many items are in L list:
d = collections.defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]
for i in L:
    d[i] += 1


print(d)

counter_d = collections.Counter(d)
print(counter_d)


print("\n")
# ChainMap
# A ChainMap encapsulates many dictionaries into a single unit and returns a list
# of dictionaries.

# Example:
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d4 = {"g": 7, "h": 8}

d_combined = collections.ChainMap(d1, d2, d3)
print(d_combined)

# Accessing a single item in the chain-mapped Dict:
c = d_combined["c"]
print(c)

print(d_combined.keys())

for k, v in d_combined.items():
    print(k, v)

print("\n")

# A new dictionary can be added by using the new_child() method. The newly added
# dictionary is added at the 'beginning' of the ChainMap.
new_chain = d_combined.new_child(d4)
print(new_chain)

print("\n")
# NamedTuple

student = collections.namedtuple("student", ["name", "age", "DOB"])
# Adding values
s = student("Tareq", 45, "123456")
print(s[1])
print(s.name)