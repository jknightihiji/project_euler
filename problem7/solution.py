#!/usr/bin/env python

#this is the solution for problem #7

from math import sqrt

n = 10001

def is_prime(a,primes) :
    if a in primes :
        return False
    else : 
        return True

def generate_primes3(n):
   pp=2     # 2 : the first prime
   ps=[pp]  # add it to prime stack
   pp+=1    # 3 : the second prime
   ps.append(pp) # add 3 to stack
   while len(set(ps)) <= n:
       pp+=2    # only increment odd number
       test=True
       sqrtpp=sqrt(pp)  # generate of pp**2
       for a in ps:
           if a>sqrtpp: break   # break if greater than complementary primes
           if pp%a==0:
               test=False
               break
       if test: ps.append(pp)
   return ps

primes = generate_primes3(n)

    
