# Comprehensions

squares = [x ** 2 for x in range(10)]
print(squares)

# Comprehensions with conditions:
even_squares = [y ** 2 for y in range(10) if y % 2 == 0]
print(even_squares)

# Dictionary Comprehension:

dict_squares = {a: a ** 2 for a in range(10)}
print(dict_squares)

even_dict_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(even_dict_squares)

sentences = "hello, world!"
word_list = [word.upper() for word in sentences]
word = "".join(word_list)
print(word)

tuple_comp = [(x, x ** 2, x ** 3) for x in range(3)]
print(tuple_comp)

triangle_matrix = [(i, j) for i in range(5) for j in range(i)]
print(triangle_matrix)

fruits_dict = {
    "Banana": 1,
    "Orange": 3,
    "Apple": 4,
    "Lemon": 2,
    "Water Melon": 2
}
berries = fruits_dict.get("Berries", 5)
print(berries)

print(fruits_dict, "\n")




def swapped_fruits(d):
    new_dict = dict()
    for k, v in d.items():
        if v in new_dict:
            new_dict[v].append(k)
        else:
            new_dict[v] = [k]
    return new_dict


print(swapped_fruits(fruits_dict))


def swapped_fruits_comp(d):
    invert_dict = {}
    swapped_items = {invert_dict.setdefault(v, []).append(k) for (k, v) in
                     d.items()}
    print(invert_dict)
    return swapped_items


print(swapped_fruits_comp(fruits_dict))

student_grades = {
    "student_1": 85,
    "student_2": 95,
    "student_3": 90,
    "student_4": 72,
    "student_5": 65,
    "student_6": int()

}

accepted_students = {k: v for (k, v) in student_grades.items() if v >= 85}

print(accepted_students)


fts = {1: 1, 2: 1, 3: 2, 4: 1}

new_dict = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
print(new_dict)


# Set Comprehension
