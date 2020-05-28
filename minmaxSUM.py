#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    S = sum(arr)
    MAXsum = S - min(arr)
    MINsum = S - max(arr)
    print (MINsum, MAXsum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
