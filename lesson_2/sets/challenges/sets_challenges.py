# Challenge: check if items are already in carts or not:
# import cart_items
# import new_items
#
# cart = cart_items.cart_items
# new_item = new_items.new_item
# print(new_item)
# print(cart, "\n")
#
#
# def cart_check(item):
#
#     new_item.add(item)
#     print(new_item)
#
#     if new_item.issubset(cart):
#         return f"{item} is already in shopping cart!"
#     else:
#         cart.add(item)
#
#         with open("items_added.txt", mode="a") as file:
#             file.write(f"{item}\n")
#
#         print(f"{item} has been  added to cart successfully!")
#
#     with open("cart_items.py", mode="a") as cart_file:
#         cart_file.write(str(cart))
#         print(cart_file)
#
#         return cart
#
#
# print(cart_check("kiwi".title()))


# Challenge,  swap dict keys with values:
print("\n")

dict_items = {"a": 1, "b": 2, "c": 3, "d": 1}
print(dict_items)


def swap_kv(dictionary):
    swapped_dict = dict()

    for kk, vv in dictionary.items():
        if vv not in swapped_dict:
            swapped_dict[vv] = set()
        swapped_dict[vv].add(kk)

    return swapped_dict


print(swap_kv(dict_items))




