'''
Q24 - Lexicographic permutations:

A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 
and 9?
'''

import time
import itertools 

def comp():
    num = 1 * 10**6
    digit = list(range(10))
    
    full_seq = itertools.permutations(digit)
    n = itertools.islice(full_seq, num-1, num)
    
    ans = (''.join(list(str(x) for x in next(n))))
    return ans

if __name__ == "__main__":
    start = time.process_time()
    print(comp())
    print(f"----- process time : {time.process_time() - start} seconds -----")

# ----- process time : 0.018880000000000004 seconds -----

