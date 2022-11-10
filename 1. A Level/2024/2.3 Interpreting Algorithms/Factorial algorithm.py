# Factorial algorithm without recursion
product = 1
n = 5
for i in range(n,0,-1):
    product = product * i

print(f"The factorial of {n} is {product}")


# Factorial algorithm with recursion

def factorial(n):
    if (n == 1):
        return 1 # once we get to one end the recursion and return to the stack
    else:
        product = n * factorial(n - 1) # recursively call the fibonacci sequence until we get to 1
        return product

print("Factorial of", 5, "is", factorial(5))
