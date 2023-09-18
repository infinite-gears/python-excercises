#!/bin/python3

import math
import os
import random
import re
import sys

def max_consecutive_ones(n):
    binary_str = bin(n)[2:]  # Convert to binary and remove the '0b' prefix
    max_consecutive = 0
    current_consecutive = 0

    for char in binary_str:
        if char == '1':
            current_consecutive += 1
            max_consecutive = max(max_consecutive, current_consecutive)
        else:
            current_consecutive = 0

    return max_consecutive

if __name__ == '__main__':
    n = int(input().strip())
    result = max_consecutive_ones(n)
    print(result)
