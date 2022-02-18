'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import time
import math

def comp():
    lcm = 1
    lcm_set = set()
    for i in range(1, 21):
        gcd = math.gcd(i, int(lcm))
        lcm = (i * lcm / gcd)       # lcm(x, y) = x * y /gcd(x, y)
        lcm_set.add(lcm)
        
    return sorted(lcm_set)[-1]

if __name__ == "__main__":
    start = time.process_time()
    print(comp())
    print(f"----- process time : {time.process_time() - start} seconds -----")


