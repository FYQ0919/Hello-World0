#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    numberp, numbern = 0,0
    for i in range(len(arr)):
        if arr[i] > 0:
           numberp += 1
        elif arr[i] < 0:
           numbern += 1
        numberz = n- numberp - numbern
    print (numberp/n)
    print (numbern/n)
    print (numberz/n) 


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
