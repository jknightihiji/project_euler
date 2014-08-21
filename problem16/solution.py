#!/usr/bin/env python

#this is the solution for problem #16


def sum_of_digits(n) :
    s = str(n)
    l = []
    for i in s :
        l.append(int(i))

    return sum(l)


print "solution: %d" % sum_of_digits(2**1000)
