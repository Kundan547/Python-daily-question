"""creating global variable inside the funcion using
global keyword"""

x = "Boys"
def myfun() :
        global x
        x = "girls"
print("Devils "+x)

myfun()
print("Devi "+x)