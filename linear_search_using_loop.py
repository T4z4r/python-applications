def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr=[4, 2, 3, 7, 5]
x= 7
result = linear_search(arr, x)

if result != -1:
    print(f"Element {x} found at index {result}")
else:
    print(f"Element {x} not found in the array")