'''
Non-abundant sums
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
 of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can 
 be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis 
 even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less 
 than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import time

def comp():
    cap = 28124
    divisorsum = [0] * cap
    for i in range(1, len(divisorsum)):
        for j in range(i*2, len(divisorsum), i):
            divisorsum[j] += i
   
    abundant = [i for (i, x) in enumerate(divisorsum) if x > i]


    tool = [False] * cap
    for i in abundant:
        for j in abundant:
            if i+j < cap:
               tool[i+j] = True

    final = sum(i for i, x in enumerate(tool) if not x)
    print(final)
    return final

if __name__ == '__main__':
    start = time.process_time()
    comp()
    print(f"----- process time : {time.process_time() - start} seconds -----") 


