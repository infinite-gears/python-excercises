#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # Initialize a variable to store the maximum hourglass sum.
    max_hourglass_sum = -63  # Minimum possible value for a single cell (-9 to 9 for each cell).

    # Iterate through the 2D array to calculate hourglass sums.
    for i in range(4):
        for j in range(4):
            # Calculate the sum of the current hourglass.
            hourglass_sum = (
                arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                arr[i + 1][j + 1] +
                arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            )
            # Update the maximum hourglass sum if necessary.
            max_hourglass_sum = max(max_hourglass_sum, hourglass_sum)

    # Print the maximum hourglass sum.
    print(max_hourglass_sum)
