def find_positive(numbers):
    for num in numbers:
        if num > 0:
            return num  # Exit early when a positive is found
    return None  # If no positives, return None

result = find_positive([-1, -2, -3, 100, -4, 5])
print(result)
