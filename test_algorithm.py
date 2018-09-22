#function test

from sort import fast_sort, merge_sort
import time
import numpy as np

l1 = []
l2 = []
for i in range(40):
    Lis = np.random.randint(0,10000000,100000).tolist()
    strat = time.clock()
    print(fast_sort(Lis)[:10])
    end = time.clock()
    l1.append(end - strat)
    strat = time.clock()
    print(merge_sort(Lis)[:10])
    end = time.clock()
    l2.append(end - strat)
e = np.array(l2) - np.array(l1)
np.set_printoptions(precision=4)
print('fast_sort Time cost:')
print(np.array(l1))
print('merge_sort Time cost:')
print(np.array(l2))
print('average (Tm - Tf)/Tf:')
print(np.mean(e/np.array(l1)))
print('Theoretically (Tm - Tf)/Tf :')
print(0.75/3)