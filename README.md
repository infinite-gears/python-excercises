# Python Exercises Repository

Welcome to the Python Exercises repository! This repository contains a collection of Python exercises and solutions to help you improve your Python programming skills. Whether you're a beginner or an experienced developer, you can use these exercises to enhance your Python knowledge.

# Table of Contents

- [Getting Started](#getting-started)
- [The Power of Python](#the-power-of-python)
- [Exercises](#exercises)
  - [Python Scripts and Exercises](#python-scripts-and-exercises)
    - [Voting Eligibility Checker](#example-voting-eligibility-checker)
    - [Conditional Statements](#exercise-conditional-statements)
    - [Age Classifier](#exercise-age-classifier)
    - [Multiples Printer](#exercise-multiples-printer)
    - [Reverse an Array](#exercise-reverse-an-array)
    - [Factorial and Even/Odd Checker](#exercise-factorial-and-even-odd-checker)
    - [Recursive Factorial](#exercise-recursive-factorial)
    - [Maximum Hourglass Sum Calculator](#exercise-maximum-hourglass-sum-calculator)
    - [Maximum Consecutive Ones](#exercise-maximum-consecutive-ones)
    - [Sum of Two Integers Calculator](#exercise-sum-of-two-integers-calculator)
    - [Maximum Difference](#exercise-maximum-difference) <!-- Added Maximum Difference Exercise Entry -->
    - [Parse String to Integer (Python Script)](#python-script-parse-string-to-integer)
    - [Parse String to Integer - Variant 1 (Python Script)](#python-script-variant-1)
    - [Parse String to Integer - Variant 2 (Python Script)](#python-script-variant-2)
    - [Parse String to Integer - Variant 3 (Python Script)](#python-script-variant-3)
    - [Calculator Script](#calculator-script) <!-- Added Calculator Script Entry -->
  - [Additional Exercises](#additional-exercises)
    - [Minimum Difference](#minimum-difference) <!-- Added Minimum Difference Exercise Entry -->
- [Hourglass Sum Calculator](#hourglass-sum-calculator)
  - [Usage](#usage)
  - [Algorithm](#algorithm)
- [Solutions](#solutions)
  - [Solution: Maximum Consecutive Ones](#solution-maximum-consecutive-ones)
  - [Solution: Maximum Difference](#solution-maximum-difference) <!-- Added Maximum Difference Solution Entry -->
  - [Solution: Minimum Difference](#solution-minimum-difference) <!-- Added Minimum Difference Solution Entry -->
- [Contributing](#contributing)
- [License](#license)



## The Power of Python

Python is a versatile and powerful programming language known for its simplicity and readability. It has gained immense popularity in various domains, including web development, data science, artificial intelligence, and more. Here's why Python is remarkable:

- **Beginner-Friendly:** Python's clean and concise syntax makes it accessible for beginners, allowing them to start coding quickly.

- **Rich Ecosystem:** Python boasts a vast library ecosystem that provides tools and frameworks for a wide range of applications.

- **Cross-Platform:** Python is compatible with major operating systems, ensuring your code works seamlessly across different platforms.

- **Community and Support:** Python has a vibrant community of developers and a wealth of online resources, making it easy to find help and collaborate on projects.

- **Versatility:** Python can be used for web development, automation, scientific computing, data analysis, machine learning, and more.

This series of exercises will introduce you to the fundamentals of Python programming and showcase its power through practical examples and applications.

---

## Exercise: Factorial and Even/Odd Checker

Explain the significance of the `factorial_even_odd.py` script here and how it uses while loops, if statements, and user input to calculate the factorial of a number and determine if it's even or odd. This exercise showcases essential programming concepts and practical applications.

## Explanation of Scripts

### `string_indexing.py`

This Python script deals with indexing and manipulating strings. It takes a string as input and separates its even-indexed and odd-indexed characters into two separate strings. Here's why it's important:

- **String Manipulation:** This script demonstrates how to work with strings, which is a fundamental skill in programming. It shows how to iterate through characters in a string and create new strings based on specific conditions (even and odd indices).

- **Indexing:** Understanding how to access characters at different indices within a string is crucial in various text-processing tasks.

- **Loops and Conditionals:** It uses loops (for iterating through characters) and conditionals (if statements) to perform the task, which are essential programming constructs.

### `factorial_even_odd.py`

This Python script calculates the factorial of a given number and checks whether the result is even or odd. Here's why it's important:

- **Factorial Calculation:** Calculating the factorial of a number is a common mathematical operation. This script demonstrates how to use a while loop to perform repetitive calculations until a certain condition is met.

- **Conditional Statements:** It uses an if statement to check whether the factorial result is even or odd, showcasing the use of conditional logic in programming.

- **User Input:** The script accepts user input, making it interactive and illustrating how to read input from the user.

Both of these scripts provide valuable insights into basic programming concepts and practical applications of loops, conditionals, and string manipulation in Python.

## Getting Started

To get started with these Python exercises, follow these steps:

1. Clone this repository to your local machine:

   ```git clone https://github.com/infinite-gears/python-exercises.git```

2. Navigate to the repository directory:

   ```cd python-exercises```

3. Start working on the exercises and improving your Python skills!

## Python Scripts and Exercises

In this repository, you'll find a collection of Python scripts that cover various simple tasks and exercises. These scripts are designed to help you practice your Python programming skills and understand fundamental concepts.

### Python Scripts

We've included Python scripts for tasks like:

- Data Manipulation: Scripts to manipulate data, such as string operations and list manipulations.

- Mathematics: Scripts for performing basic mathematical operations and solving mathematical problems.

- File Handling: Scripts to read from and write to files, including text and CSV files.

- User Input: Examples of how to take user input and process it in Python.

- Control Structures: Scripts demonstrating the use of control structures like loops and conditionals.

### How to Use

- Clone or Download: You can clone this repository or download the contents to your local machine.

- Explore the PythonScripts Directory: Navigate to the PythonScripts directory to find the Python scripts organized by categories.

- Run the Scripts: Open the scripts in your favorite Python IDE or text editor. You can run them and modify them to experiment with different inputs and scenarios.

## Exercises

In addition to the scripts, we've included exercises to test your understanding of Python concepts. These exercises are located in the Exercises directory.

### Additional Exercises

Feel free to add more exercises to this repository to challenge yourself and others. To contribute additional exercises, please follow the Contributing guidelines below.

#### Exercise: Calculate the Fibonacci Sequence

In this exercise, you'll write a Python program to calculate the Fibonacci sequence up to a specified number of terms. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

**Script Name:** `fibonacci.py`

**Instructions**

1. Create a new Python file named `fibonacci.py`.

2. Write a function `calculate_fibonacci(n)` that takes an integer `n` as input and returns a list containing the first `n` Fibonacci numbers.

3. Implement the function using a loop or recursion.

4. In your `fibonacci.py` script, take user input for the number of terms they want in the Fibonacci sequence.

5. Call the `calculate_fibonacci` function with the user's input and print the resulting list of Fibonacci numbers.

6. Test your program with different values of `n` to verify its correctness.

#### Exercise: Conditional Statements

In this exercise, you'll practice using conditional statements by writing a Python program that determines whether an input integer is "Weird" or "Not Weird" based on specific conditions.

**Script Name:** `weird_or_not_weird.py`

**Instructions**

1. Create a new Python file (e.g., `weird_or_not_weird.py`) for your program.

2. Write a Python program that does the following:

   - Takes an integer input from the user.

   - Determines whether the input is "Weird" or "Not Weird" based on the following conditions:

     - If the input is odd, print "Weird."
     - If the input is even and in the inclusive range of 2 to 5, print "Not Weird."
     - If the input is even and in the inclusive range of 6 to 20, print "Weird."
     - If the input is even and greater than 20, print "Not Weird."

   - Ensure your program handles both positive and negative integers.

3. Test your program with various input values to verify its correctness.

#### Exercise: Age Classifier

In this exercise, you'll write a Python program that classifies a person's age into different categories: infant, child, teenager, adult, or senior.

**Script Name:** `age_classifier.py`

**Instructions**

1. Create a new Python file named `age_classifier.py`.

2. Write a function `classify_age(age)` that takes an integer `age` as input and returns a string indicating the age category. Use the following criteria:

   - If the age is 0 or negative, return "Invalid Age."
   - If the age is less than 1, return "Infant."
   - If the age is between 1 and 12 (inclusive), return "Child."
   - If the age is between 13 and 19 (inclusive), return "Teenager."
   - If the age is between 20 and 64 (inclusive), return "Adult."
   - If the age is 65 or older, return "Senior."

3. In your `age_classifier.py` script, take user input for their age and call the `classify_age` function to determine and print their age category.

4. Test your program with different age values to verify its correctness.

#### Exercise: Multiples Printer

In this exercise, you'll write a Python program that prints the multiples of a given number within a specified range.

**Script Name:** `multiples_printer.py`

**Instructions**

1. Create a new Python file named `multiples_printer.py`.

2. Write a function `print_multiples(n, start, end)` that takes three integers as input: `n`, `start`, and `end`. The function should print all multiples of `n` within the range from `start` to `end` (inclusive).

3. In your `multiples_printer.py` script, take user input for `n`, `start`, and `end`, and call the `print_multiples` function to print the multiples.

4. Test your program with different inputs to verify its correctness.

#### Exercise: Reverse an Array

In this exercise, you'll write a Python program to reverse an array of integers.

**Script Name:** `reverse_array.py`

**Instructions**

1. Create a new Python file named `reverse_array.py`.

2. Write a function `reverse_list(arr)` that takes a list of integers `arr` as input and returns a new list with the elements reversed. Do not use built-in functions like `reverse()`.

3. In your `reverse_array.py` script, take user input for a list of integers, call the `reverse_list` function to reverse the list, and print the reversed list.

4. Test your program with different lists of integers to verify its correctness.

#### Exercise: Factorial and Even/Odd Checker

In this exercise, you'll write a Python program that calculates the factorial of a given number and checks whether it's even or odd.

**Script Name:** `factorial_even_odd.py`

**Instructions**

1. Create a new Python file named `factorial_even_odd.py`.

2. Write a function `calculate_factorial(n)` that takes an integer `n` as input and returns its factorial. Use a while loop for the calculation.

3. Write a function `is_even(num)` that takes an integer `num` as input and returns `True` if it's even and `False` if it's odd.

4. In your `factorial_even_odd.py` script, take user input for a positive integer `n`.

5. Call the `calculate_factorial` function to calculate the factorial of `n`.

6. Call the `is_even` function to check if the factorial is even or odd.

7. Print the factorial and whether it's even or odd.

8. Test your program with different values of `n` to verify its correctness.

#### Exercise: Recursive Factorial

In this exercise, you'll write a Python program to calculate the factorial of a given number using recursion.

**Script Name:** `recursive_factorial.py`

**Instructions**

1. Create a new Python file named `recursive_factorial.py`.

2. Write a function `calculate_factorial_recursive(n)` that takes an integer `n` as input and returns its factorial using recursion.

3. In your `recursive_factorial.py` script, take user input for a positive integer `n`.

4. Call the `calculate_factorial_recursive` function to calculate the factorial of `n`.

5. Print the factorial.

6. Test your program with different values of `n` to verify its correctness.

#### Exercise: Maximum Hourglass Sum Calculator

In this exercise, you'll write a Python program to find the maximum hourglass sum in a 2D array.

**Script Name:** `hourglass_sum.py`

**Instructions**

1. Create a new Python file named `hourglass_sum.py`.

2. Write a function `find_max_hourglass_sum(arr)` that takes a 2D list `arr` as input and returns the maximum hourglass sum. An hourglass in the 2D array is defined as a subset of values with the following shape:


For example, in the 2D array:


The maximum hourglass sum is `19`, which corresponds to the hourglass:


3. In your `hourglass_sum.py` script, create a 2D list to represent the array and populate it with values.

4. Call the `find_max_hourglass_sum` function to calculate and print the maximum hourglass sum.

5. Test your program with different 2D arrays to verify its correctness.

#### Exercise: Maximum Consecutive Ones

In this exercise, you'll write a Python program to find the maximum number of consecutive ones in a binary sequence.

**Script Name:** `max_consecutive_ones.py`

**Instructions**

1. Create a new Python file named `max_consecutive_ones.py`.

2. Write a function `find_max_consecutive_ones(nums)` that takes a list of integers `nums`, where each integer is either `0` or `1`, as input. The function should return the maximum number of consecutive ones in the list.

3. In your `max_consecutive_ones.py` script, take user input for a list of integers, ensuring that the input only contains `0` and `1` values.

4. Call the `find_max_consecutive_ones` function to calculate and print the maximum number of consecutive ones.

5. Test your program with different input lists to verify its correctness.

#### Exercise: Sum of Two Integers Calculator

In this exercise, you'll write a Python program that calculates the sum of two integers without using the `+` or `-` operators.

**Script Name:** `sum_of_integers.py`

**Instructions**

1. Create a new Python file named `sum_of_integers.py`.

2. Write a function `calculate_sum(a, b)` that takes two integers `a` and `b` as input and returns their sum without using the `+` or `-` operators.

3. In your `sum_of_integers.py` script, take user input for two integers and call the `calculate_sum` function to calculate and print the sum.

4. Test your program with different integer inputs to verify its correctness.

#### Exercise: Book Inheritance (Python Program)

In this exercise, you'll create a Python program to model inheritance among different types of books.

**Script Name:** `book_inheritance.py`

**Instructions**

1. Create a new Python file named `book_inheritance.py`.

2. Define a class `Book` with the following attributes and methods:

- Attributes:
  - `title` (string): The title of the book.
  - `author` (string): The author of the book.
- Methods:
  - `__init__(self, title, author)`: Initializes a new `Book` instance with the given `title` and `author`.
  - `display(self)`: Prints the title and author of the book in the following format: `"Title: {title}, Author: {author}"`.

3. Define a class `eBook` that inherits from the `Book` class with the following additional attributes and methods:

- Attributes:
  - `file_size` (string): The file size of the eBook.
- Methods:
  - `__init__(self, title, author, file_size)`: Initializes a new `eBook` instance with the given `title`, `author`, and `file_size`.
  - `display(self)`: Overrides the `display` method of the parent class to also print the file size in the following format: `"Title: {title}, Author: {author}, File Size: {file_size}"`.

4. In your `book_inheritance.py` script, create instances of both the `Book` and `eBook` classes and demonstrate the use of the `display` method for both.

5. Test your program to verify its correctness.

#### Exercise: Maximum Difference

In this exercise, you'll write a Python function to find the maximum difference between any two elements in an integer list.

**Script Name:** `max_difference.py`

**Instructions**

1. Create a new Python file named `max_difference.py`.

2. Write a function `find_max_difference(nums)` that takes a list of integers `nums` as input and returns the maximum difference between any two elements in the list.

3. In your `max_difference.py` script, take user input for a list of integers.

4. Call the `find_max_difference` function to calculate and print the maximum difference.

5. Test your program with different input lists to verify its correctness.

#### Exercise: Parse String to Integer (Python Script)

In this exercise, you'll write a Python script to parse a string containing an integer and convert it to an integer data type.

**Script Name:** `parse_string_to_integer.py`

**Instructions**

1. Create a new Python file named `parse_string_to_integer.py`.

2. Write a script that does the following:

- Takes user input for a string containing an integer value (e.g., `"123"`).

- Parses the input string and converts it to an integer data type.

- Prints the integer value.

3. Test your script with different input strings to verify its correctness.

#### Exercise: Parse String to Integer - Variant 1 (Python Script)

In this exercise, you'll write a Python script to parse a string containing an integer and convert it to an integer data type. However, this time, you'll handle cases where the string may contain leading or trailing whitespace characters.

**Script Name:** `parse_string_to_integer_variant1.py`

**Instructions**

1. Create a new Python file named `parse_string_to_integer_variant1.py`.

2. Write a script that does the following:

- Takes user input for a string that may contain an integer value with optional leading or trailing whitespace characters (e.g., `"  123  "`).

- Parses the input string, removing any leading or trailing whitespace characters, and converts it to an integer data type.

- Prints the integer value.

3. Test your script with different input strings, including those with leading or trailing whitespace, to verify its correctness.

#### Exercise: Parse String to Integer - Variant 2 (Python Script)

In this exercise, you'll write a Python script to parse a string containing an integer and convert it to an integer data type. This time, you'll handle cases where the string may contain non-numeric characters.

**Script Name:** `parse_string_to_integer_variant2.py`

**Instructions**

1. Create a new Python file named `parse_string_to_integer_variant2.py`.

2. Write a script that does the following:

- Takes user input for a string that may contain an integer value with optional non-numeric characters (e.g., `"12abc34"`).

- Parses the input string, extracting the first contiguous sequence of numeric characters, and converts it to an integer data type.

- Prints the integer value.

3. Test your script with different input strings, including those with non-numeric characters, to verify its correctness.

#### Exercise: Parse String to Integer - Variant 3 (Python Script)

In this exercise, you'll write a Python script to parse a string containing an integer and convert it to an integer data type. This time, you'll handle cases where the string may contain leading plus or minus signs.

**Script Name:** `parse_string_to_integer_variant3.py`

**Instructions**

1. Create a new Python file named `parse_string_to_integer_variant3.py`.

2. Write a script that does the following:

- Takes user input for a string that may contain an integer value with an optional leading plus (`+`) or minus (`-`) sign (e.g., `"-123"` or `"+456"`).

- Parses the input string, considering the leading sign (if present), and converts it to an integer data type.

- Prints the integer value.

3. Test your script with different input strings, including those with leading plus or minus signs, to verify its correctness.

---

## Hourglass Sum Calculator

The `hourglass_sum.py` script calculates the maximum hourglass sum in a 2D array. It defines a function `find_max_hourglass_sum(arr)` that takes a 2D list `arr` as input and returns the maximum hourglass sum.

### Usage

To use the `hourglass_sum.py` script:

1. Ensure you have Python installed on your system.

2. Create a 2D list representing the array you want to analyze. The list should contain integer values.

3. Call the `find_max_hourglass_sum(arr)` function, passing your 2D list as an argument.

4. The function will return the maximum hourglass sum, which you can print or use as needed.

### Algorithm

The `find_max_hourglass_sum` function iterates through the 2D array, focusing on each possible hourglass shape within the array. For each hourglass, it calculates the sum of its values and keeps track of the maximum sum found so far. The function uses nested loops to visit each cell in the array, ensuring that it considers all possible hourglasses.

This algorithm allows the script to efficiently find the maximum hourglass sum within the given 2D array.

---

## Solutions

In this section, you'll find solutions to some of the exercises presented earlier. These solutions are provided to help you understand how to approach and solve the exercises.

### Solution: Maximum Consecutive Ones

Here's a solution for the "Maximum Consecutive Ones" exercise:

```python
def find_max_consecutive_ones(nums):
 max_count = 0
 current_count = 0

 for num in nums:
     if num == 1:
         current_count += 1
     else:
         # Update the maximum count if the current count is greater
         max_count = max(max_count, current_count)
         current_count = 0

 # Update the maximum count one more time in case the sequence ends with 1s
 max_count = max(max_count, current_count)

 return max_count
```
# Example usage:
nums = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
max_ones = find_max_consecutive_ones(nums)
print("Maximum Consecutive Ones:", max_ones)

def find_max_difference(nums):
    if not nums or len(nums) < 2:
        return None

    min_num = nums[0]
    max_diff = nums[1] - nums[0]

    for num in nums[1:]:
        if num - min_num > max_diff:
            max_diff = num - min_num
        if num < min_num:
            min_num = num

    return max_diff

# Example usage:
nums = [2, 3, 10, 6, 4, 8, 1]
max_diff = find_max_difference(nums)
print("Maximum Difference:", max_diff)


## Calculator Script Exercise

### Exercise Description

**Objective:** In this exercise, you will create a Python script for a simple calculator. The script should define a `Calculator` class with a `power` method that calculates the power of a number. However, the method must throw an exception if either of the input numbers is negative.

## Calculator Script Exercise

### Exercise Description

**Objective:** In this exercise, you will create a Python script for a simple calculator. The script should define a `Calculator` class with a `power` method that calculates the power of a number. However, the method must throw an exception if either of the input numbers is negative.

**Instructions:**

1. Create a Python script that defines a `Calculator` class.

2. Inside the `Calculator` class, define a `power` method that takes two integers `n` and `p` as parameters.

3. Implement the `power` method such that it calculates and returns `n` raised to the power of `p`.

4. Add error handling to the `power` method: If either `n` or `p` is negative, raise an exception with the message: "n and p should be non-negative."

5. Write test cases to verify that the `power` method works as expected, both for valid inputs and when an exception is raised.

### Why This Exercise?

This exercise helps you practice exception handling in Python. It also reinforces your understanding of defining classes and methods, as well as writing test cases to ensure your code behaves as intended.

[Back to Table of Contents](#table-of-contents)



# Contributing and License

```plaintext
Contributions to this Python Exercises repository are welcome! If you'd like to add more exercises, improve existing ones, or suggest new features or improvements, please follow these guidelines:

1. Fork this repository.
2. Create a new branch for your contributions.
3. Make your changes, add new exercises, or make improvements to existing ones.
4. Test your changes to ensure they work as expected.
5. Commit your changes and create a descriptive commit message.
6. Push your changes to your forked repository.
7. Create a pull request to merge your changes into this repository.
```

# License

This Python Exercises repository is licensed under the MIT License. You are free to use, modify, and distribute the content for personal or educational purposes.

Happy coding, and enjoy improving your Python skills!
