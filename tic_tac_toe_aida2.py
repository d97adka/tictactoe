from turtle import *
import random

#user play is 1 and computer play is 2
#boardlist
blist=[0, 0, 0, 0, 0, 0, 0, 0, 0]

screensize(600,600)
screen=Screen()

def draw_board():
    print('draw board')
    penup()
    goto(-300,100)
    pendown()
    goto(300,100)
    penup()
    goto(-300,-100)
    pendown()
    goto(300,-100)
    penup()
    goto(-100,300)
    pendown()
    goto(-100,-300)
    penup()
    goto(100,300)
    pendown()
    goto(100,-300)
    penup()

#comp plays circle
def draw_c(pos):
    #draw cicle in position 0 to 8
    print('draw circle')
    if pos==0:
        goto(-200,200)
        right(90)
        forward(90)
        left(90)
    elif pos==1:
        goto(0,200)
        right(90)
        forward(90)
        left(90)
    elif pos==2:
        goto(200,200)
        right(90)
        forward(90)
        left(90)
    elif pos==3:
        goto(-200,0)
        right(90)
        forward(90)
        left(90)
    elif pos==4:
        goto(0,0)
        right(90)
        forward(90)
        left(90)
    elif pos==5:
        goto(200,0)
        right(90)
        forward(90)
        left(90)
    elif pos==6:
        goto(-200,-200)
        right(90)
        forward(90)
        left(90)
    elif pos==7:
        goto(0,-200)
        right(90)
        forward(90)
        left(90)
    elif pos==8:
        goto(200,-200)
        right(90)
        forward(90)
        left(90)
    pendown()
    circle(90)
    penup()


#user plays x
def draw_x(pos):
    #draw x in position 0 to 8
    print('draw x')
    if pos==0:
        goto(-200,200)
    elif pos==1:
        goto(0,200)
    elif pos==2:
        goto(200,200)
    elif pos==3:
        goto(-200,0)
    elif pos==4:
        goto(0,0)
    elif pos==5:
        goto(200,0)
    elif pos==6:
        goto(-200,-200)
    elif pos==7:
        goto(0,-200)
    elif pos==8:
        goto(200,-200)
    left(45)
    forward(90)
    left(180)
    pendown()
    forward(180)
    penup()
    right(135)
    forward(130)
    pendown()
    right(135)
    forward(180)
    left(45)
    penup()


#this cane be done better by only checking relevant and by going trough the list with for loop
#check if there are two in row and
#return position for best next move
def get_best_move(p):
    pos=-1
    if (blist[1] == p and blist[2] == p )\
    or (blist[3] == p and blist[6] == p)\
    or (blist[4] == p and blist[8] == p):
        if blist[0] == 0:
            pos = 0
   
    elif (blist[0] == p and blist[2] == p)\
    or (blist[4] == p and blist[7] == p):
        if blist[1] == 0:
            pos = 1
   
    elif (blist[0] == p and blist[1] == p)\
    or (blist[5] == p and blist[8] == p)\
    or (blist[6] == p and blist[4] == p):
        if blist[2] == 0:
            pos = 2

    elif (blist[0] == p and blist[6] == p)\
    or (blist[4] == p and blist[5] == p):
        if blist[3] == 0:
            pos = 3

    elif (blist[2] == p and blist[8] == p)\
    or (blist[3] == p and blist[4] == p):
        if blist[5] == 0:
            pos = 5
        
    if (blist[0] == p and blist[3] == p)\
    or (blist[2] == p and blist[4] == p)\
    or (blist[7] == p and blist[8] == p):
        if blist[6] == 0:
            pos = 6
        
    if (blist[1] == p and blist[4] == p)\
    or (blist[6] == p and blist[8] == p):
        if blist[7] == 0:
            pos = 7
   
    if (blist[0] == p and blist[4] == p)\
    or (blist[2] == p and blist[5] == p)\
    or (blist[6] == p and blist[7] == p):
        if blist[8] == 0:
            pos = 8  
    return pos
 
def get_random_move():
    #get only free positions from blist
    free_pos_list = []
    for i in range(len(blist)):
        if blist[i]==0:
            free_pos_list.append(i)
        
    #select random of free positions
    print("Freepos list")
    print(free_pos_list)
    if len(free_pos_list)>0:
        random_pos=random.choice(free_pos_list)
        return random_pos
    return -1

