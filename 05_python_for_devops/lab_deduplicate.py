my_list = [5,1,2,2,3,1,4,5,4,5]
deduped_list = []

for item in my_list:
    if item not in deduped_list:
        deduped_list.append(item)
print(deduped_list)