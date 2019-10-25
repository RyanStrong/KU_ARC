'''
File: tools.py
Author: Thomas Woodruff
Date: 10/23/19
Revision: 0.1
Description: module to store necessary
             helper functions.
'''

# IMPORTS
import math

class median:
    '''
    computes median filter over range of size
    '''
    def __init__(self, size=3):
        '''
        Inputs:
            size  : [3,inf), size of filter
        '''
        self.size = size
        self.medX = math.ceil(size/2)  # compute position of med value

        self.store = []
        self.medArray = []
        for i in range(size-1):
            self.store.append(0)
            self.medArray.append(0)
        self.medArray.append(0)

        self.loop = size + 1

    def run(self,value):
        '''
        Inputs:
            input : value to be filtered

        Function: computes median filter

        Outputs:
            medVal : median value
        '''
        self.store.append(value)
        i = self.loop - 2
        self.medArray[self.loop-i] = self.store[self.loop-2]
        self.medArray[self.loop-i-1] = self.store[self.loop-3]
        self.medArray[self.loop-i-2] = self.store[self.loop-4]

        sortArr = sorted(self.medArray)    # sort the input low to high

        self.loop += 1

        return sortArr[self.medX-1]      # compute median value