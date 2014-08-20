#!/usr/bin/env python

#this is the solution for problem #9

import sys

def is_py_triplet(a,b,c) :
    """ asserts that a,b,c are pythangorean triplets"""
    try :
        assert(a**2 + b**2 == c**2)
        return True
    except :
        return False

def is_sum_valid(a,b,c):
    ''' asserts that a+b+c==1000'''
    try :
        assert( a+b+c == 1000)
        return True
    except:
        return False

def greater(a,b,c):
    ''' asserts a < b < c '''
    try :
        assert(a < b < c)
        return True
    except :
        return False

is_solution = False
a = 1
b = 2
c = 3
for i in range(a,1000) :
    a = i
    b = a+1 
    c = b+1
    for j in range(b,1000) :
        b = j
        c = b+1
        for k in range(c,1000) :
            c = k
            total = a+b+c
            if not a+b+c == 1000 :
                continue
            print "(%d,%d,%d = %d)"%(a,b,c,total)
            if not is_py_triplet(a,b,c) :
                continue
            if not is_sum_valid(a,b,c) :
                continue
            if not greater(a,b,c) :
                continue
            is_solution = True
            print "solution : (%d,%d,%d = %d)"%(a,b,c,total)
            sys.exit(0)


