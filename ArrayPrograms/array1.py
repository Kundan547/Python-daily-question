def _sum(arr):

    sum = 0

    for i in arr:
        sum = sum + i

    return sum

arr = [12,23,5,70]

n = len(arr)

ans = _sum(arr)

print(ans)