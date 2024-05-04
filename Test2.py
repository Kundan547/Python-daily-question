try :
    x = int(input("Enter a number : "))
    result = 10/x
except Exception as e:
    print("An error Occurred:",e)
else:
    print("Everything is well")
    print("Result:", result)