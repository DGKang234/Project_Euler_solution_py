#
# Solution to Project Euler problem 6
# Copyright (c) Dong-gi Kang. All rights reserved.
#
# https://github.com/DGKang234/Project_Euler_solution_py
# https://donggikang.com/category/project-euler/
#
'''
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import time

def comp():
    
    sum_of_sqaures = sum([x**2 for x in range(1, 100+1)])
    square_of_sum = sum(range(1, 100+1))**2

    diff = square_of_sum-sum_of_sqaures

    return diff

if __name__ == "__main__":
    start = time.process_time()
    print(comp())
    print(f"----- process time : {time.process_time() - start} seconds -----")


# ----- process time : 4.60000000000009e-05 seconds -----
