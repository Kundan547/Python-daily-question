import sys
data = "    Data Science"

print(sys.getsizeof(data))

data1 = '    Kundan'
print(sys.getsizeof(data1))
print(data1.lstrip())

data2 = 'kundan'
print(sys.getsizeof(data2))
print(data2.lstrip('k'))