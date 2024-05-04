#Largest element in array.

def largest(arr):
    max_val = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

arr = [12, 21, 3, 4, 76, 99, 100]
ans = largest(arr)
print(ans)
