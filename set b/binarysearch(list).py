def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    for i in range(len(arr)):
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 9
index = binary_search(arr, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the list.")
