'''
Q16

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

import time

def comp():
    num = 2**1000
    digit = [int(x) for x in list(str(num))] 
    
    return sum(digit)

if __name__ == "__main__":
    start = time.process_time()
    print(comp())
    print(f"----- process time : {time.process_time() - start} seconds -----")

# ----- process time : 6.499999999999909e-05 seconds ----- 
