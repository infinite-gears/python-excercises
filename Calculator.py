class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        # Initialize the sum to 0
        total_sum = 0
        
        # Iterate from 1 to n (inclusive)
        for i in range(1, n + 1):
            # If 'i' is a divisor of 'n', add it to the sum
            if n % i == 0:
                total_sum += i
        
        # Return the sum of divisors
        return total_sum

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
