import itertools
import numpy as np

def p(a=1, b=2, c=3, d=4):
    print(a,b,c,d)
    return a+b+c+d

g = np.vectorize(p)
print(g(np.random.rand(3),10))

print(np.fromiter(itertools.takewhile(lambda x: x <= 3, [1,2,3,4,5,6,7,8,9,1,1,1]), dtype=int))