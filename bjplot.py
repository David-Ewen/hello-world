

#If player goes bust, dealer automatically wins

import random

import numpy
import matplotlib.pyplot as plt
from scipy import stats


L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


n = 2
stand = []
success = []

#first loop is to run the 1000 games for stopping on 2, 3... 21.

while n < 22:

    p1 = 0
    p2 = 0
    draws = 0
    turns = 0


    while turns < 1000:
           
        while True:
            
#player accepting cards until n or more reached
            
            random.shuffle(L1)
            
            total1 = L1[1] + L1[2]
            if total1 >= n:
                total1 = total1
                break
            else:
                total1 = total1 + L1[3]

            if total1 >= n:
                total1 = total1
                break
            else:
                total1 = total1 + L1[4]

            if total1 >= n:
                total1 = total1
                break

            else:
                total1 = total1 + L1[5]

            if total1 >= n:
                total1 = total1
                break
            else:
                total1 = total1 + L1[6]

            if total1 >= n:
                total1 = total1
                break
            else:
                total1 = total1 + L1[7]
                break

            if total1 >= n:
                total1 = total1
                break
            else:
                total1 = total1 + L1[8]
                break

            if total1 >= n:
                total1 = total1
                break
            else:
                total1 = total1 + L1[9]
                break
          
        while True:
            
#dealer turning on 16, standing on anything more than 16
            
            random.shuffle(L1)
            
            total2 = L1[1] + L1[2]

            
            if total2> 15:
                break
            
            else:
                total2 = total2 + L1[3]
      
            if total2> 15:
                break
            
            else:
                total2 = total2 + L1[4]

            if total2> 15:
                break
            
            else:
                total2 = total2 + L1[5]

            if total2> 15:
                break
            
            else:
                total2 = total2 + L1[6]
            
# if player more than 21, bust; if player ok, dealer bust; if both 21 or under
       
        if total1 > 21:
            p2 = p2 + 1
        elif total1 < 22 and total2 > 21:
            p1 = p1 + 1
        elif total2 < 22 and total1 < 22 and total2 > total1:
            p2 = p2 + 1
        elif total1 < 22 and total2 < 22 and total1 > total2:
            p1 = p1 + 1
        else:
            draws = draws + 1

        turns = turns + 1

#calculates % win  
    
    
    perwin = p1/p2*100
    perwinround = round(perwin, 1)

    stand.append(n)
    success.append(perwinround)
 
    n = n + 1
    

#polynomial. 3 gives a good approximation

mymodel = numpy.poly1d(numpy.polyfit(stand, success, 3))

# 1 and 22 are x values, the 100 relates to granularity of fit

myline = numpy.linspace(1, 22, 100)

# this plots graph
plt.scatter(stand, success)
plt.plot(myline, mymodel(myline))

#check fit for polynomial

from sklearn.metrics import r2_score



#linear

#slope, intercept, r, p, std_err = stats.linregress(stand, success)



# def myfunc(stand):
#  return slope * stand + intercept

#mymodel2 = list(map(myfunc, stand))

#plt.plot(stand, mymodel2)
plt.show()

# to get predicted value, success = myfunc([n value])
#success15 = myfunc(15)
#print (success15)


