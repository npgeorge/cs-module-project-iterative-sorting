def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    if left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return True

        if arr[middle] < target:
            return binary_search(arr[middle + 1:], target)
        elif arr[middle] > target:
            return binary_search(arr[:middle], target)

    return -1
