# 
# Solution to Project Euler problem 3
# Copyright (c) Dong-gi Kang. All rights reserved.
# 
# https://github.com/DGKang234/Project_Euler_solution_py
# https://donggikang.com/category/project-euler/
# 
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import time


def comp():
    n = 600851475143
    i = 1
    while i < n**1/2:
        if n % i == 0:
            n = n / i
        i = i + 1
    
    return n

if __name__ == "__main__":
    start = time.process_time()
    print(comp())
    print(f"----- process time : {time.process_time() - start} seconds -----")

# ----- process time : 0.000735000000000003 seconds -----
