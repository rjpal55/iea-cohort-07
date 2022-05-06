from collections import Counter
list1 = ["a","b","c"]
list2 = ["a","b","c"]
user_action = ""
user_pos = ""
cur_list = ""

while user_action != "quit":
    user_action = input("Enter action (add, remove, delete (by position), reverse, print, equality, quit): ")
    if user_action == "quit":
        break
    if user_action == "equality":
        if Counter(list1) == Counter(list2):
            print("The lists are equal")
        else:
            print("The lists are not equal")
        continue

    user_list = int(input("Enter list (1 or 2): "))
    if user_list == 1:
        cur_list = list1
    else:
        cur_list = list2

    if user_action == "print":
        for index,item in enumerate(cur_list):
            print(index,item)
        continue        
    if user_action == "reverse":
        cur_list.reverse()
        print(cur_list)
        continue
    if user_action == "delete":
        for index,item in enumerate(cur_list):
            print(index,item)
        user_pos = int(input("Enter position: "))
        cur_pos = user_pos
        cur_list.pop(cur_pos)
        continue
    
    if user_action == "add":
        print(cur_list)
        user_item = input("Enter item to add: ")
        cur_list.append(user_item)
    elif user_action == "remove":
        print(cur_list)
        user_item = input("Enter item to remove: ")
        cur_list.remove(user_item)

print(list1)
print(list2)