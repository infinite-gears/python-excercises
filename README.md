# Python Exercises Repository

Welcome to the Python Exercises repository! This repository contains a collection of Python exercises and solutions to help you improve your Python programming skills. Whether you're a beginner or an experienced developer, you can use these exercises to enhance your Python knowledge.

# Table of Contents

- [Getting Started](#getting-started)
- [Exercises](#exercises)
  - [Python Scripts and Exercises](#python-scripts-and-exercises)
    - [Example: Voting Eligibility Checker](#example-voting-eligibility-checker)
    - [Exercise: Conditional Statements](#exercise-conditional-statements)
    - [Exercise: Age Classifier](#exercise-age-classifier)
    - [Exercise: Multiples Printer](#exercise-multiples-printer) <!-- Added Exercise Entry -->
  - [Additional Exercises](#additional-exercises) <!-- Added Additional Exercises Entry -->
- [Solutions](#solutions)
- [Contributing](#contributing)
- [License](#license)


## Getting Started

To get started with these Python exercises, follow these steps:

1. Clone this repository to your local machine:

     ```git clone https://github.com/infinite-gears/python-exercises.git```
   
2. Navigate to the repository directory:

   ```cd python-exercises```

3.     Start working on the exercises and improving your Python skills!

## Python Scripts and Exercises

In this repository, you'll find a collection of Python scripts that cover various simple tasks and exercises. These scripts are designed to help you practice your Python programming skills and understand fundamental concepts.
Python Scripts

We've included Python scripts for tasks like:

    Data Manipulation: Scripts to manipulate data, such as string operations and list manipulations.

    Mathematics: Scripts for performing basic mathematical operations and solving mathematical problems.

    File Handling: Scripts to read from and write to files, including text and CSV files.

    User Input: Examples of how to take user input and process it in Python.

    Control Structures: Scripts demonstrating the use of control structures like loops and conditionals.

## How to Use

    Clone or Download: You can clone this repository or download the contents to your local machine.

    Explore the PythonScripts Directory: Navigate to the PythonScripts directory to find the Python scripts organized by categories.

    Run the Scripts: Open the scripts in your favorite Python IDE or text editor. You can run them and modify them to experiment with different inputs and scenarios.

## Exercises

In addition to the scripts, we've included exercises to test your understanding of Python concepts. These exercises are located in the Exercises directory.
Additional Exercises

Feel free to add more exercises to this repository to challenge yourself and others. To contribute additional exercises, please follow the Contributing guidelines below.
Exercise: Calculate the Fibonacci Sequence

In this exercise, you'll write a Python program to calculate the Fibonacci sequence up to a specified number of terms. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

Script Name: fibonacci.py
Instructions

    Create a new Python file named fibonacci.py.

    Write a function calculate_fibonacci(n) that takes an integer n as input and returns a list containing the first n Fibonacci numbers.

    Implement the function using a loop or recursion.

    In your fibonacci.py script, take user input for the number of terms they want in the Fibonacci sequence.

    Call the calculate_fibonacci function with the user's input and print the resulting list of Fibonacci numbers.

    Test your program with different values of n to verify its correctness.

## Exercise: Conditional Statements

In this exercise, you'll practice using conditional statements by writing a Python program that determines whether an input integer is "Weird" or "Not Weird" based on specific conditions.

Script Name: weird_or_not_weird.py
Instructions

    Create a new Python file (e.g., weird_or_not_weird.py) for your program.

    Write a Python program that does the following:
        Takes an integer input from the user.
        Determines whether the input is "Weird" or "Not Weird" following the conditions mentioned earlier.
        Prints the result.

    Test your program with different inputs to ensure it behaves correctly.

## Exercise: Age Classifier

In this exercise, you will write a Python script named "age_classifier.py" to classify a person's age into different categories based on specific conditions. The script will take an integer representing a person's age as input and determine whether the person is young, a teenager, or old. Follow these steps to complete the exercise.

Script Name: age_classifier.py
Instructions

    Create a new Python file named "age_classifier.py" in your repository.
    Inside "age_classifier.py," define a Person class with the following methods:

        __init__(self, initialAge): A constructor that takes an integer initialAge as a parameter. It should check if initialAge is negative. If initialAge is negative, set the age to 0 and print "Age is not valid, setting age to 0." Otherwise, set the age to initialAge.

        amIOld(self): A method that performs age-related checks and prints one of the following messages based on the age:
            If the age is less than 13, print "You are young."
            If the age is between 13 and 17 (inclusive), print "You are a teenager."
            If the age is 18 or older, print "You are old."

        yearPasses(self): A method that increments the age of the person by 1.

    After defining the Person class and its methods, implement the following logic in your script:

        Read the number of test cases, t, from the user.

        For each test case, read an integer representing a person's age from the user.

        Create a Person object with the given age and use the amIOld method to print the appropriate message based on the age.

        Call the yearPasses method three times to simulate three years passing and then call the amIOld method again to print the updated age category.

    Test your "age_classifier.py" script with different inputs to ensure it behaves correctly.

    Share your code and the results of your tests in this repository.

## Exercise: Multiples Printer

### Problem Statement

You are given an integer `n`. Your task is to write a Python script that prints the first 10 multiples of `n` in the following format:

n x 1 = result
n x 2 = result
n x 3 = result
...
n x 10 = result


Implement this in a Python script and make sure to use a loop to generate the multiples.

### Example

If the input is `3`, the output should be:

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30


### Explanation

- You need to read an integer `n` as input.
- Then, use a loop to calculate and print the first 10 multiples of `n` in the specified format.

### Starter Code

```python
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    # Your code goes here
```

**Contributing**

If you'd like to contribute to this Python Exercises repository, please follow these guidelines:

1. Fork this repository to your GitHub account.
2. Clone your forked repository to your local machine:
    
  ```
  git clone https://github.com/your-username/python-exercises.git
```


  Create a new branch for your contributions:
  
```
git checkout -b feature/add-exercise
```

Add your new exercises or solutions to the appropriate directories.

Commit your changes and push them to your GitHub repository:

```
git add .
```
```
git commit -m "Add new exercises"
```
```
git push origin feature/add-exercise
```
    Create a pull request from your forked repository to the main repository.

**License**

This repository and its contents are open-source and available under the MIT License. You can find the full license details in the LICENSE file.
