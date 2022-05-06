words_dict = {}
with open('/tmp/poem.txt', 'r') as read_file:
    content = read_file.read()
words_content = content.lower().strip(',!—')
# print(len(content))
# for word in content:
#     print(word)
words_list = words_content.split()
# print(words_list)

for word in words_list:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1
# print dictionary sorted descending by value
print(dict(sorted(words_dict.items(), key=lambda item: item[1],reverse=True)))