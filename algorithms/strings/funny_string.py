#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    n_codes = [ord(l) for l in s]
    i, k = 0, len(n_codes) - 1
    while i < len(n_codes) - 1:
        x = abs(n_codes[i] - n_codes[i + 1])
        y = abs(n_codes[k] - n_codes[k - 1])
        if x != y: return "Not Funny"
        i += 1
        k -= 1
    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
