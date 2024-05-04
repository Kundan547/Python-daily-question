"""Swap Two Elements in a List"""

def swap(list, pos1, pos2):
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2-1)


    #inserting eachother positions
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list

list = [23,43,55,76,87]

pos1 = int(input("Enter a first position :"))
pos2 = int(input("Enter a second position :"))

print(swap(list, pos1-1, pos2-1))