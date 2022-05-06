# Lab: File I/O
with open('/tmp/poem.txt', 'r') as read_file:
    content = read_file.read()
with open('/tmp/test.txt', 'w') as write_file:
    write_file.write(content)
# need to add print lines in bottom to top
