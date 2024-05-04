import sys

a_list = []
a_tuple = ()


a_list = ["Kundan", "Kuldeep", "Trilok"]
a_tuple = ("Karthik", "Yuvraj", "Sidharth")

print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))