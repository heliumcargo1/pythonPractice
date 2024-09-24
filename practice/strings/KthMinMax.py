arr = [3, 2, 1, 5, 4]
k =2

def kthMaxMin(arr,k):
    arr.sort()
    n = len(arr)
    minK = arr[k-1]
    maxK = arr[-k]
    return (minK, maxK )
    
a,b = kthMaxMin(arr,k)
print(a)
print(b)

# arr.sort()
# n = len(arr)
# print(n)
