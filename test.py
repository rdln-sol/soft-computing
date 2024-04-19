def lower_bound(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def lower_bound_float(arr, target):
    index = lower_bound(arr, int(target))
    if index < len(arr) and arr[index] == target:
        return index
    return index

# Example usage:
arr = [1, 2, 3, 4, 4, 4, 5, 6]
target = 3.5
result = lower_bound_float(arr, target)
print("Lower bound index of", target, "in the array is:", result)
