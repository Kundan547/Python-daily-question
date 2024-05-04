
#Problem: Extract the last 4 digits from a credit card number for validation.

credit_card = input("Enter credit card number: ")

print("Credit card number:", credit_card)

validation_number = credit_card[-4:]
print("Last four digits:", validation_number)

print("Welcome!")
