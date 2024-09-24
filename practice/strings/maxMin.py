arr = [3, 5, 1, 8, 4]

def findArr(arr):
    max_arr = arr[0]
    min_arr = arr[0]
    for i in arr :
        if i > max_arr:
            max_arr = i
        if i < min_arr:
            min_arr = i
    return max_arr,min_arr

a, b = findArr(arr)

print(f"Maximum value: {a}")
print(f"Minimum value: {b}")