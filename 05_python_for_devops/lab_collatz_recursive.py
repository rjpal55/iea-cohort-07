def collatzr(num):
    if num == 1:
        return num
    print(num, end=' ')
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
    return collatzr(num)

final = collatzr(52)
print(final)