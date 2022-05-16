
def conway(num):
    current = num[0]
    run = ''
    run_list = []
    continue_loop = 'C'
    while continue_loop != 'Q':
        for n in num:
            if n == current:
                run += n
            else:
                # print(run, len(run))
                run_list.append(len(run))
                run_list.append(run)
                current = n
                run = n
        # print(run, len(run))
        run_list.append(len(run))
        run_list.append(run)
        # print(run_list)

        rl2 = list(map(str, run_list))
        rl3 = []
        for i in rl2:
            if len(i) > 1:
                # print(i[0:1])
                rl3.append(i[0:1])
            else:
                # print(i)
                rl3.append(i)
        num = "".join(rl3)

        # print(rl3)
        print(f'The ending Conway number is {num}')
        continue_loop = str.upper(input("(C)ontinue, (N)ew sequence, (Q)uit "))
        if continue_loop == "C" or continue_loop == "N" or continue_loop == "Q":
            pass
        else:
            continue_loop = str.upper(input("(C)ontinue, (N)ew sequence, (Q)uit "))
        if continue_loop == "Q":
            break
        else:
            current = num[0]
            run = ''
            run_list = []
            rl2 = []
            rl3 =[]
            if continue_loop == "N":
                num = str(input("Enter a number: "))
                current = num[0]
                print(f'The starting Conway number is {num}')

num = str(input("Enter a number: "))
print(f'The starting Conway number is {num}')
conway(num)