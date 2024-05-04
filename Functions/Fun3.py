#Create a default argument for function
def defaultfun(fname, mname = "Kumar", lname = "Singh"):
    print("Hello",fname,mname,lname)

defaultfun("Avinash","Vyas","Kappor")

#So this is how default arguments work


def average(a=9, b=2):
    print("The average of given number : ",(a+b)/2)

average(12,45)
average()