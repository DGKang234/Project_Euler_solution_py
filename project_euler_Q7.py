'''
Q7 - 1000st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
def comp():
    prime_list = lambda x:[i for i in range(2, x+1) if all([i % x for x in range(2, int(i**0.5+1))])][10000]
    print (prime_list(120000))

    return None


import time
if __name__ == "__main__":
    start = time.process_time()
    print(comp())
    print(f"----- process time : {time.process_time() - start} seconds -----")



# ----- process time : 0.663118 seconds -----

