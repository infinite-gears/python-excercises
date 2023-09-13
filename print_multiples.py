#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    # Loop from 1 to 10 to print the first 10 multiples of n
    for i in range(1, 11):
        result = n * i
        print(f"{n} x {i} = {result}")
