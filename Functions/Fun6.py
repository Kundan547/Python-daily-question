def fun1():
    s = int(input("Enter a number :"))

    def fun2():
        print("The number is ", s)

    def fun3():
        if s % 2 == 0:
            print("Number is even :")
        else:
            print("Number is odd :")

    def fun4(s):
        while s <= 3:
            s += 1
            print("Working")
        else:
            print("NotWorking")

    fun2()
    fun4(s)
    fun3()

fun1()
