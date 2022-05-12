
def conway(num):
    current = num[0]
    run = ''
    run_list = []
    continue_loop = 'Y'
    while continue_loop != 'N':
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
        continue_loop = str.upper(input("Continue? Enter: (y)es | (n)o | (b)egin new loop "))
        if continue_loop == "B":
            rl2 = []
            num = str(input("Enter a number: "))

num = str(input("Enter a number: "))
print(f'The starting Conway number is {num}')
conway(num)