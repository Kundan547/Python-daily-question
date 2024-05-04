#Adding Docstring to the function
"""The first string after the function is called the Document string or Docstring in short.
 This is used to describe the functionality of the function.
 The use of docstring in functions is optional but it is considered a good practice"""
def evenodd(x):

    if(x%2==0):
        print("Even")
    else:print("Odd")

print(evenodd.__doc__)