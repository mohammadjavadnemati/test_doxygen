## This class performs various mathematical operations such as addition, subtraction, multiplication, division, etc.
# @class Calculator
    
class Calculator:
    

       
    ## Adds two numbers.
    # @param a The first number.
    # @param b The second number.
    # @return The sum of a and b.
    ##
    def add(self, a, b):
        return a + b

    ## Subtracts two numbers.
    # @param a The first number.
    # @param b The second number.
    # @return The result of subtracting b from a.
    ##
    def subtract(self, a, b):  
        
        
        return a - b

    ## Multiplies two numbers.
    # @param a The first number.
    # @param b The second number.
    # @return The product of a and b.
    ##
    def multiply(self, a, b):  
      
      
        return a * b

    ## Divides two numbers.
    # @param a The numerator.
    # @param b The denominator.
    # @throws ValueError If b is zero.
    # @return The result of dividing a by b.
    def divide(self, a, b): 
       
        
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    ## Raises a to the power of b.
    # @param a The base number.
    # @param b The exponent.
    # @return The result of a raised to the power of b.
    def power(self, a, b):  
        
        
        return a ** b

    ## Calculates the factorial of a number.
    # @param n The input number.
    # @throws ValueError If n is negative.
    # @return The factorial of n.
    def factorial(self, n):  
        
        
        if n < 0:
            raise ValueError("Factorial does not exist for negative numbers")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    ## Calculates the square root of a number.
    # @param a The input number.
    # @throws ValueError If a is negative.
    # @return The square root of a.
    def sqrt(self, a):  
        
        
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return a ** 0.5

    ## Sums the elements of a list of numbers.
    # @param numbers A list of numeric values.
    # @throws ValueError If any element of the list is not a number.
    # @return The sum of the elements in the list.
    def sum_of_numbers(self, numbers):  
        
        
        if not all(isinstance(x, (int, float)) for x in numbers):
            raise ValueError("All elements must be numbers")
        return sum(numbers)

    ## Checks if a number is prime.
    # @param n The input number.
    # @return True if the number is prime, False otherwise.
    def is_prime(self, n):  
        
        
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
