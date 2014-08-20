#!/usr/bin/env python

#this is the solution for problem #10

from math import sqrt

def generate_primes3(n):
    pp=2     # 2 : the first prime
    ps=[pp]  # add it to prime stack
    pp+=1    # 3 : the second prime
    ps.append(pp) # add 3 to stack
    while pp <= n:
        pp+=2    # only increment odd number
        test=True
        sqrtpp=sqrt(pp)  # generate of pp**2
        for a in ps:
            if a>sqrtpp: break   # break if greater than complementary primes
            if pp%a==0:
                test=False
                break
        if test: 
            ps.append(pp)
            if pp % 1000 == 0 :
                print pp
        
    return ps

n = 2000000
primes = generate_primes3(n)

print "solution: %d " % sum(primes)
