Allowed_users = ["Kunal","Shivam","trilok","kuldeep"]

new_list = Allowed_users.append("karthik")



username = input("What is your login : ")

if username in Allowed_users:
    print("Access granted")
else:
    print("Invalid")
