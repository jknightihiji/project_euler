#!/usr/bin/env python

#this is the solution for problem #3


from math import sqrt

def generate_primes3(n):
    limit= n
    pp=2     # 2 : the first prime
    ps=[pp]  # add it to prime stack
    pp+=1    # 3 : the second prime
    ps.append(pp) # add 3 to stack
    while pp <= limit:
        pp+=2    # only increment odd number
        test=True
        sqrtpp=sqrt(pp)  # generate of pp**2
        for a in ps:
            if a>sqrtpp: break   # break if greater than complementary primes
            if pp%a==0:
                test=False
                break
        if test: 
            # this is a prime number
            ps.append(pp)
        
        if n % pp == 0 :
            limit = n/pp
            print "limit = %d "% limit
        
    return ps

n = 600851475143
print "starting primes"
primes = generate_primes3(n)

factors = [primes[0]]

for p in primes:
    if n % p == 0 :
        factors.append(p)


print "solution: %d " %( factors[-1] )
