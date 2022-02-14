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
    divisor = []
    divisor_candi = list(range(1, num))
    for i in divisor_candi:
        #print(i)
        if num % i == 0:            # get the least common factor list
            divisor.append(i)
 
    divisor.sort() 
    print(f"List of the proper divisor for {num} is : ")
    print(divisor)
    print()
    print(f"Sum of the proper divisor for {num} is : ")
    print(sum(divisor))
    return divisor 

prop_divisor(10000)
print(f"----- process time : {time.process_time() - start} seconds -----")



