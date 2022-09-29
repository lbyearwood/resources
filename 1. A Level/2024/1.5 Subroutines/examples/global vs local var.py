a = 2 # global
b = 3
def proc1():
    global b
    print(a)
    b = 6 # local
    print(b)

def proc2():
    print(b)

proc1()
proc2()