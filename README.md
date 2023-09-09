
# Python Exercises Repository

Welcome to the Python Exercises repository! This repository contains a collection of Python exercises and solutions to help you improve your Python programming skills. Whether you're a beginner or an experienced developer, you can use these exercises to enhance your Python knowledge.

## Table of Contents

- [Getting Started](#getting-started)
- [Exercises](#exercises)
- [Solutions](#solutions)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with these Python exercises, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/infinite-gears/python-exercises.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd python-exercises
   ```

3. Start working on the exercises and improving your Python skills!

## Exercises

In this section, you will find a variety of Python exercises to test and improve your coding skills. Each exercise includes a problem statement and may have one or more example solutions. Choose an exercise, attempt it on your own, and then check the solutions if you need help or want to compare your solution.

<!-- Additional Exercises -->
### Additional Exercises

Feel free to add more exercises to this repository to challenge yourself and others. To contribute additional exercises, please follow the Contributing guidelines below.


### Exercise: Calculate the Fibonacci Sequence

In this exercise, you'll write a Python program to calculate the Fibonacci sequence up to a specified number of terms. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

#### Instructions:

1. Create a Python script named `fibonacci.py`.

2. Write a function `calculate_fibonacci(n)` that takes an integer `n` as input and returns a list containing the first `n` Fibonacci numbers.

3. Implement the function using a loop or recursion.

4. In your `fibonacci.py` script, take user input for the number of terms they want in the Fibonacci sequence.

5. Call the `calculate_fibonacci` function with the user's input and print the resulting list of Fibonacci numbers.

6. Test your program with different values of `n` to verify its correctness.

#### Example:


# fibonacci.py

def calculate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

try:
    n = int(input("Enter the number of Fibonacci terms to calculate: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result = calculate_fibonacci(n)
        print(f"The first {n} Fibonacci numbers are: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


#### Problem Statement

Write a Python function `calculate_fibonacci(n)` that calculates the first `n` numbers in the Fibonacci sequence and returns them as a list.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. In this exercise, consider the Fibonacci sequence to start with 0, 1, 1, 2, 3, 5, ...

#### Example

```python
>>> calculate_fibonacci(5)
[0, 1, 1, 2, 3]

>>> calculate_fibonacci(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

#### Constraints

- The input `n` is a positive integer.
- Your function should handle `n` values up to 100.

#### Notes

- You may use recursion or an iterative approach to solve this problem.
- Consider implementing the function efficiently to handle larger values of `n`.

## Solutions

Solutions to the exercises can be found in the solutions directory of this repository. You can use these solutions to check your work or to learn different ways to solve the exercises.

Below are Python solutions for calculating the Fibonacci sequence:

#### Using Recursion

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_recursive(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

n = int(input("Enter the number of Fibonacci terms to calculate (using recursion): "))
result = fibonacci_recursive(n)
print(f"The first {n} Fibonacci numbers are: {result}")

### Using a Loop to Calculate the Fibonacci Sequence

def fibonacci_loop(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

n = int(input("Enter the number of Fibonacci terms to calculate (using a loop): "))
result = fibonacci_loop(n)
print(f"The first {n} Fibonacci numbers are: {result}")


## Contributing

If you'd like to contribute to this Python Exercises repository, please follow these guidelines:

1. Fork this repository to your GitHub account.

2. Clone your forked repository to your local machine:

   ```bash
   git clone https://github.com/your-username/python-exercises.git
   ```

3. Create a new branch for your contributions:

   ```bash
   git checkout -b feature/add-exercise
   ```

4. Add your new exercises or solutions to the appropriate directories.

5. Commit your changes and push them to your GitHub repository:

   ```bash
   git add .
   git commit -m "Add new exercises"
   git push origin feature/add-exercise
   ```

6. Create a pull request from your forked repository to the main repository.

## License

This repository and its contents are open-source and available under the MIT License. You can find the full license details in the [LICENSE](LICENSE) file.
```

Feel free to add these sections to your Markdown document, and don't forget to include the actual MIT License text in a `LICENSE` file in your repository.
6. Create a pull request from your forked repository to the main repository.
```

