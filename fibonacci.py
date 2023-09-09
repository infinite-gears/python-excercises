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
