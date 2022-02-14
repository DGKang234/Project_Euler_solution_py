""" 
Q21 - Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import numpy as np
import time

start = time.process_time()
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

if __name__ == '__main__':
    print(prop_divisor(10000))

print(f"----- process time : {time.process_time() - start} seconds -----")



