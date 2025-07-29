def binary_search_recursive(arr, x, low, high):
    if high >=low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, x, low, mid - 1)           
        else:
            return binary_search_recursive(arr, x, mid + 1, high)
    else:
        return -1
    
arr= [2, 3, 4, 10, 40]
x = 10
result = binary_search_recursive(arr, x, 0, len(arr) - 1)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")