#Keyword arguments in function.

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i

    print("Avrage is: ", sum / len(numbers))

average(11,45.24,29,76)