"""Find the length of the list and
swap the first element with (n-1)th element"""

#we create function Swap

def Swap(List):
    size = len(List)

    #temp variable to storte the first index value of list.
    temp = List[0]
    List[0] = List[size-1]
    List[size-1] = temp

    return List
List = [12,15,17,11]

#calling the swap fuction

print(Swap(List))