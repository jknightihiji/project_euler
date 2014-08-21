#!/usr/bin/env python

#this is the solution for problem #14


def collatz_seq(n):
    i = n 
    seq = [i]
    while i > 1:
        if i % 2 == 0 :
            i = i/2
        else :
            i = 3*i + 1
        seq.append(i)
    return seq

longest_seq = 0
starting_value = 0
for i in range(1,1000000):
    
    seq = collatz_seq(i)
    
    length = len(seq)
    if length > longest_seq :
        longest_seq = length
        starting_value = i


print "solution: i= %d  with length %d " % (starting_value,longest_seq)


