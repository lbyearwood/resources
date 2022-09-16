from functools import reduce

print("print the sum of numbers 1 to 9")
fx = reduce(lambda a,b: a +b,list(x for x in range(1,10)),0)
print(fx)
