#largest element by using sort()

def largest(arr,n):
    arr.sort()

    return arr[0]

arr = [123,32,33,56,88,1]
n= len(arr)
ans = largest(arr,n)

print(ans)