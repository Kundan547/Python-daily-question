txt = "python1980"
print(txt.isalnum())

data = "python 3.0.3"
print(data.isalnum())

password = "abc1231"

if password.isalnum():
    print("Password is alfanumaric")
else:
    print("invalid")



# Using isalpha() to check the string that have only alphabet

txt1 = "trilokkundan"

words = txt1.isalpha()

print(words)


passwords = "trilokvyas1224"

if passwords.isalpha():
    print("Yes its alphabet")
elif passwords.isalnum() :
    print("its a alphanumaric value")
else:
    print("invalid")