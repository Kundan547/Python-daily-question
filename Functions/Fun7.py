#Anonymous Functions

def cube(x):
    return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))

print(cube_v2(10))


str1 = 'hey EVEYoNe'

upper = lambda string: string.upper()

lower = lambda string: string.lower()

title = lambda string: string.title()

split = lambda string: string.split()

print(split(str1))
print(type(split))
print(title(str1))
print(lower(str1))
print(upper(str1))





