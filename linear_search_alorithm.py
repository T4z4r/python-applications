
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

arr=[4,2,1,7,5]
x=7
result = linear_search(arr, x)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")    
