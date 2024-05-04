is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
	print(item())





is_odd_list = [lambda arg=y: arg + 10 for y in range(1, 6)]
for item in is_odd_list:
    print(item())




is_list = [lambda arg=a: arg / 10 for a in range(1,11)]
for item in is_list:
    print(item())



Max = lambda a,b : a if(a>b) else b
print(Max(5,9))


import math

# Lambda to check if a number n is prime
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

# Testing the lambda function
print(is_prime(29))
print(is_prime(10))
