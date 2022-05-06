start_list = ['1','1','1','3','5']
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0

counter = 0
while counter < len(start_list):
    for i in start_list:

        if start_list[counter] == start_list[counter+1]:
            print(i)
            counter += 1
# list_len = [i for i in start_list.count(i)]
# print(list_len)
# print(start_list.count('1'))
# print(start_list[0])