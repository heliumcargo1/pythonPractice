# A closure in Python is a function that "remembers" the environment in which it was created.
# In this case, f2() remembers the value of x from the time when f1() was called,
# even though x is local to f1() and f1() has already finished executing.

# CLOUSERS ARE ALSO CALLED FACTORY FUNCTIONS


x= 99

def f1():
    x = 88
    def f2():
        print(x)
        def f3():
            print(f2)
        return f3
    return f2



myRes = f1()
myRes()