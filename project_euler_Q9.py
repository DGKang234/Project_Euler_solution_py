# 
# Solution to Project Euler problem 1
# Copyright (c) Dong-gi Kang. All rights reserved.
# 
# https://github.com/DGKang234/Project_Euler_solution_py
# https://donggikang.com/category/project-euler/
# 
'''
Q9 - Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
import time
import math

def comp():
    '''
    Easy simple solution without fancy mathematics
    '''
    #for i in range(1, 1000):
        #for j in range(1, i):
        #    if i != j:

        #        k = i**2 + j**2 
        #        root_k = math.sqrt(k)
        #        if i + j + root_k == 1000:
        #            print("answer")
        #            print(i, j, root_k)
        #            print(i*j*root_k)
        #            print()

    '''
    Euclid's formula a = (i**2 -j**2), b = ij, c = (i**2 + j**2)/2
    0 < a < c
    '''

    S = 1000
    for m in range(math.ceil(math.sqrt(S / 2)),
                   math.floor(math.sqrt(S) + 1)):
        a = S - S ** 2 / (2 * m ** 2)
        if a.is_integer():
            a = int(a)
            b = S - m ** 2
            c = S - a - b
    
            return a, b, c, a * b * c 

if __name__ == "__main__":
    start = time.process_time()
    print(comp())
    print(f"----- process time : {time.process_time() - start} seconds -----")
