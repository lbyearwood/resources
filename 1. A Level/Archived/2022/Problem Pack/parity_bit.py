import random
binaryString = []

def even_parity(binaryString):
   pass

for i in range(0, 10):
   x = ""
   for i in range(0, 8):
       x += str(random.randint(0, 1))
   binaryString = even_parity(x)
   binaryString.append(binaryString)
   print(binaryString)