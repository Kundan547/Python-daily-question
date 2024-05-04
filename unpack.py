"""data = (64, "Trilok", True)

id, name, status = data

#output is 1.
print(id)

#output is Trilo.
print(name)

#output is true.
print(status)"""

def get_user():
    # Returning the tuple.
    return 1, "Kundan", True

user_id, user_name, user_status = get_user()

print(user_id)    # Should print: 1
print(user_name)  # Should print: Kundan
print(user_status) # Should print: True


get_user()
