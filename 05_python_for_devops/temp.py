import timeit

ti1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(ti1)

ti2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(ti2)

ti3 = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(ti3)

ti4 = ("-".join(map(str, range(100))))
print(ti4)