#Smallest element in array.

def smallest(arr):
    min_val = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val

arr = [12, 21, 3, 4, 76, 99, 100]
ans = smallest(arr)
print(ans)



def small(arr):
    ans = min(arr)
    return ans

arr = [10, 324, 786, 999, 1000]

print(small(arr))
