#!/bin/python3

import math
import os
import random
import re
import sys

def count_swaps(arr):
    n = len(arr)
    swaps = 0

    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return swaps

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    num_swaps = count_swaps(a)

    print(f"Array is sorted in {num_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
