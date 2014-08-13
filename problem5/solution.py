#!/usr/bin/env python

i = 1 
while True :
    valid = 0 
    for divisor in range(20,0,-1) :
        if i % divisor == 0 :
            valid = 1 
        else :
            valid = 0
            break
    if valid == 1 :
        print "answer: "+str(i)
        break
    i+=1 
