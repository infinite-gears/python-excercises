#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    # Reverse the array and print it
    reversed_arr = arr[::-1]
    print(" ".join(map(str, reversed_arr)))
