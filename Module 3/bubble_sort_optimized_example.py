arr = [64, 25, 120, 22, 11, 1000, 999999, 4]
n = len(arr)
for i in range(n):
    # Flag to optimize: if no swaps are made in a pass, the list is sorted
    swapped = False
      # Traverse through the list, up to n-i-1 because the last i elements are already sorted
    for j in range(0, n-i-1):
        # Compare adjacent elements
        if arr[j] > arr[j+1]:
            # Swap them
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
        # If no swaps were made in this pass, the list is sorted
    if not swapped:
        break
print("Sorted list:", arr)
