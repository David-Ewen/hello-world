import pandas as pd

# WHERE HANDICAP > 36 (OR MORE THAN > 54), PROGRAMME NEEDS ADJUSTED
# ALSO, LINE FOR SPOON TIED NEEDS TO REFLECT NUMBER OF PLAYERS

# The program first calculates what the par should be, based on the
# the player's handicap should be.It then works out the difference
# between the player's strokes and the par, and converts the difference
# into points using a formula -1 x (difference -2) if the difference
# is within the Stableford boundary

# players' handicaps:



davidh = 17
andrewh = 59
kevinh = 11
neilh = 15
garyh = 30

jackh = 36

#course card:

par = [4, 4, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 4, 5, 3, 5, 4]
stroke = [15, 1, 7, 9, 17, 3, 5, 13, 11, 4, 8, 14, 6, 2, 12, 18, 16, 10]

#shots taken:


davidshots =  [5, 6, 6, 5, 5, 6, 3, 5, 11, 4, 5, 5, 5, 6, 5, 3, 6, 4]

garyshots =   [8, 7, 5, 6, 6, 11, 7, 7, 5, 6, 7, 3, 5, 8, 11, 4, 11, 7]

neilshots =   [4, 7, 6, 5, 5, 4, 4, 4, 3, 6, 5, 3, 4, 6, 8, 6, 4, 6]



andrewshots = [6, 11, 7, 7, 5, 8, 8, 7, 7, 8, 9,11, 8, 8, 8, 7, 10, 8]



jackshots = [8, 8, 5, 6, 11, 5, 6, 11, 5, 4, 11, 11, 6, 7, 8, 6, 7, 5]


kevinshots = [5, 6, 4, 5, 4, 5, 4, 4, 4, 5, 5, 4, 5, 7, 5, 3, 5, 5]



back9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

back6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

back3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]

back1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]





par = [4, 4, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 4, 5, 3, 5, 4]
stroke = [15, 1, 7, 9, 17, 3, 5, 13, 11, 4, 8, 14, 6, 2, 12, 18, 16, 10]
if davidh>= 18:
#if handicap is equal to or over, makes par = par + 1
     par = [i + 1 for i in par]
     davidh = davidh - 18
     #finds how many more strokes need to be given
else:
     par = [i for i in par]

