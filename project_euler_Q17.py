# 
# Solution to Project Euler problem 17
# Copyright (c) Dong-gi Kang. All rights reserved.
# 
# https://github.com/DGKang234/Project_Euler_solution_py
# https://donggikang.com/category/project-euler/
# 
'''
Q17

If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 
20 letters. The use of 'and' when writing out numbers is in compliance 
with British usage.
'''

import time

def comp():
    numbers = [str(x) for x in range(1, 1001)]
    
    call_digits = {
        '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', 
        '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    
    call_tens = {
        '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', 
        '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '1': 'ten', 
        '2': 'twenty','3': 'thirty', '4': 'fourty', '5': 'fifty', '6': 'sixty', '7': 'seventy', 
        '8': 'eighty', '9': 'ninty'
    }
    
    hundred = 'hundred'
    
    start = time.process_time()
    sum_len_name = 0
    for i in numbers:
        if len(i) == 1:
            sum_len_name += len(call_digits[i])
    
        elif len(i) == 2:
            if 10 < int(i) < 20:
                sum_len_name += len(call_tens[i])
    
            elif i[1] == '0':
                sum_len_name += len(call_tens[i[0]])
    
            elif 20 <= int(i):
                sum_len_name += len(call_tens[i[0]] + call_digits[i[1]])
    
        elif len(i) == 3:
            if (i[1] == '0' and i[2] == '0'):       # 100
                sum_len_name += len(call_digits[i[0]] + 'hundred')
            
            elif (i[1] == '0'):                     # 110
                sum_len_name += len(call_digits[i[0]] + 'hundred' + 'and' + call_digits[i[2]])
            
            elif (i[2] == '0' and int(i[1:]) >= 10): # x > 120
                sum_len_name += len(call_digits[i[0]] + 'hundred' + 'and' + call_tens[i[1]])      
    
            elif 10 < int(i[1:]) < 20: 
                sum_len_name += len(call_digits[i[0]] + 'hundred' + 'and' + call_tens[i[1:]])
    
            else:
                sum_len_name += len(call_digits[i[0]] + 'hundred' + 'and' + call_tens[i[1]] + call_digits[i[2]])
        else:
            sum_len_name += len('onethousand')
    
    return (sum_len_name)

if __name__ == "__main__":
    start = time.process_time()
    print(comp())
    print(f"----- process time : {time.process_time() - start} seconds     -----")

#----- process time : 0.0007769999999999999 seconds     -----







