try:
    result = int("abc")
except ValueError:
    print("Invalid integer")
except TypeError:
    print("Type error occurred")
