x = "Brothers"

def myfun() :
    print("They are my "+x)
myfun()
#Local variable

def myfun2() :
    x = "Enemies"
    print("They are my "+x)

myfun2()
print("they are my "+x)

def myfun3():
    global x
    x = "Brothers"
print("Anna "+x)