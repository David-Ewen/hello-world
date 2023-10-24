# probability of at least one person

# from group size n getting it right

a = 1

b = 2

n = 3

 

 

x = a/b

z = 1-(1-x)**n

print(z)

 

# group's collective performance

 

import random

 

def average():

   

    L1 = list(range(0, 100))

    L3 = []

 

    contributors = 1

    while contributors < 4:

   

        random.shuffle(L1)

        L2 = L1[0:49]

        L3.extend(L2)

        contributors = contributors + 1

     

    x = set(L3)

    result = list(x)

    y = len(result)

    print(y)

  

 

# this runs the game z number of times:

 

 

for z in range(0,20):

    average()
