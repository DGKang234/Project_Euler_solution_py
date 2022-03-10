'''
Q7 - 1000st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

def comp(num):
    prime_list = lambda x:[i for i in range(2, x+1) if all([i % x for x in range(2, int(i**0.5+1))])][10000]
    print (prime_list(num))

import time
if __name__ == "__main__":
    start = time.process_time()
    print(comp(120000))
    print(f"----- process time : {time.process_time() - start} seconds -----")

# ----- process time : 0.663118 seconds -----


# ==================================================


def PrimeChecker(n):
    if n < 2: return "Neither prime, nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# returns the nth prime number
def PrimeOrder(n):
    numberOfPrimes = 0
    p = 1

    while numberOfPrimes < n:
        p += 1
        if PrimeChecker(p):
            numberOfPrimes += 1
    return p

start = time.process_time()
print(PrimeOrder(10001))
print(f"----- process time : {time.process_time() - start} seconds -----")

#----- process time : 0.093947 seconds -----
