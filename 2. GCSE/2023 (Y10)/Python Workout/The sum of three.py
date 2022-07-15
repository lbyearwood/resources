# step 1 - store three random numbers in three variables
# step 2 - calculate the sum
# step 3 - check if the sum is even or odd
# step 4 - if the sum is even print the sum squared otherwise print it cubed

import random

# step 1 complete
a = random.randint(5,88)
b = random.randint(5,88)
c = random.randint(5,88)

# step 2 complete
sum = a + b + c

# step 3 and 4 complete

if sum % 2 == 0:
    print(sum**2)
else:
    print(sum ** 3)