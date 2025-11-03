count = 5

def increase_count():
    global count
    count += 1
    print("Inside function:", count)

increase_count()
print("Outside function:", count)
