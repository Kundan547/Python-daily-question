data = "mY naME Is KuNdAN123, i complETED£ My HSC and SSC fRoM!£$%^ GovT*&^% ScHOol "


new_data = data.lower()

def Alfa():
    if new_data.isalnum():
        print("yes alphanumaric vaslue  is exists :")
    else:
        # useing the replace method to replace the alphanumaric value

        print(new_data.replace("kundan123", "kundan"))


# Call the Alfa() function
Alfa()


tessd= "mY naME Is KuNdAN123, i complETED£ My HSC and SSC fRoM!£$%^ GovT*&^% ScHOol "

def test(tessd):  # Define the function with tessd as a parameter
    if tessd.isascii():
        print("There are some special symbols present in this string")
        print(tessd.title())
    else:
        print("Not working")

# Call the test() function with a string as an argument
test("its working")



