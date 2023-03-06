'''
uniqueSteps.py: Python program to calculate number of unique ways to climb N stairs
given that you can climb either 1 or 2 steps at a time
'''
import numpy as np

# Function args #
#################
# N : number of stairs

# Return value #
################
# returns an integer

def uniqueWays(n):
    # array of size n+1 to keep track of unique ways for each step
    steps = np.zeros(shape=n+1, dtype=np.int64)

    # initializing base cases
    # when n: 0, 1
    # only 1 way to climb stairs
    steps[0] = 1
    steps[1] = 1

    # For other values of n 
    # we iterate over array to calculate number of ways at current step
    # by summing number of ways to climb previous one or two steps
    # which covers all possible ways to reach current step
    for i in range(2,len(steps)):
        steps[i] = steps[i-1] + steps[i-2]
    
    # return the value at nth step
    return steps[n]

# for n = 4
print(uniqueWays(4))
