
#
# Solution to Project Euler problem 1
# Copyright (c) Dong-gi Kang. All rights reserved.
#
# https://github.com/DGKang234/Project_Euler_solution_py
# https://donggikang.com/category/project-euler/
#

'''
Q19 - Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def comp():
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    count = 0
    
    for y in range(1900, 2001):
        for m in range(12):
            day = days[m]
            if (y % 4 == 0 and m == 1):
                day += 1
    
            for d in range(day):
                if (y > 1900 and d == 0 and total % 7 == 6): 
                    count += 1 
                total += 1
    
    return total, count 



import time
if __name__ == "__main__":
    start = time.process_time()
    print(comp())
    print(f"----- process time : {time.process_time() - start} seconds -----")

# ----- process time : 0.0024750000000000015 seconds -----



