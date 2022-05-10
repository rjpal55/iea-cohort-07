from functools import reduce
def sumdigits(n1):
    total = 10
    num = [int(n) for n in str(n1)]
    numsum = reduce((lambda x,y: x+y),num)
    total = numsum
    print(total)
    while total >=10:
        num = [int(n) for n in str(numsum)]
        numsum = reduce((lambda x,y: x+y),num)
        total = numsum
        print(total)
    return numsum
sumd = sumdigits(12351235)
print(sumd)