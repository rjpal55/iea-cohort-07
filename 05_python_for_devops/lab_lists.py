from collections import Counter
list1 = ["a","b","c"]
list2 = ["a","b","c"]
user_action = ''

while user_action != "quit":
    user_action = input("Enter action (add, remove, reverse, print, equality, quit): ")
    if user_action == "quit":
        break
    if user_action == "equality":
        if Counter(list1) == Counter(list2):
            print("The lists are equal")
        else:
            print("The lists are not equal")
        continue
    user_list = int(input("Enter list (1 or 2): "))
    if user_action == "print":
        if user_list == 1:
            print(list1)
            continue
        else:
            print(list2)
            continue
    if user_action == "reverse":
        if user_list == 1:
            list1.reverse()
            print(list1)
            continue
        else:
            list2.reverse()
            print(list2)
            continue
    
    user_item = input("Enter item: ")
    
    if user_action == "add" and user_list == 1:
        list1.append(user_item)
    elif user_action == "add" and user_list == 2:
        list2.append(user_item)
    elif user_action == "remove" and user_list == 1:
        if user_item in list1:
            list1.remove(user_item)
    elif user_action == "remove" and user_list == 2:
        if user_item in list2:
            list2.remove(user_item)
    elif user_action == "reverse" and user_list == 1:
        list1.reverse()
    else:
        list2.reverse()

print(list1)
print(list2)