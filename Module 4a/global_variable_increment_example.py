count = 0

def increment_count():
    global count  # Use the 'global' keyword to modify the global variable.
    count += 1

increment_count()
print(count)  # The global variable count has been modified to 1.
