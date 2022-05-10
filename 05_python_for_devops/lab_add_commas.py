def add_commas(num):
    snum = str(num)[::-1]
    rsnum = []
    counter = 0
    for n in enumerate(snum):
        rsnum.append(n[1])
        counter += 1
        if counter == len(snum):
            pass
        elif counter % 3 == 0:
            rsnum.append(',')
    rsnum.reverse()
    rsnum = ''.join(rsnum)
    return rsnum
commas = add_commas(124)
print(commas)