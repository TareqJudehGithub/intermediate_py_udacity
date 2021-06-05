# Creating a dict:

# new_dict = dict()
#
# a = dict(one=1, two=2, three=3)
# b = {'one': 1, 'two': 2, 'three': 3}
# c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
#
# print(a["one"])
#
# # Add a new value to the dict
# a["four"] = 4
#
# # Del elem from a dict:
# del a["four"]
# # Or,
# a.pop("three")
# print(a)
#
# # View the keys:
# print(a.keys())
#
# # View values:
# print(a.values())
#
# # View both keys and values
# a.items()
#
# # size of keys
# len(a.keys())
#
# # Looping over both keys and values:
# for k, v in a.items():
#     print(k, v)
#
# # get()  refer to notes.txt
# five = a.get("five", 5)
# print(len(a))
# print(a)
#
# print(("one", 1) in a.items())
#
# # clear the entire dict:
# a.clear()
# print(a)

# ===============================================

d = {"one": 1, "two": 2, "three": 3}
print(d["two"]) # > 2
d["three"] = 5
# d = {"one": 1, "two": 2, "three": 5}
del d["one"]
# d = {"two": 2, "three": 5}
print(len(d)) # 2
d["four"] = 8
# d = {"two": 2, "three": 5, "four": 8}
print(d.get("three"))
print(d.get("three", d["four"]))
print(max(d.values())) # 8
print(min(d)) # four
print(d.pop("four", 4)) # 8
print(d.pop("one", d["two"])) # 2
print(d.pop("two")) # 2
print("\n")
print(d)
for key, value in d.items():
    print(key * value)