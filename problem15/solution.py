#!/usr/bin/env python

#this is the solution for problem #15

import numpy as np


grid = np.zeros((21,21),dtype=int)
#grid = np.zeros((5,5),dtype=int)

for i in range(len(grid)):
    for j in range(len(grid[i])):   
        if i == 0 :
            grid[i][j] = 1
            continue

        if j == 0 :
            grid[i][j] = 1
            continue

        grid[i][j] = (grid[i-1][j] + grid[i][j-1])



        
print grid
print grid[-1][-1]