stroke = [x*0 if x > davidh else x//x for x in stroke]
# if, say, handicap is 20, then holes with stroke index
# 1 and 2 have a second stroke added to the par by making the easiest
#and second easiest holes have value of 1

par = [i+x for i,x in zip(par,stroke)]
#par the player is playing to


difference = [j-i for j,i in zip(davidshots,par)]


#difference if, say, 1 under stableford par, it's -1, if 1 over, it's 1
#-1 x (-1 - 2) = 3; or -1 x (1 - 2) = 1
#if difference is more than 1, you get 0 points, but beyond this it will give -ve return,
#which affects sum, hence y < 2
davidpoints = [-1*(y-2) if y < 2 else 0*y for y in difference]

#converts difference into points

davidscore = sum(int(i) for i in davidpoints)

#back 9 count etc

davidback9 = [i*x for i,x in zip(back9,davidpoints)]
davidback9score = sum(int(i) for i in davidback9)

davidback6 = [i*x for i,x in zip(back6,davidpoints)]
davidback6score = sum(int(i) for i in davidback6)

davidback3 = [i*x for i,x in zip(back3,davidpoints)]
davidback3score = sum(int(i) for i in davidback3)

davidback1 = [i*x for i,x in zip(back1,davidpoints)]
davidback1score = sum(int(i) for i in davidback1)

par = [4, 4, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 4, 5, 3, 5, 4]
stroke = [15, 1, 7, 9, 17, 3, 5, 13, 11, 4, 8, 14, 6, 2, 12, 18, 16, 10]
if andrewh>= 36:
     par = [i + 2 for i in par]
     andrewh = andrewh - 36
else:
     par = [i for i in par]
stroke = [x*0 if x > andrewh else x//x for x in stroke]
par = [i+x for i,x in zip(par,stroke)]
difference = [j-i for j,i in zip(andrewshots,par)]
andrewpoints = [-1*(y-2) if y < 2 else 0*y for y in difference]
andrewscore = sum(int(i) for i in andrewpoints)

andrewback9 = [i*x for i,x in zip(back9,andrewpoints)]
andrewback9score = sum(int(i) for i in andrewback9)

andrewback6 = [i*x for i,x in zip(back6,andrewpoints)]
andrewback6score = sum(int(i) for i in andrewback6)

andrewback3 = [i*x for i,x in zip(back3,andrewpoints)]
andrewback3score = sum(int(i) for i in andrewback3)

andrewback1 = [i*x for i,x in zip(back1,andrewpoints)]
andrewback1score = sum(int(i) for i in andrewback1)


par = [4, 4, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 4, 5, 3, 5, 4]
stroke = [15, 1, 7, 9, 17, 3, 5, 13, 11, 4, 8, 14, 6, 2, 12, 18, 16, 10]
if neilh>= 18:
     par = [i + 1 for i in par]
     neilh = neilh - 18
else:
     par = [i for i in par]
stroke = [x*0 if x > neilh else x//x for x in stroke]
par = [i+x for i,x in zip(par,stroke)]
difference = [j-i for j,i in zip(neilshots,par)]
neilpoints = [-1*(y-2) if y < 2 else 0*y for y in difference]
neilscore = sum(int(i) for i in neilpoints)

neilback9 = [i*x for i,x in zip(back9,neilpoints)]
neilback9score = sum(int(i) for i in neilback9)

neilback6 = [i*x for i,x in zip(back6,neilpoints)]
neilback6score = sum(int(i) for i in neilback6)

neilback3 = [i*x for i,x in zip(back3,neilpoints)]
neilback3score = sum(int(i) for i in neilback3)

neilback1 = [i*x for i,x in zip(back1,neilpoints)]
neilback1score = sum(int(i) for i in neilback1)

par = [4, 4, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 4, 5, 3, 5, 4]
stroke = [15, 1, 7, 9, 17, 3, 5, 13, 11, 4, 8, 14, 6, 2, 12, 18, 16, 10]
if kevinh>= 18:
     par = [i + 1 for i in par]
     kevinh = kevinh - 18
else:
     par = [i for i in par]
stroke = [x*0 if x > kevinh else x//x for x in stroke]
par = [i+x for i,x in zip(par,stroke)]
difference = [j-i for j,i in zip(kevinshots,par)]
kevinpoints = [-1*(y-2) if y < 2 else 0*y for y in difference]
kevinscore = sum(int(i) for i in kevinpoints)

kevinback9 = [i*x for i,x in zip(back9,kevinpoints)]
kevinback9score = sum(int(i) for i in kevinback9)

kevinback6 = [i*x for i,x in zip(back6,kevinpoints)]
kevinback6score = sum(int(i) for i in kevinback6)

kevinback3 = [i*x for i,x in zip(back3,kevinpoints)]
kevinback3score = sum(int(i) for i in kevinback3)

kevinback1 = [i*x for i,x in zip(back1,kevinpoints)]
kevinback1score = sum(int(i) for i in kevinback1)



par = [4, 4, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 4, 5, 3, 5, 4]
stroke = [15, 1, 7, 9, 17, 3, 5, 13, 11, 4, 8, 14, 6, 2, 12, 18, 16, 10]
if garyh>= 18:
     par = [i + 1 for i in par]
     garyh = garyh - 18
else:
     par = [i for i in par]
stroke = [x*0 if x > garyh else x//x for x in stroke]
par = [i+x for i,x in zip(par,stroke)]
difference = [j-i for j,i in zip(garyshots,par)]
garypoints = [-1*(y-2) if y < 2 else 0*y for y in difference]
garyscore = sum(int(i) for i in garypoints)

garyback9 = [i*x for i,x in zip(back9,garypoints)]
garyback9score = sum(int(i) for i in garyback9)

garyback6 = [i*x for i,x in zip(back6,garypoints)]
garyback6score = sum(int(i) for i in garyback6)

garyback3 = [i*x for i,x in zip(back3,garypoints)]
garyback3score = sum(int(i) for i in garyback3)

garyback1 = [i*x for i,x in zip(back1,garypoints)]
garyback1score = sum(int(i) for i in garyback1)




par = [4, 4, 4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 4, 5, 3, 5, 4]
stroke = [15, 1, 7, 9, 17, 3, 5, 13, 11, 4, 8, 14, 6, 2, 12, 18, 16, 10]
if jackh>= 18:
     par = [i + 1 for i in par]
     jackh = jackh - 18
else:
     par = [i for i in par]
stroke = [x*0 if x > jackh else x//x for x in stroke]
par = [i+x for i,x in zip(par,stroke)]
difference = [j-i for j,i in zip(jackshots,par)]
jackpoints = [-1*(y-2) if y < 2 else 0*y for y in difference]
jackscore = sum(int(i) for i in jackpoints)

jackback9 = [i*x for i,x in zip(back9,jackpoints)]
jackback9score = sum(int(i) for i in jackback9)

jackback6 = [i*x for i,x in zip(back6,jackpoints)]
jackback6score = sum(int(i) for i in jackback6)

jackback3 = [i*x for i,x in zip(back3,jackpoints)]
jackback3score = sum(int(i) for i in jackback3)

jackback1 = [i*x for i,x in zip(back1,jackpoints)]
jackback1score = sum(int(i) for i in jackback1)




dip_data = pd.DataFrame({
"name":["David","Andrew","Neil","Gary","Jack","Kevin"]
,"Score":[davidscore,andrewscore,neilscore,garyscore,jackscore,kevinscore]
,"back 9":[davidback9score, andrewback9score,neilback9score,garyback9score,\
          jackback9score,kevinback9score]
,"back 6":[davidback6score, andrewback6score,neilback6score,garyback6score,\
          jackback6score,kevinback6score]
,"back 3":[davidback3score,andrewback3score,neilback3score,garyback3score,\
          jackback3score,kevinback3score]
,"back 1":[davidback1score, andrewback1score, neilback1score, garyback1score, \
          jackback1score, kevinback1score]})



results = dip_data.sort_values(by="Score", ascending = False)

# next 2 lines make index relate to scoring position rather than entry in list above
# then makes it start at 1 not 0 

results.reset_index(drop=True, inplace=True)

results.index += 1

if results['Score'].is_unique:
     print ("RESULTS")
else:
     print ("SCORES TIED - USE COUNTBACK")
     print ("Highest score on back 9, if tied, back 6, then back 3, then last hole")

if results.Score[1] == results.Score[2]: 
     print ("*** WINNER IS TIED ***")

if results.Score[5] == results.Score[6]: 
     print ("*** SPOON IS TIED ***")

print ()

print (results)



#print(results.name[1])
#print(results.Score[1])

#print(results.name[2])
#print(results.Score[2])

#print(results.name[3])
#print(results.Score[3])

#print(results.name[4])
#print(results.Score[4])

#print(results.name[5])
#print(results.Score[5])

#print(results.name[6])
#print(results.Score[6])



