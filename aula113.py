# count é um iterador sem fim

from itertools import count

c1 = count(8, 8) # START AND STEP
r1 = range(8, 100) # START AND END

for i in c1:
    if i >= 100:
        break

    print(i)

for r in r1:
    print(r)


print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))
