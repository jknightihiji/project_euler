#!/usr/bin/env python

#this is the solution for problem #


def sum_of_squares(a,b):
    '''
    calculates the sum of sqares between a and b
    '''
    total = 0
    for i in  range(a,b+1) :
        total+=i**2

    return total

def sum_of_the_squares(a,b):
    '''
    calculates the sum of all number between a and b, squared
    '''
    total = 0
    for i in  range(a,b+1) :
        total+=i
    
    return total**2


diff = sum_of_the_squares(1,100) - sum_of_squares(1,100)

print "answer: "+str(diff)
