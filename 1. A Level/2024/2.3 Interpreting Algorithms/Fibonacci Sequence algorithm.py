a,b = 1,1
# Fibonacci sequence algorithm without recursion
for i in range(10):
    print(a)
    c = a + b # create the third term
    a = b # update first term
    b = c # update second term


# Fibonacci sequence algorithm with recursion

def fibonacci(counter,stop,a,b):
    if counter > stop:
        return
        exit()
    print(a)
    c = a + b  # create the third term
    a = b  # update first term
    b = c  # update second term
    counter += 1 # increment counter by 1
    fibonacci(counter,stop,a,b) # recursive call


fibonacci(1,10,1,1)