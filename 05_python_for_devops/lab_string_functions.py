# psuedo code: get user input, accept stride (int) from user, loop over string, upper case stride # of characters, lower case stride # of chars, output
# user_input = ("abcdefghijklmnopqrstuvwxyz")
# stride = 2
user_input = input("Enter string:")
stride = int(input("Enter stride:"))

# output = ''
# pos = 0
# while pos < len(user_input):
#     section = user_input[pos:pos+stride]
#     output += section.upper()
#     section = user_input[pos+stride:pos+stride * 2]
#     output += section.lower()
#     pos += stride * 2
# print(output)

# output = ''
# for pos in range(0,len(user_input),stride * 2):
#     section = user_input[pos:pos+stride]
#     output += section.upper()
#     section = user_input[pos+stride:pos+stride * 2]
#     output += section.lower()
#     pos += stride * 2
# print(output)

# output = ''
# for pos in range(0,len(user_input),stride):
#     section = user_input[pos:pos+stride]
#     if pos % (stride * 2) == 0:
#         output += section.upper()
#     else:
#         output += section.lower()
# print(output)

output = ''
do_upper = True
for pos in range(0,len(user_input),stride):
    section = user_input[pos:pos+stride]
    if do_upper:
        output += section.upper()
    else:
        output += section.lower()
    do_upper = not do_upper
print(output)