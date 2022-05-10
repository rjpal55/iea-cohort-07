# Lab: File I/O
with open('/tmp/poem.txt', 'r') as read_file:
    content = read_file.readlines()
content.reverse()
with open('/tmp/test.txt', 'w') as write_file:
    write_file.writelines(content)