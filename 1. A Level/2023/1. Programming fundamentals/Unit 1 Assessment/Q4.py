def fibonacci(nterms):
   n1, n2 = 0, 1
   count = 0
   if nterms <= 0:
      print("You can only enter a positive integer")
   else:
      print("Fibonacci sequence:")
      while count < nterms:
          print(n1)
          nth = n1 + n2
          n1 = n2
          n2 = nth
          count += 1
nterms = int(input("How many fib key terms would you like to see?>>"))
fibonacci(nterms)