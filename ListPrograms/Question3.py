"""Find the length of the list and
swap the first element with (n-1)th element"""

def swap(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)

    return list

list = [12,43,54,67,88]
print(swap(list))