'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import time

def comp():
    palindromic = set()
    three_int = set()
    for i in range(100, 1000):
        for j in range(100, 1000):
            numb = i*j
            n = [x for x in str(numb)]
            
            half = int(len(n)/2)
            if half == 3:
                first_half = n[0: half]
                second_half = n[half: ]

                second_half.reverse() 
                if first_half == second_half:
                    palindromic.add(numb) 

    return sorted(palindromic)[-1]

if __name__ == "__main__":
    start = time.process_time()
    print(comp())
    print(f"----- process time : {time.process_time() - start} seconds -----")

# ----- process time : 0.36790100000000003 seconds -----
