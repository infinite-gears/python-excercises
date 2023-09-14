# Function to calculate factorial
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

# Read an integer from the user
num = int(input("Enter an integer: "))

# Calculate factorial
fact = factorial(num)

# Check if the factorial is even or odd
if fact % 2 == 0:
    print(f"{fact} is even.")
else:
    print(f"{fact} is odd.")
