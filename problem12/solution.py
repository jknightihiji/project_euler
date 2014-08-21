#!/usr/bin/env python

#this is the solution for problem #12


from math import sqrt 

def triangle_number(n):
    return sum(range(1,n+1))

def find_divisors(n):
    divisors = [1,n]
    i = 2
    while i < sqrt(n) :
        if n % i == 0 :
            divisors.append(i)
            divisors.append(n/i)
        i+=1

    #print "%d  has divisor count:  %d " % (n,len(divisors))
    return divisors


i = 1

most_divisors = 0
while 1 :
    t = triangle_number(i)
    #print "%dth | t: %d" % (i,t)

    d = find_divisors(t)
    l = len(d)
    if l > most_divisors :
        print "most divisors found: %d " % l
        most_divisors = l 

    if i % 1000 == 0 :
        print "i = %d" % i

    if l > 500:
        print "solution: %d" % t
        break
    i+=1



