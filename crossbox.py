#oct 2016


import pygame

import random

import time

import sys

pygame.init()

# sound:

# pygame.mixer.init()
# pygame.mixer.pre_init(44100, -16, 2, 2048)
# tap1 = pygame.mixer.Sound("tap1.aif")
# tap2 = pygame.mixer.Sound("tap2.aif")


player1_total = 0
player2_total = 0

running = 1
while running > 0:


    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    GREEN    = (   0, 200,   0)
    RED      = ( 255,   0,   0)
    BLUE     = ( 0,  130, 255)



    screen = pygame.display.set_mode([460, 460])
    width  = 60
    height = 60
    margin = 5
    pygame.display.set_caption("crossbox")


    font2 = pygame.font.SysFont('Calibri', 20, True, False)


     
    myArray = [[0 for j in range(7)] for i in range(7)]


    clock = pygame.time.Clock()
    clock.tick(60)


    def user_input():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # tap1.play(0) 
                 
                    pos = pygame.mouse.get_pos()
                    if pos[0] > 65 and pos[1] > 65 and pos[0] < 390 and pos[1] < 390:
                        # making them into co-ordinates, width and margin like unit measure:
                        i = pos[0] // (width + margin)
                        j = pos[1] // (height + margin)
                        if myArray[i][j] == 0: 
                            myArray[i][j] = 1
                            return myArray[i][j]
                        else:
                            text = font2.render("Taken, pick another " , True, WHITE)
                            screen.blit(text, [145, 412])
                            pygame.time.wait(300)
                            pygame.display.update()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                

    def drawstuff():

        screen.fill(BLACK)

        text = font2.render("Player1:  " +str(player1_total),True,WHITE)
        screen.blit(text, [110, 20])
        text = font2.render("Player2:  " +str(player2_total),True,WHITE)
        screen.blit(text, [255, 20])
        
        for i in range(1,6):
            for j in range(1,6):
                color = WHITE
                if myArray[i][j] == 1:
                    color = GREEN
                if myArray[i][j] == 4:
                    color = BLUE
                pygame.draw.rect(screen,
                         color,
                         [(margin+width)*i+margin,
                          (margin+height)*j+margin,
                          width,
                          height])
        
        pygame.display.update()



    L1 = [1, 2, 3, 4, 5]
    L2 = [1, 2, 3, 4, 5]

    def boxtest():

        a = myArray[i][j + 1]
        b = myArray[i][j - 1]
        c = myArray[i + 1][j]
        d = myArray[i - 1][j]
        f = myArray[i + 1][j + 1]
        g = myArray[i + 1][j - 1]
        k = myArray[i - 1][j + 1]
        l = myArray[i -1][j -1]

        d1 = b + l + d 
        h1 = d + k + a 
        p1 = a + f + c 
        t1 = c + g + b 

        if d1==3 or d1==12 or h1==3 or h1==12 or p1==3 or p1==12 or t1==3 or t1==12:
            myArray[i][j] = 4
        
                     
    def rectest():
        
        a = myArray[i][j + 1]
        b = myArray[i][j - 1]
        c = myArray[i + 1][j]
        d = myArray[i - 1][j]
        f = myArray[i + 1][j + 1]
        g = myArray[i + 1][j - 1]
        k = myArray[i - 1][j + 1]
        l = myArray[i -1][j -1]

        d1 = l + d + k 
        h1 = k + a + f 
        p1 = f + c + g
        t1 = g + b + l

        if d1==3 or d1==12 or p1==3 or p1==12:
             if (a + b) == 0:
                 myArray[i][j] = 4

        if h1==3 or h1==12 or t1==3 or t1==12:
             if (c + d) == 0:
                 myArray[i][j] = 4
        
    def nexttest1():

        a = myArray[i][j + 1]
        b = myArray[i][j - 1]
        c = myArray[i + 1][j]
        d = myArray[i - 1][j]
        f = myArray[i + 1][j + 1]
        g = myArray[i + 1][j - 1]
        k = myArray[i - 1][j + 1]
        l = myArray[i - 1][j - 1]

        i2 = l + b
        j2 = b + g
        k2 = g + c
        l2 = c + f
        m2 = f + a
        n2 = a + k
        p2 = k + d
        q2 = d + l
        r2 = b + c 
        s2 = c + a
        t2 = a + d
        v2 = d + b
     
        list = [i2, j2, k2, l2, m2, n2, p2, q2, r2, s2, t2, v2]
        for x in list:
            if x ==8 or x == 2:
                myArray[i][j] = 4


    def nexttest2():

        a = myArray[i][j + 1]
        b = myArray[i][j - 1]
        c = myArray[i + 1][j]
        d = myArray[i - 1][j]
        

        if a==1 or a==4 or d==1 or d==4 or b ==1 or b == 4 or c == 1 or c==4:
            myArray[i][j] = 4

        

    def nexttest3():

        
        f = myArray[i + 1][j + 1]
        g = myArray[i + 1][j - 1]
        k = myArray[i - 1][j + 1]
        l = myArray[i - 1][j - 1]

        if f==1 or f==4 or g==1 or g==4 or k ==1 or k == 4 or l == 1 or 1==4:
            myArray[i][j] = 4

        

    #game start

    drawstuff()

    user_input()

    drawstuff()

    while True:
            compi = random.randint(2,4)
            compj = random.randint(2,4)
            if myArray[compi][compj] == 0:
                myArray[compi][compj] = 4
                break;

    while True:
            compi = random.randint(1,5)
            compj = random.randint(1,5)
            if myArray[compi][compj] == 0:
                myArray[compi][compj] = 4
                break;

    pygame.time.wait(1000)
    # tap2.play(0) 

    drawstuff()

    turns = 0
    while turns < 22:
        
        user_input()

        drawstuff()

        while True:

    # next five lines, compx gives 1 in 10 chance of machine picking random box
    # each turn before following AI. Option of "easy" or "difficult" might
    # be difference between, say, 1 in 2 and 1 in 20 setting. Good to retain
    # some randomness so game play isn't predictable

            compi = random.randint(1,5)
            compj = random.randint(1,5)
            compx = random.randint(1,10)
            if myArray[compi][compj] == 0 and compx == 1:
                myArray[compi][compj] = 4
                break

    # the random.shuffle randomises order in which squares are
    # checked to make machine play (offensive/defensive) less predictable

            random.shuffle(L1)
            random.shuffle(L2)

            if myArray[L1[0]][L2[0]] == 0:
                i = L1[0]
                j = L2[0]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[1]][L2[0]] == 0:
                i = L1[1]
                j = L2[0]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[0]] == 0:
                i = L1[2]
                j = L2[0]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[3]][L2[0]] == 0:
                i = L1[3]
                j = L2[0]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[0]] == 0:
                i = L1[4]
                j = L2[0]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[1]] == 0:
                i = L1[0]
                j = L2[1]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[1]][L2[1]] == 0:
                i = L1[1]
                j = L2[1]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[1]] == 0:
                i = L1[2]
                j = L2[1]
                boxtest()
                if myArray[i][j] == 4:
                    break
          
            if myArray[L1[3]][L2[1]] == 0:
                i = L1[3]
                j = L2[1]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[1]] == 0:
                i = L1[4]
                j = L2[1]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[2]] == 0:
                i = L1[0]
                j = L2[2]
                boxtest()
                if myArray[i][j] == 4:
                    break
                   
            if myArray[L1[1]][L2[2]] == 0:
                i = L1[1]
                j = L2[2]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[2]] == 0:
                i = L1[2]
                j = L2[2]
                boxtest()
                if myArray[i][j] == 4:
                    break   

            if myArray[L1[3]][L2[2]] == 0:
                i = L1[3]
                j = L2[2]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[2]] == 0:
                i = L1[4]
                j = L2[2]
                boxtest()
                if myArray[i][j] == 4:
                    break
            
            if myArray[L1[0]][L2[3]] == 0:
                i = L1[0]
                j = L2[3]
                boxtest()
                if myArray[i][j] == 4:
                    break
                
            if myArray[L1[1]][L2[3]] == 0:
                i = L1[1]
                j = L2[3]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[3]] == 0:
                i = L1[2]
                j = L2[3]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[3]][L2[3]] == 0:
                i = L1[3]
                j = L2[3]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[3]] == 0:
                i = L1[4]
                j = L2[3]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[4]] == 0:
                i = L1[0]
                j = L2[4]
                boxtest()
                if myArray[i][j] == 4:
                    break
           
            if myArray[L1[1]][L2[4]] == 0:
                i = L1[1]
                j = L2[4]
                boxtest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[4]] == 0:
                i = L1[2]
                j = L2[4]
                boxtest()
                if myArray[i][j] == 4:
                    break
          
            if myArray[L1[3]][L2[4]] == 0:
                i = L1[3]
                j = L2[4]
                boxtest()
                if myArray[i][j] == 4:
                    break
           
            if myArray[L1[4]][L2[4]] == 0:
                i = L1[4]
                j = L2[4]
                boxtest()
                if myArray[i][j] == 4:
                    break


    # 

            if myArray[L1[0]][L2[0]] == 0:
                i = L1[0]
                j = L2[0]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[1]][L2[0]] == 0:
                i = L1[1]
                j = L2[0]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[0]] == 0:
                i = L1[2]
                j = L2[0]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[3]][L2[0]] == 0:
                i = L1[3]
                j = L2[0]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[0]] == 0:
                i = L1[4]
                j = L2[0]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[1]] == 0:
                i = L1[0]
                j = L2[1]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[1]][L2[1]] == 0:
                i = L1[1]
                j = L2[1]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[1]] == 0:
                i = L1[2]
                j = L2[1]
                rectest()
                if myArray[i][j] == 4:
                    break
          
            if myArray[L1[3]][L2[1]] == 0:
                i = L1[3]
                j = L2[1]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[1]] == 0:
                i = L1[4]
                j = L2[1]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[2]] == 0:
                i = L1[0]
                j = L2[2]
                rectest()
                if myArray[i][j] == 4:
                    break
                   
            if myArray[L1[1]][L2[2]] == 0:
                i = L1[1]
                j = L2[2]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[2]] == 0:
                i = L1[2]
                j = L2[2]
                rectest()
                if myArray[i][j] == 4:
                    break   

            if myArray[L1[3]][L2[2]] == 0:
                i = L1[3]
                j = L2[2]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[2]] == 0:
                i = L1[4]
                j = L2[2]
                rectest()
                if myArray[i][j] == 4:
                    break
            
            if myArray[L1[0]][L2[3]] == 0:
                i = L1[0]
                j = L2[3]
                rectest()
                if myArray[i][j] == 4:
                    break
                
            if myArray[L1[1]][L2[3]] == 0:
                i = L1[1]
                j = L2[3]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[3]] == 0:
                i = L1[2]
                j = L2[3]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[3]][L2[3]] == 0:
                i = L1[3]
                j = L2[3]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[3]] == 0:
                i = L1[4]
                j = L2[3]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[4]] == 0:
                i = L1[0]
                j = L2[4]
                rectest()
                if myArray[i][j] == 4:
                    break
           
            if myArray[L1[1]][L2[4]] == 0:
                i = L1[1]
                j = L2[4]
                rectest()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[4]] == 0:
                i = L1[2]
                j = L2[4]
                rectest()
                if myArray[i][j] == 4:
                    break
          
            if myArray[L1[3]][L2[4]] == 0:
                i = L1[3]
                j = L2[4]
                rectest()
                if myArray[i][j] == 4:
                    break
           
            if myArray[L1[4]][L2[4]] == 0:
                i = L1[4]
                j = L2[4]
                rectest()
                if myArray[i][j] == 4:
                    break
    #
            if myArray[L1[0]][L2[0]] == 0:
                i = L1[0]
                j = L2[0]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[1]][L2[0]] == 0:
                i = L1[1]
                j = L2[0]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[0]] == 0:
                i = L1[2]
                j = L2[0]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[3]][L2[0]] == 0:
                i = L1[3]
                j = L2[0]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[0]] == 0:
                i = L1[4]
                j = L2[0]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[1]] == 0:
                i = L1[0]
                j = L2[1]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[1]][L2[1]] == 0:
                i = L1[1]
                j = L2[1]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[1]] == 0:
                i = L1[2]
                j = L2[1]
                nexttest1()
                if myArray[i][j] == 4:
                    break
          
            if myArray[L1[3]][L2[1]] == 0:
                i = L1[3]
                j = L2[1]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[1]] == 0:
                i = L1[4]
                j = L2[1]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[2]] == 0:
                i = L1[0]
                j = L2[2]
                nexttest1()
                if myArray[i][j] == 4:
                    break
                   
            if myArray[L1[1]][L2[2]] == 0:
                i = L1[1]
                j = L2[2]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[2]] == 0:
                i = L1[2]
                j = L2[2]
                nexttest1()
                if myArray[i][j] == 4:
                    break   

            if myArray[L1[3]][L2[2]] == 0:
                i = L1[3]
                j = L2[2]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[2]] == 0:
                i = L1[4]
                j = L2[2]
                nexttest1()
                if myArray[i][j] == 4:
                    break
            
            if myArray[L1[0]][L2[3]] == 0:
                i = L1[0]
                j = L2[3]
                nexttest1()
                if myArray[i][j] == 4:
                    break
                
            if myArray[L1[1]][L2[3]] == 0:
                i = L1[1]
                j = L2[3]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[3]] == 0:
                i = L1[2]
                j = L2[3]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[3]][L2[3]] == 0:
                i = L1[3]
                j = L2[3]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[3]] == 0:
                i = L1[4]
                j = L2[3]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[4]] == 0:
                i = L1[0]
                j = L2[4]
                nexttest1()
                if myArray[i][j] == 4:
                    break
           
            if myArray[L1[1]][L2[4]] == 0:
                i = L1[1]
                j = L2[4]
                nexttest1()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[4]] == 0:
                i = L1[2]
                j = L2[4]
                nexttest1()
                if myArray[i][j] == 4:
                    break
          
            if myArray[L1[3]][L2[4]] == 0:
                i = L1[3]
                j = L2[4]
                nexttest1()
                if myArray[i][j] == 4:
                    break
           
            if myArray[L1[4]][L2[4]] == 0:
                i = L1[4]
                j = L2[4]
                nexttest1()
                if myArray[i][j] == 4:
                    break
    #

            if myArray[L1[0]][L2[0]] == 0:
                i = L1[0]
                j = L2[0]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[1]][L2[0]] == 0:
                i = L1[1]
                j = L2[0]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[0]] == 0:
                i = L1[2]
                j = L2[0]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[3]][L2[0]] == 0:
                i = L1[3]
                j = L2[0]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[0]] == 0:
                i = L1[4]
                j = L2[0]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[1]] == 0:
                i = L1[0]
                j = L2[1]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[1]][L2[1]] == 0:
                i = L1[1]
                j = L2[1]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[1]] == 0:
                i = L1[2]
                j = L2[1]
                nexttest2()
                if myArray[i][j] == 4:
                    break
          
            if myArray[L1[3]][L2[1]] == 0:
                i = L1[3]
                j = L2[1]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[1]] == 0:
                i = L1[4]
                j = L2[1]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[2]] == 0:
                i = L1[0]
                j = L2[2]
                nexttest2()
                if myArray[i][j] == 4:
                    break
                   
            if myArray[L1[1]][L2[2]] == 0:
                i = L1[1]
                j = L2[2]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[2]] == 0:
                i = L1[2]
                j = L2[2]
                nexttest2()
                if myArray[i][j] == 4:
                    break   

            if myArray[L1[3]][L2[2]] == 0:
                i = L1[3]
                j = L2[2]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[2]] == 0:
                i = L1[4]
                j = L2[2]
                nexttest2()
                if myArray[i][j] == 4:
                    break
            
            if myArray[L1[0]][L2[3]] == 0:
                i = L1[0]
                j = L2[3]
                nexttest2()
                if myArray[i][j] == 4:
                    break
                
            if myArray[L1[1]][L2[3]] == 0:
                i = L1[1]
                j = L2[3]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[3]] == 0:
                i = L1[2]
                j = L2[3]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[3]][L2[3]] == 0:
                i = L1[3]
                j = L2[3]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[3]] == 0:
                i = L1[4]
                j = L2[3]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[4]] == 0:
                i = L1[0]
                j = L2[4]
                nexttest2()
                if myArray[i][j] == 4:
                    break
           
            if myArray[L1[1]][L2[4]] == 0:
                i = L1[1]
                j = L2[4]
                nexttest2()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[4]] == 0:
                i = L1[2]
                j = L2[4]
                nexttest2()
                if myArray[i][j] == 4:
                    break
          
            if myArray[L1[3]][L2[4]] == 0:
                i = L1[3]
                j = L2[4]
                nexttest2()
                if myArray[i][j] == 4:
                    break
           
            if myArray[L1[4]][L2[4]] == 0:
                i = L1[4]
                j = L2[4]
                nexttest2()
                if myArray[i][j] == 4:
                    break
    #

            if myArray[L1[0]][L2[0]] == 0:
                i = L1[0]
                j = L2[0]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[1]][L2[0]] == 0:
                i = L1[1]
                j = L2[0]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[0]] == 0:
                i = L1[2]
                j = L2[0]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[3]][L2[0]] == 0:
                i = L1[3]
                j = L2[0]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[0]] == 0:
                i = L1[4]
                j = L2[0]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[1]] == 0:
                i = L1[0]
                j = L2[1]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[1]][L2[1]] == 0:
                i = L1[1]
                j = L2[1]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[1]] == 0:
                i = L1[2]
                j = L2[1]
                nexttest3()
                if myArray[i][j] == 4:
                    break
          
            if myArray[L1[3]][L2[1]] == 0:
                i = L1[3]
                j = L2[1]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[1]] == 0:
                i = L1[4]
                j = L2[1]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[2]] == 0:
                i = L1[0]
                j = L2[2]
                nexttest3()
                if myArray[i][j] == 4:
                    break
                   
            if myArray[L1[1]][L2[2]] == 0:
                i = L1[1]
                j = L2[2]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[2]] == 0:
                i = L1[2]
                j = L2[2]
                nexttest3()
                if myArray[i][j] == 4:
                    break   

            if myArray[L1[3]][L2[2]] == 0:
                i = L1[3]
                j = L2[2]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[2]] == 0:
                i = L1[4]
                j = L2[2]
                nexttest3()
                if myArray[i][j] == 4:
                    break
            
            if myArray[L1[0]][L2[3]] == 0:
                i = L1[0]
                j = L2[3]
                nexttest3()
                if myArray[i][j] == 4:
                    break
                
            if myArray[L1[1]][L2[3]] == 0:
                i = L1[1]
                j = L2[3]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[3]] == 0:
                i = L1[2]
                j = L2[3]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[3]][L2[3]] == 0:
                i = L1[3]
                j = L2[3]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[4]][L2[3]] == 0:
                i = L1[4]
                j = L2[3]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[0]][L2[4]] == 0:
                i = L1[0]
                j = L2[4]
                nexttest3()
                if myArray[i][j] == 4:
                    break
           
            if myArray[L1[1]][L2[4]] == 0:
                i = L1[1]
                j = L2[4]
                nexttest3()
                if myArray[i][j] == 4:
                    break

            if myArray[L1[2]][L2[4]] == 0:
                i = L1[2]
                j = L2[4]
                nexttest3()
                if myArray[i][j] == 4:
                    break
          
            if myArray[L1[3]][L2[4]] == 0:
                i = L1[3]
                j = L2[4]
                nexttest3()
                if myArray[i][j] == 4:
                    break
           
            if myArray[L1[4]][L2[4]] == 0:
                i = L1[4]
                j = L2[4]
                nexttest3()
                if myArray[i][j] == 4:
                    break


        pygame.time.wait(1000)
        # tap2.play(0) 

      
        drawstuff()
            
        turns = turns + 2


    # game result

    marks0 = myArray[1][1]

    marks1 = myArray[2][1] 
    marks2 = myArray[3][1] 
    marks3 = myArray[4][1] 
    marks4 = myArray[5][1] 
         
    marks5 = myArray[1][2] 
    marks6 = myArray[2][2] 
    marks7 = myArray[3][2] 
    marks8 = myArray[4][2] 
    marks9 = myArray[5][2] 

    marks10 = myArray[1][3] 
    marks11 = myArray[2][3] 
    marks12 = myArray[3][3] 
    marks13 = myArray[4][3] 
    marks14 = myArray[5][3] 

    marks15 = myArray[1][4] 
    marks16 = myArray[2][4] 
    marks17 = myArray[3][4] 
    marks18 = myArray[4][4] 
    marks19 = myArray[5][4] 

    marks20 = myArray[1][5] 
    marks21 = myArray[2][5] 
    marks22 = myArray[3][5] 
    marks23 = myArray[4][5] 
    marks24 = myArray[5][5]

    a1 = marks0 + marks1
    if a1 == 2:
        pygame.draw.line(screen, RED, (100, 100), (165, 100), 5)
    if a1 == 8:
        pygame.draw.line(screen, WHITE, (100, 100), (165, 100), 5)
        
    a2 = marks1 + marks6
    if a2 == 2:
        pygame.draw.line(screen, RED, (165, 100), (165, 165), 5)
    if a2 == 8:
        pygame.draw.line(screen, WHITE, (165, 100), (165, 165), 5)

    a3 = marks6 + marks5
    if a3 == 2:
        pygame.draw.line(screen, RED, (165, 165), (100, 165), 5)
    if a3 == 8:
        pygame.draw.line(screen, WHITE, (165, 165), (100, 165), 5)

    a4 = marks5 + marks0
    if a4 == 2:
        pygame.draw.line(screen, RED, (100, 165), (100, 100), 5)
    if a4 == 8:
        pygame.draw.line(screen, WHITE, (100, 165), (100, 100), 5)

    a5 = marks0 + marks6
    if a5 == 2:
        pygame.draw.line(screen, RED, (100, 100), (165, 165), 5)
    if a5 == 8:
        pygame.draw.line(screen, WHITE, (100, 100), (165, 165), 5)

    a6 = marks1 + marks5
    if a6 == 2:
        pygame.draw.line(screen, RED, (100, 165), (165, 100), 5)
    if a6 == 8:
        pygame.draw.line(screen, WHITE, (100, 165), (165,100), 5)

    a7 = marks1 + marks2
    if a7 == 2:
        pygame.draw.line(screen, RED, (165, 100), (230, 100), 5)
    if a7 == 8:
        pygame.draw.line(screen, WHITE, (165, 100), (230, 100), 5)

    a8 = marks2 + marks7
    if a8 == 2:
        pygame.draw.line(screen, RED, (230, 100), (230, 165), 5)
    if a8 == 8:
        pygame.draw.line(screen, WHITE, (230, 100), (230, 165), 5)

    a9 = marks7 + marks6
    if a9 == 2:
        pygame.draw.line(screen, RED, (230, 165), (165, 165), 5)
    if a9 == 8:
        pygame.draw.line(screen, WHITE, (230, 165), (165, 165), 5)

    a10 = marks1 + marks7
    if a10 == 2:
        pygame.draw.line(screen, RED, (165, 100), (230, 165), 5)
    if a10 == 8:
        pygame.draw.line(screen, WHITE, (165, 100), (230, 165), 5)

    a11 = marks6 + marks2
    if a11 == 2:
        pygame.draw.line(screen, RED, (165, 165), (230, 100), 5)
    if a11 == 8:
        pygame.draw.line(screen, WHITE, (165, 165), (230, 100), 5)

    a12 = marks2 + marks3
    if a12 == 2:
        pygame.draw.line(screen, RED, (230, 100), (295, 100), 5)
    if a12 == 8:
        pygame.draw.line(screen, WHITE, (230, 100), (295, 100), 5)

    a13 = marks3 + marks8
    if a13 == 2:
        pygame.draw.line(screen, RED, (295, 100), (295, 165), 5)
    if a13 == 8:
        pygame.draw.line(screen, WHITE, (295, 100), (295, 165), 5)

    a14 = marks8 + marks7
    if a14 == 2:
        pygame.draw.line(screen, RED, (295, 165), (230, 165), 5)
    if a14 == 8:
        pygame.draw.line(screen, WHITE, (295, 165), (230, 165), 5)

    a15 = marks2 + marks8
    if a15 == 2:
        pygame.draw.line(screen, RED, (230, 100), (295, 165), 5)
    if a15 == 8:
        pygame.draw.line(screen, WHITE, (230, 100), (295, 165), 5)

    a16 = marks7 + marks3
    if a16 == 2:
        pygame.draw.line(screen, RED, (230, 165), (295, 100), 5)
    if a16 == 8:
        pygame.draw.line(screen, WHITE, (230, 165), (295, 100), 5)

    a17 = marks3 + marks4
    if a17 == 2:
        pygame.draw.line(screen, RED, (295, 100), (360, 100), 5)
    if a17 == 8:
        pygame.draw.line(screen, WHITE, (295, 100), (360, 100), 5)

    a18 = marks4 + marks9
    if a18 == 2:
        pygame.draw.line(screen, RED, (360, 100), (360, 165), 5)
    if a18 == 8:
        pygame.draw.line(screen, WHITE, (360, 100), (360, 165), 5)

    a19 = marks9 + marks8
    if a19 == 2:
        pygame.draw.line(screen, RED, (360, 165), (295, 165), 5)
    if a19 == 8:
        pygame.draw.line(screen, WHITE, (360, 165), (295, 165), 5)

    a20 = marks3 + marks9
    if a20 == 2:
        pygame.draw.line(screen, RED, (295, 100), (360, 165), 5)
    if a20 == 8:
        pygame.draw.line(screen, WHITE, (295, 100), (360, 165), 5)

    a21 = marks8 + marks4
    if a21 == 2:
        pygame.draw.line(screen, RED, (295, 165), (360, 100), 5)
    if a21 == 8:
        pygame.draw.line(screen, WHITE, (295, 165), (360, 100), 5)

    a22 = marks5 + marks10
    if a22 == 2:
        pygame.draw.line(screen, RED, (100, 165), (100, 230), 5)
    if a22 == 8:
        pygame.draw.line(screen, WHITE, (100, 165), (100, 230), 5)

    a23 = marks10 + marks11
    if a23 == 2:
        pygame.draw.line(screen, RED, (100, 230), (165, 230), 5)
    if a23 == 8:
        pygame.draw.line(screen, WHITE, (100, 230), (165, 230), 5)

    a24 = marks11 + marks6
    if a24 == 2:
        pygame.draw.line(screen, RED, (165, 230), (165, 165), 5)
    if a24 == 8:
        pygame.draw.line(screen, WHITE, (165, 230), (165, 165), 5)

    a25 = marks5 + marks11
    if a25 == 2:
        pygame.draw.line(screen, RED, (100, 165), (165, 230), 5)
    if a25 == 8:
        pygame.draw.line(screen, WHITE, (100, 165), (165, 230), 5)

    a26 = marks10 + marks6
    if a26 == 2:
        pygame.draw.line(screen, RED, (100, 230), (165, 165), 5)
    if a26 == 8:
        pygame.draw.line(screen, WHITE, (100, 230), (165, 165), 5)

    a27 = marks11 + marks12
    if a27 == 2:
        pygame.draw.line(screen, RED, (165, 230), (230, 230), 5)
    if a27 == 8:
        pygame.draw.line(screen, WHITE, (165, 230), (230, 230), 5)

    a28 = marks7 + marks12
    if a28 == 2:
        pygame.draw.line(screen, RED, (230, 165), (230, 230), 5)
    if a28 == 8:
        pygame.draw.line(screen, WHITE, (230, 165), (230, 230), 5)

    a29 = marks6 + marks12
    if a29 == 2:
        pygame.draw.line(screen, RED, (165, 165), (230, 230), 5)
    if a29 == 8:
        pygame.draw.line(screen, WHITE, (165, 165), (230, 230), 5)

    a30 = marks11 + marks7
    if a30 == 2:
        pygame.draw.line(screen, RED, (230, 165), (165, 230), 5)
    if a30 == 8:
        pygame.draw.line(screen, WHITE, (230, 165), (165, 230), 5)

    a31 = marks12 + marks13
    if a31 == 2:
        pygame.draw.line(screen, RED, (230, 230), (295, 230), 5)
    if a31 == 8:
        pygame.draw.line(screen, WHITE, (230, 230), (295, 230), 5)

    a32 = marks13 + marks8
    if a32 == 2:
        pygame.draw.line(screen, RED, (295, 165), (295, 230), 5)
    if a32 == 8:
        pygame.draw.line(screen, WHITE, (295, 165), (295, 230), 5)

    a33 = marks7 + marks13
    if a33 == 2:
        pygame.draw.line(screen, RED, (230, 165), (295, 230), 5)
    if a33 == 8:
        pygame.draw.line(screen, WHITE, (230, 165), (295, 230), 5)

    a34 = marks12 + marks8
    if a34 == 2:
        pygame.draw.line(screen, RED, (230, 230), (295, 165), 5)
    if a34 == 8:
        pygame.draw.line(screen, WHITE, (230, 230), (295, 165), 5)

    a35 = marks13 + marks14
    if a35 == 2:
        pygame.draw.line(screen, RED, (360, 230), (295, 230), 5)
    if a35 == 8:
        pygame.draw.line(screen, WHITE, (360, 230), (295, 230), 5)

    a36 = marks14 + marks9
    if a36 == 2:
        pygame.draw.line(screen, RED, (360, 230), (360, 165), 5)
    if a36 == 8:
        pygame.draw.line(screen, WHITE, (360, 230), (360,165), 5)

    a37 = marks13 + marks9
    if a37 == 2:
        pygame.draw.line(screen, RED, (360, 165), (295, 230), 5)
    if a37 == 8:
        pygame.draw.line(screen, WHITE, (360, 165), (295, 230), 5)

    a38 = marks8 + marks14
    if a38 == 2:
        pygame.draw.line(screen, RED, (360, 230), (295, 165), 5)
    if a38 == 8:
        pygame.draw.line(screen, WHITE, (360, 230), (295, 165), 5)

    a39 = marks10 + marks15
    if a39 == 2:
        pygame.draw.line(screen, RED, (100, 295), (100, 230), 5)
    if a39 == 8:
        pygame.draw.line(screen, WHITE, (100, 295), (100, 230), 5)

    a40 = marks15 + marks16
    if a40 == 2:
        pygame.draw.line(screen, RED, (100, 295), (165, 295), 5)
    if a40 == 8:
        pygame.draw.line(screen, WHITE, (100, 295), (165, 295), 5)

    a41 = marks16 + marks11
    if a41 == 2:
        pygame.draw.line(screen, RED, (165, 230), (165, 295), 5)
    if a41 == 8:
        pygame.draw.line(screen, WHITE, (165, 230), (165, 295), 5)

    a42 = marks10 + marks16
    if a42 == 2:
        pygame.draw.line(screen, RED, (100, 230), (165, 295), 5)
    if a42 == 8:
        pygame.draw.line(screen, WHITE, (100, 230), (165, 295), 5)

    a43 = marks15 + marks11
    if a43 == 2:
        pygame.draw.line(screen, RED, (165, 230), (100, 295), 5)
    if a43 == 8:
        pygame.draw.line(screen, WHITE, (165, 230), (100, 295), 5)

    a44 = marks16 + marks17
    if a44 == 2:
        pygame.draw.line(screen, RED, (230, 295), (165, 295), 5)
    if a44 == 8:
        pygame.draw.line(screen, WHITE, (230, 295), (165, 295), 5)

    a45 = marks17 + marks12
    if a45 == 2:
        pygame.draw.line(screen, RED, (230, 295), (230, 230), 5)
    if a45 == 8:
        pygame.draw.line(screen, WHITE, (230, 295), (230, 230), 5)

    a46 = marks16 + marks12
    if a46 == 2:
        pygame.draw.line(screen, RED, (165, 295), (230, 230), 5)
    if a46 == 8:
        pygame.draw.line(screen, WHITE, (165, 295), (230, 230), 5)

    a47 = marks11 + marks17
    if a47 == 2:
        pygame.draw.line(screen, RED, (230, 295), (165, 230), 5)
    if a47 == 8:
        pygame.draw.line(screen, WHITE, (230, 295), (165, 230), 5)

    a48 = marks17 + marks18
    if a48 == 2:
        pygame.draw.line(screen, RED, (230, 295), (295, 295), 5)
    if a48 == 8:
        pygame.draw.line(screen, WHITE, (230, 295), (295, 295), 5)

    a49 = marks18 + marks13
    if a49 == 2:
        pygame.draw.line(screen, RED, (295, 230), (295, 295), 5)
    if a49 == 8:
        pygame.draw.line(screen, WHITE, (295, 230), (295, 295), 5)

    a50 = marks12 + marks18
    if a50 == 2:
        pygame.draw.line(screen, RED, (230, 230), (295, 295), 5)
    if a50 == 8:
        pygame.draw.line(screen, WHITE, (230, 230), (295, 295), 5)
    a51 = marks17 + marks13
    if a51 == 2:
        pygame.draw.line(screen, RED, (295, 230), (230, 295), 5)
    if a51 == 8:
        pygame.draw.line(screen, WHITE, (295, 230), (230, 295), 5)

    a52 = marks18 + marks19
    if a52 == 2:
        pygame.draw.line(screen, RED, (360, 295), (295, 295), 5)
    if a52 == 8:
        pygame.draw.line(screen, WHITE, (360, 295), (295, 295), 5)

    a53 = marks19 + marks14
    if a53 == 2:
        pygame.draw.line(screen, RED, (360, 295), (360, 230), 5)
    if a53 == 8:
        pygame.draw.line(screen, WHITE, (360, 295), (360, 230), 5)

    a54 = marks18 + marks14
    if a54 == 2:
        pygame.draw.line(screen, RED, (360, 230), (295, 295), 5)
    if a54 == 8:
        pygame.draw.line(screen, WHITE, (360, 230), (295, 295), 5)

    a55 = marks13 + marks19
    if a55 == 2:
        pygame.draw.line(screen, RED, (360, 295), (295, 230), 5)
    if a55 == 8:
        pygame.draw.line(screen, WHITE, (360, 295), (295, 230), 5)

    a56 = marks15 + marks20
    if a56 == 2:
        pygame.draw.line(screen, RED, (100, 295), (100, 360), 5)
    if a56 == 8:
        pygame.draw.line(screen, WHITE, (100, 295), (100, 360), 5)

    a57 = marks20 + marks21
    if a57 == 2:
        pygame.draw.line(screen, RED, (100, 360), (165, 360), 5)
    if a57 == 8:
        pygame.draw.line(screen, WHITE, (100, 360), (165, 360), 5)

    a58 = marks21 + marks16
    if a58 == 2:
        pygame.draw.line(screen, RED, (165, 295), (165, 360), 5)
    if a58 == 8:
        pygame.draw.line(screen, WHITE, (165, 295), (165, 360), 5)

    a59 = marks15 + marks21
    if a59 == 2:
        pygame.draw.line(screen, RED, (100, 295), (165, 360), 5)
    if a59 == 8:
        pygame.draw.line(screen, WHITE, (100, 295), (165, 360), 5)

    a60 = marks20 + marks16
    if a60 == 2:
        pygame.draw.line(screen, RED, (165, 295), (100, 360), 5)
    if a60 == 8:
        pygame.draw.line(screen, WHITE, (165, 295), (100, 360), 5)

    a61 = marks21 + marks22
    if a61 == 2:
        pygame.draw.line(screen, RED, (230, 360), (165, 360), 5)
    if a61 == 8:
        pygame.draw.line(screen, WHITE, (230, 360), (165, 360), 5)

    a62 = marks22 + marks17
    if a62 == 2:
        pygame.draw.line(screen, RED, (230, 360), (230, 295), 5)
    if a62 == 8:
        pygame.draw.line(screen, WHITE, (230, 360), (230, 295), 5)

    a63 = marks16 + marks22
    if a63 == 2:
        pygame.draw.line(screen, RED, (230, 360), (165, 295), 5)
    if a63 == 8:
        pygame.draw.line(screen, WHITE, (230, 360), (165, 295), 5)

    a64 = marks21 + marks17
    if a64 == 2:
        pygame.draw.line(screen, RED, (230, 295), (165, 360), 5)
    if a64 == 8:
        pygame.draw.line(screen, WHITE, (230, 295), (165, 360), 5)

    a65 = marks22 + marks23
    if a65 == 2:
        pygame.draw.line(screen, RED, (230, 360), (295, 360), 5)
    if a65 == 8:
        pygame.draw.line(screen, WHITE, (230, 360), (295, 360), 5)

    a66 = marks23 + marks18
    if a66 == 2:
        pygame.draw.line(screen, RED, (295, 295), (295, 360), 5)
    if a66 == 8:
        pygame.draw.line(screen, WHITE, (295, 295), (295, 360), 5)

    a67 = marks17 + marks23
    if a67 == 2:
        pygame.draw.line(screen, RED, (230, 295), (295, 360), 5)
    if a67 == 8:
        pygame.draw.line(screen, WHITE, (230, 295), (295, 360), 5)

    a68 = marks22 + marks18
    if a68 == 2:
        pygame.draw.line(screen, RED, (295, 295), (230, 360), 5)
    if a68 == 8:
        pygame.draw.line(screen, WHITE, (295, 295), (230, 360), 5)

    a69 = marks23 + marks24
    if a69 == 2:
        pygame.draw.line(screen, RED, (360, 360), (295, 360), 5)
    if a69 == 8:
        pygame.draw.line(screen, WHITE, (360, 360), (295, 360), 5)

    a70 = marks24 + marks19
    if a70 == 2:
        pygame.draw.line(screen, RED, (360, 360), (360, 295), 5)
    if a70 == 8:
        pygame.draw.line(screen, WHITE, (360, 360), (360, 295), 5)

    a71 = marks23 + marks19
    if a71 == 2:
        pygame.draw.line(screen, RED, (295, 360), (360, 295), 5)
    if a71 == 8:
        pygame.draw.line(screen, WHITE, (295, 360), (360, 295), 5)

    a72 = marks18 + marks24
    if a72 == 2:
        pygame.draw.line(screen, RED, (360, 360), (295, 295), 5)
    if a72 == 8:
        pygame.draw.line(screen, WHITE, (360, 360), (295, 295), 5)


    pygame.time.delay(1500)
    pygame.display.update()

        
    scores = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10,
              a11, a12, a13, a14, a15, a16, a17, a18, a19, a20,
              a21, a22, a23, a24, a25, a26, a27, a28, a29, a30,
              a31, a32, a33, a34, a35, a36, a37, a38, a39, a40,
              a41, a42, a43, a44, a45, a46, a47, a48, a49, a50,
              a51, a52, a53, a54, a55, a56, a57, a58, a59, a60,
              a61, a62, a63, a64, a65, a66, a67, a68, a69, a70,
              a71, a72]

    player1 = [1 if w == 2 else 0*w for w in scores]
    player2 = [1 if v == 8 else 0*v for v in scores]

    player1score = sum(int(y) for y in player1)
    player2score = sum(int(z) for z in player2)

    pygame.time.delay(1000)

    if player1score > player2score:
        text = font2.render("You win: " +str(player1score), True, WHITE)
        screen.blit(text, [147, 412])
        text = font2.render("to " +str(player2score), True, WHITE)
        screen.blit(text, [249, 412])
        pygame.display.update()
        
        player1_total = player1_total + 1
        
    elif player1score < player2score:
        text = font2.render("You lose: " +str(player1score), True, WHITE)
        screen.blit(text, [145, 412])
        text = font2.render("to " +str(player2score), True, WHITE)
        screen.blit(text, [253, 412])
        pygame.display.update()
        
        player2_total = player2_total + 1
        
    else:
        text = font2.render("Draw: " +str(player1score), True, WHITE)
        screen.blit(text, [145, 412])
        text = font2.render("to " +str(player2score), True, WHITE)
        screen.blit(text, [225, 412])
        pygame.display.update()
    
        
    pygame.time.delay(4000)

        

    running = running + 1

