"""Swap Two Elements in a List"""


def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]

    return list


list = [12, 45, 32, 67, 65]

pos1 = int(input("Enter a position 1 :"))
pos2 = int(input("Enter a position 2 :"))
print(swap(list, pos1-1, pos2-1))
