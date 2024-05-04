
list1 = ['I am ', 'You are ']
list2 = ['healthy', 'fine', 'geek']

list2_size = len(list2)


for item in list1:

    print("start outer for loop ")
    i = 0

    while (i < list2_size):

        print(item, list2[i])

        i = i + 1

    print("end for loop ")
