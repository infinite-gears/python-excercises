# Exercise: Minimum Difference

# Objective:
# In this exercise, you will work with arrays in Python.
# Your goal is to find the minimum difference between any two elements in a given array.

# Instructions:
# You are given an array of integers.
# Write a function `minimum_difference(arr)` that takes the array as input and returns the minimum difference between any two elements in the array.

# Example:
# Input: [3, 8, 10, 23, 5]
# Output: 2 (The minimum difference is between 3 and 5)

# Input: [1, 5, 7, 9, 12]
# Output: 2 (The minimum difference is between 5 and 7)

# Input: [7, 21, 33, 44, 6]
# Output: 1 (The minimum difference is between 33 and 44)

# You can assume that the input array contains at least two elements.

def minimum_difference(arr):
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize the minimum difference as infinity
    min_diff = float('inf')
    
    # Iterate through the array and find the minimum difference
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    
    return min_diff

# Test cases
arr1 = [3, 8, 10, 23, 5]
print("Minimum Difference:", minimum_difference(arr1))

arr2 = [1, 5, 7, 9, 12]
print("Minimum Difference:", minimum_difference(arr2))

arr3 = [7, 21, 33, 44, 6]
print("Minimum Difference:", minimum_difference(arr3))