#return position of play 0 to 8 based on x and y
def user_play_event(x,y):
    clicked_pos = 0
    
    if x > -300 and x < -100 and y < 300 and y > 100:
        clicked_pos = 0
    elif x > -100 and x < 100 and y < 300 and y > 100:
        clicked_pos = 1
    elif x > 100 and x < 300 and y < 300 and y > 100:
        clicked_pos = 2
    elif x > -300 and x < -100 and y < 100 and y > -100:
        clicked_pos = 3
    elif x > -100 and x < 100 and y < 100 and y > -100:
        clicked_pos = 4
    elif x > 100 and x < 300 and y < 100 and y > -100:
        clicked_pos = 5
    elif x > -300 and x < -100 and y < -100 and y > -300:
        clicked_pos = 6
    elif x > -100 and x < 100 and y < -100 and y > -300:
        clicked_pos = 7
    elif x > 100 and x < 300 and y < -100 and y > -300:
        clicked_pos = 8
    print(clicked_pos)
    user_play(clicked_pos)
    
    
#events start here
def start_play():
    onscreenclick(user_play_event)

def user_play(pos):
    #check it is not already taken position
    if blist[pos] != 0:
        print('Already used position! Click on other');
        return
    
    blist[pos]=1
    draw_x(pos)
    print("List after user move")
    print(blist)
    isDone = check_win_done('User')
    if isDone:
        restart_finish()
    else:
        computer_play()
  

#Let computer play
def computer_play():
    comp_move_done = False
    #check if position 4 middle taken and take it
    if blist[4] == 0:
        print("one")
        blist[4]=2
        draw_c(4)
        comp_move_done = True

    #check if computer has 2 in row and set third
    if comp_move_done == False:
        comp_pos = get_best_move(2)
        if comp_pos != -1:
            print("two")
            blist[comp_pos]=2
            draw_c(comp_pos)
            comp_move_done = True

    #check if user has 2 in row and stop third
    if comp_move_done == False:
        comp_pos = get_best_move(1)
        if comp_pos != -1:
            print("three")
            blist[comp_pos]=2
            draw_c(comp_pos)
            comp_move_done = True

    #set random among not set positions
    if comp_move_done == False:
        comp_pos=get_random_move()
        print("Random move")
        print(comp_pos)
        if comp_pos != -1:
            print("four")
            blist[comp_pos]=2
            draw_c(comp_pos)
            comp_move_done = True

    print("List after computer move")
    print(blist)
    isDone = check_win_done('Computer')
    if isDone:
        restart_finish()

#check if three in row are: 1 or 2
#combinations: 012, 345, 678, 036, 147, 258, 048, 246
#or game done: all positions taken. No 0 in blist
def check_win_done(who):
    lookup=1
    if who=='Computer':
        lookup=2
        
    if blist[0]==lookup and blist[1]==lookup and blist[2]==lookup:
        print(who + ' won!')
        return True
    elif blist[3]==lookup and blist[4]==lookup and blist[5]==lookup:
        print(who + ' won!')
        return True
    elif blist[6]==lookup and blist[7]==lookup and blist[8]==lookup:
        print(who + ' won!')
        return True
    elif blist[0]==lookup and blist[3]==lookup and blist[6]==lookup:
        print(who + ' won!')
        return True
    elif blist[1]==lookup and blist[4]==lookup and blist[7]==lookup:
        print(who + ' won!')
        return True
    elif blist[2]==lookup and blist[5]==lookup and blist[8]==lookup:
        print(who + ' won!')
        return True
    elif blist[0]==lookup and blist[4]==lookup and blist[8]==lookup:
        print(who + ' won!')
        return True
    elif blist[2]==lookup and blist[4]==lookup and blist[6]==lookup:
        print(who + ' won!')
        return True
    elif 0 not in blist:
        print("No Winner. Game over!")
        return True
    else:
        return False

def restart_finish():
    restart=input("Do you want to reset the game and start over (y) or finish the game (n)? ")
    if restart == 'y':
        clearscreen()
        resetscreen()
        for i in range(0, len(blist)):
            blist[i] = 0
        init_game()
    elif restart == 'n':
        #done()
        screen.bye()
        exit()

def init_game():
    speed(0)
    ht()
    draw_board()
    isWin=False
    start_play()
    
#main code
title("Aida's Tic tac Toe")
init_game()
