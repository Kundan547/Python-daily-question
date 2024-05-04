x = input("Enter a number :")
y = input("enter a second number :")
z=input("enter a third number :")

Sum = int(x) + int(y) * int(z)



if x > y:
    print("x is greater than y")
elif y < z :
    print(" z is greater than y")
else:
    print("Nope! your are wrong")
    exit()

print("Sum of the values is :", Sum)