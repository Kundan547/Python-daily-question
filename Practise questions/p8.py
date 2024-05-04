"""Write a Python program that inputs three integers and calculates and prints out their sum.
 However, if the three numbers are all equal then print out three times their sum."""

num1 = int(input("Enter a first integer :"))
num2 = int(input("Enter a second integer :"))
num3 = int(input("Enter a thired integer :"))

sum = num1 + num2 + num3

print(sum)


if num1 == num2 and num2 == num3:
    print("All three integers are same :")
    print(sum*3)
else:
    print("invalid")
