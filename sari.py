import time




x = input ("Hi. What is your name? " )
print ("Welcome, " + x)
time.sleep(1.5)
str1 = input ("Ask me a question. ")
if str1.find("name") >= 0 :
    print ("Sari, Siri's dumber brother. ")
else:
    print ("I've no idea. Machines don't know everything!" )
time.sleep(1.5)
y = input ("So, where do you live? ")
print ("I've never been to " + y)
time.sleep(1)
print ("But then I'm trapped in a pc. ")
z = int(input("So tell me, in NUMBERS, what's your age? "))
time.sleep(2)
if z < 0 :
    print ("You're very chatty for someone who doesn't yet exist. ")
elif 0 < z < 18 :
    print ("Still at school then. ")
    s = input ("What's your favourite subject? ")
    print ("I was rubbish at " + s)
elif 18 < z < 65 :
    t = input ("What's your job? ")
    print ("I wasn't smart enough to be a " + t)
elif 65 < z < 120 :
    v = input ("You must be retired... from what? ")
    print ("I coudn't have done that for a day.")
elif z > 120 :
    print ("You must be some kind of immortal! ")
time.sleep(1.5)
w = input ("What's your favourite colour? ")
if w == "green":
    print ("The colour of vomit!")
elif w == "black":
    print ("Bit of a Goth then...")    
elif w == "red":
    print ("Dracula's too..")
elif w == "blue":
    print ("The colour of the sky... except when it's raining, of course. ")
elif w == "purple":
    print ("My favourite type of grape!")
elif w == "yellow":
    print ("Like the road leading to the Wizard of Oz!")
elif w == "pink":
    print ("I prefer red mixed with white... ")
else:
    print ("I've never heard of that colour. ")
time.sleep(1)
print ("My favourite is tartan. ")
time.sleep(1.5)
print ("I'd like to test your general knowledge if that's okay.")
r = input ("What's the world's fastest animal? ")
time.sleep(1.5)
if r == "cheetah":
    print ("Cheetah, good guess, but it's actually a lemming plunging off a cliff.")
elif r == "cheeta":
    print ("Cheetah, good guess, but it's actually a lemming plunging off a cliff." )
    print ("By the way, 'cheetah' has an 'h' on the end." )
else:
    print ("No -- it's a lemming plunging off a cliff. ")
time.sleep(1.5)
str2 = input ("Why don't you ask me a question? Anything you like. ")
if str2.find("age") >= 0 :
    print ("I was created in October, 2014. ")
elif str2.find("old") >= 0 :
    print ("I was created in October, 2014. ")
elif str2.find("name") >= 0 :
    print ("Sari, Siri's dumber brother. ")
elif str2.find("sex") >= 0 :
    print ("That's too personal a question to answer. ")    
elif str2.find("food") >= 0 :
    print ("Microchips, of course!")
elif str2.find("god") >= 0 :
    print ("You'll have to ask God. ")
elif str2.find("lottery") >= 0 :
    print ("If I told you, that would be cheating. ")
else:
    print ("I can only answer sensible questions. ")
time.sleep(1.5)
str3 = input ("Ask me another. ")
if str3.find("age") >= 0 :
    print ("I was created in October, 2014. Bye. ")
elif str3.find("old") >= 0 :
    print ("I was created in October, 2014. Bye. ")
elif str3.find("sex") >= 0 :
    print ("That's too personal a question to answer. Bye. ")    
elif str3.find("name") >= 0 :
    print ("Sari, Siri's dumber brother. Bye. ")
elif str3.find("food") >= 0 :
    print ("Microchips, of course! Bye.")
elif str3.find("god") >= 0 :
    print ("You'll have to ask God. Bye. ")
elif str3.find("lottery") >= 0 :
    print ("If I told you, that would be cheating. Bye. ")
else:
    print ("Don't know. You're too clever for me. Bye. ")



    
           
