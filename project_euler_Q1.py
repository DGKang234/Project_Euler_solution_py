# 
# Solution to Project Euler problem 4
# Copyright (c) Dong-gi Kang. All rights reserved.
# 
# https://github.com/DGKang234/Project_Euler_solution_py
# https://donggikang.com/category/project-euler/
# 
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
import time

def comp(num):
    answer = sum(x for x in range(num) if (x % 3 == 0 or x % 5 == 0))
    '''
    # [solution] the list comprehension is equal to:
    answer = 0
    for x in range(num):
        if (x % 3 == 0 or x % 5 == 0):
            answer += x
    '''
    return answer

if __name__ == "__main__":
    start = time.process_time()
    print(comp(1000))
    print(f"----- process time : {time.process_time() - start} seconds -----")
