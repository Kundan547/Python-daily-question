"""Find the length of the list and
swap the first element with (n-1)th element"""

def Swap(newlist):


 newlist[0] , newlist[-1] = newlist[-1] , newlist[0]

 return newlist

newlist = [12,90,34,65,44]

print(Swap(newlist))

