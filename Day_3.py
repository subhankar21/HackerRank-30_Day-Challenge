#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N >=1 and N <= 100:
        if  N%2 == 0:
            if N<6:
                print("Not Weird") 
            elif N > 5 and N < 21:
                print("Weird") 
            elif N > 20:
                print ("Not Weird")
        elif N%2 != 0:
            print("Weird")


        



