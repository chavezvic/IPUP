try:
    result = 10/2
except ZeroDivisionError:
    print("Division by zero")
else:
    print(f"Result: {result}")
finally:
    print("Cleanup")
