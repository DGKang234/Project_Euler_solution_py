# 
# Solution to Project Euler problem 21
# Copyright (c) Dong-gi Kang. All rights reserved.
# 
# https://github.com/DGKang234/Project_Euler_solution_py
# https://donggikang.com/category/project-euler/
# 
""" 
Q21 - Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import numpy as np
import time

'''
solution:
1. get list of proper divisor up to 10000
2. get another list of proper divisor of the elements of the list
3. collect amicable numbers
----- process time : 2.94942 seconds -----
'''



start = time.process_time()
'''
def prop_divisor(num):
    amicable_num = set()
    for i in range(1, num):
        divisor = 0
        divisor_2 = 0
        for j in list(range(1, i)):
            if (i % j) == 0:
                divisor += j 
    
        for k in range(1, divisor):
            if (divisor % k) == 0:
                divisor_2 += k
        
        if i == divisor_2 and divisor != divisor_2: 
                amicable_num.add(divisor_2)

    return sum(amicable_num) 
'''
# We first compute a table of sum-of-proper-divisors, then we use it to test which numbers are amicable.
# This approach differs from the Java implementation because trying to directly compute
# the proper-divisor-sum of each number by brute force is unacceptably slow in Python.

#def compute():
# Compute sum of proper divisors for each number
divisorsum = [0] * 300                        # prepare an array
print(divisorsum)
print()
for i in range(1, len(divisorsum)):             # 1 to 9999
    for j in range(i * 2, len(divisorsum), i):  
        divisorsum[j] += i
        #print(i, j, divisorsum)
print()
print()
print(divisorsum)
'''	
# Find all amicable pairs within range
ans = 0
for i in range(1, len(divisorsum)):
    j = divisorsum[i]
    print(i, j, len(divisorsum))
    if j != i and j < len(divisorsum) and divisorsum[j] == i:
        print('#', i, j)
        ans += i
        print(ans)
#return None
'''


#if __name__ == '__main__':
#    print(prop_divisor(10000))

print(f"----- process time : {time.process_time() - start} seconds -----")



