def factorial(n):
    # Base case: If n is 0 or 1, return 1.
    if n == 0 or n == 1:
        return 1
    # Recursive case: Multiply n by the factorial of (n-1).
    else:
        return n * factorial(n - 1)

result = factorial(4)  # Calculates 4! (4 factorial)
print(result)  # Output: 24
