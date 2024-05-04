numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 12]

square = 0


#here we store the squares list
squares = []

for value in numbers:
    square = value ** 2
    squares.append(square)
print("The list of squares is", squares)