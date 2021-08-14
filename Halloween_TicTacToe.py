import turtle
import time

#set screen and main turtle - only one used
t = turtle.Turtle()
t.speed(0)
t.ht()

screen = turtle.Screen()
screen.bgcolor("black")

#function which draws jack_o_lanterns for Player 1
def draw_jol(x,y):

  def jol_eyes(x,y):
    a = 27
    for i in range(2):
      t.penup()
      t.goto(x-a,y+53)
      t.color("yellow")
      t.pendown()
      t.begin_fill()
      for i in range(3):
        t.fd(20)
        t.lt(120)
      t.end_fill()
      a -= 35

  def jol_nose(x,y):
    t.penup()
    t.goto(x-2.5,y+37.5)
    t.color("yellow")
    t.pendown()
    t.begin_fill()
    for i in range(3):
      t.fd(7.5)
      t.lt(120)
    t.end_fill()
    t.penup()

  def jol_mouth(x,y):
    a = 22.5
    for i in range(4):
      t.penup()
      t.goto(x-a,y+27.5)
      t.begin_fill()
      t.pendown()
      t.setheading(180)
      for i in range(3):
        t.lt(120)
        t.fd(10)
      t.end_fill()
      a -= 12

  def jol_stem(x,y):
    t.penup() 
    t.goto(x-7.5,y+90)
    t.begin_fill()
    t.color("brown")
    t.pendown()
    t.setheading(90)
    for i in range(2):
      t.fd(20)
      t.rt(90)
      t.fd(15)
      t.rt(90)
    t.end_fill()
    t.penup()
    t.color("green")
    t.goto(x+3,y+105)
    t.setheading(45)
    t.shape("turtle")
    t.stamp()
    t.ht()
    t.penup()
  
  t.setheading(0)
  t.penup() 
  t.goto(x,y)
  t.begin_fill()
  t.color("orange")
  t.pendown()
  t.circle(50)
  t.end_fill()
  jol_eyes(x,y)
  jol_nose(x,y)
  jol_mouth(x,y)
  jol_stem(x,y)

#function which draws ghosts for Player 2
def draw_ghost(x,y):

  def ghost_eyes(x,y):
    a = 18
    for i in range(2):
      t.penup()
      t.goto(x-a,y+48)
      t.color("black")
      t.pendown()
      t.begin_fill()
      t.circle(10)
      t.end_fill()
      a -= 35

  def ghost_mouth(x,y):
    t.penup()
    t.goto(x,y+25)
    t.color("black")
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

  def ghost_boo(x,y):
    t.penup()
    t.color("red")
    t.goto(x-12,y+77.5)
    t.pendown()
    t.write("BOO!")
    t.penup()

  t.penup()
  t.setheading(0)
  t.goto(x,y)
  t.pendown()
  t.begin_fill()
  t.color("white")
  t.pendown()
  t.circle(50)
  t.end_fill()
  ghost_eyes(x,y)
  ghost_mouth(x,y)
  ghost_boo(x,y)

#function that creates the tic-tac-toe board
def draw_grid():
  x = -100
  y = -75
  
  for i in range(2):
    t.penup()
    t.color("white")
    t.goto(x,250)
    t.pendown()
    t.setheading(270)
    t.fd(500)
    x += 200
  
  for i in range(2):
    t.penup()
    t.color("white")
    t.goto(-300,y)
    t.pendown()
    t.setheading(0)
    t.fd(600)
    y += 150

#print game instructions - should be skippable
def instructions():
    print("Hi! Welcome to Halloween Tic-Tac-Toe!\n")
    time.sleep(3.5)
    skip = input("Skip instructions? (Y or N): ")
    if skip == 'Y':
      pass
    elif skip == 'N':
      print("The objective is to obtain three spaces in a row, either vertically, horizontally, or diagonally.\n")
      time.sleep(4.5)
      print("t = top, m = middle, b = bottom.")
      time.sleep(3.5)
      print("l = left, m = middle, r = right.")
      time.sleep(3.5)
      print("So for example, top middle = tm and bottom left = bl.\n")
      time.sleep(4)
      print("Any invalid spot choices will abort the game!\n")
      time.sleep(4)
      print("Got it? Go!")
      time.sleep(2)

#game's main function - check whether game won or tie (a & b)
def tic_tac_toe():
  
  a = 0
  b = 0

  row1 = [0,0,0]
  row2 = [0,0,0]
  row3 = [0,0,0]

  print("\nWhat are your names?")
  time.sleep(1.5)
  p1 = input("Player_1: ")
  p2 = input("Player_2: ")
  print('')
  time.sleep(2)
  print("The grid is drawing! Click result and console to switch between the board and the spot chooser.\n")
  draw_grid()

  #check if player 1 has won
  def win_check1(name, name2, row1, row2, row3, var):

    if (row1[0] == 1 and row2[1] == 1 and row3[2] == 1) or (row1[2] == 1 and row2[1] == 1 and row3[0] == 1):
      
      time.sleep(1)
      screen.resetscreen()
      screen.bgcolor("black")
      t.penup()
      t.goto(0,0)
      t.pendown()
      t.color("purple")
      t.ht()
      t.write(str(name) + " Wins!", align="center", font=("Arial", 40, "normal"))
      var = 1
      return var
    
    elif (row1[0] == 1 and row1[1] == 1 and row1[2] == 1) or (row2[0] == 1 and row2[1] == 1 and row2[2] == 1) or (row3[0] == 1 and row3[1] == 1 and row3[2] == 1):
      
      time.sleep(1)
      screen.resetscreen()
      screen.bgcolor("black")
      t.penup()
      t.goto(0,0)
      t.pendown()
      t.color("purple")
      t.ht()
      t.write(str(name) + " Wins!", align="center", font=("Arial", 40, "normal"))
      var = 1
      return var
    
    elif (row1[0] == 1 and row2[0] == 1 and row3[0] == 1) or (row1[1] == 1 and row2[1] == 1 and row3[1] == 1) or (row1[2] == 1 and row2[2] == 1 and row3[2] == 1):
        
      time.sleep(1)
      screen.resetscreen()
      screen.bgcolor("black")
      t.penup()
      t.goto(0,0)
      t.pendown()
      t.color("purple")
      t.ht()
      t.write(str(name) + " Wins!", align="center", font=("Arial", 40, "normal"))
      var = 1
      return var
          
    else:
      var = 0

  #check if player 2 has won
  def win_check2(name,name2, row1, row2, row3, var):

    if (row1[0] == 2 and row2[1] == 2 and row3[2] == 2) or (row1[2] == 2 and row2[1] == 2 and row3[0] == 2):
      
      time.sleep(1)
      screen.resetscreen()
      screen.bgcolor("black")
      t.penup()
      t.goto(0,0)
      t.pendown()
      t.color("purple")
      t.ht()
      t.write(str(name2) + " Wins!", align="center", font=("Arial", 40, "normal"))
      var = 1
      return var
    
    elif (row1[0] == 2 and row1[1] == 2 and row1[2] == 2) or (row2[0] == 2 and row2[1] == 2 and row2[2] == 2) or (row3[0] == 2 and row3[1] == 2 and row3[2] == 2):
      
      time.sleep(1)
      screen.resetscreen()
      screen.bgcolor("black")
      t.penup()
      t.goto(0,0)
      t.pendown()
      t.color("purple")
      t.ht()
      t.write(str(name2) + " Wins!", align="center", font=("Arial", 40, "normal"))
      var = 1
      return var

    elif (row1[0] == 2 and row2[0] == 2 and row3[0] == 2) or (row1[1] == 1 and row2[1] == 2 and row3[1] == 2) or (row1[2] == 2 and row2[2] == 2 and row3[2] == 2):
      
      time.sleep(1)
      screen.resetscreen()
      screen.bgcolor("black")
      t.penup()
      t.goto(0,0)
      t.pendown()
      t.color("purple")
      t.ht()
      t.write(str(name2) + " Wins!", align="center", font=("Arial", 40, "normal"))
      var = 1
      return var
    
    else:
      var = 0

  #Main loop - use 'x' to count # of choices - use 'y' to break loop 
  x = 0
  y = True

  while x < 9 and y == True:
  
    #player 1's turn
    if x % 2 == 0:
      spot = input("\n" + p1 + ", type your spot: ")
      if spot == "tl" and row1[0] == 0:
        row1[0] = 1
        draw_jol(-200,100)
        if win_check1(p1,p2,row1,row2,row3,a) == True:
          a = 1
          y = False
        x += 1
      elif spot == "tm" and row1[1] == 0:
        row1[1] = 1
        draw_jol(0,100)
        if win_check1(p1,p2,row1,row2,row3,a) == True:
          a = 1
          y = False
        x += 1
      elif spot == "tr" and row1[2] == 0:
        row1[2] = 1
        draw_jol(200,100)
        if win_check1(p1,p2,row1,row2,row3,a) == True:
          a = 1
          y = False
        x += 1
      elif spot == "bl" and row3[0] == 0:
        row3[0] = 1
        draw_jol(-200,-200)
        if win_check1(p1,p2,row1,row2,row3,a) == True:
          a = 1
          y = False
        x += 1
      elif spot == "bm" and row3[1] == 0:
        row3[1] = 1
        draw_jol(0,-200)
        if win_check1(p1,p2,row1,row2,row3,a) == True:
          a = 1
          y = False
        x += 1
      elif spot == "br" and row3[2] == 0:
        row3[2] = 1
        draw_jol(200,-200)
        if win_check1(p1,p2,row1,row2,row3,a) == True:
          a = 1
          y = False
        x += 1
      elif spot == "ml" and row2[0] == 0:
        row2[0] = 1
        draw_jol(-200,-50)
        if win_check1(p1,p2,row1,row2,row3,a) == True:
          a = 1
          y = False
        x += 1
      elif spot == "mm" and row2[1] == 0:
        row2[1] = 1
        draw_jol(0,-50)
        if win_check1(p1,p2,row1,row2,row3,a) == True:
          a = 1
          y = False
        x += 1
      elif spot == "mr" and row2[2] == 0:
        row2[2] = 1
        draw_jol(200,-50)
        if win_check1(p1,p2,row1,row2,row3,a) == True:
          a = 1
          y = False
        x += 1
      else:
        print("Not valid move! Restart!")
        y = False
    
    #player 2's turn
    else:
      spot = input(p2 + ", type your spot: ")
      if spot == "tl" and row1[0] == 0:
        row1[0] = 2
        draw_ghost(-200,100)
        if win_check2(p1,p2,row1,row2,row3,b) == True:
          b = 1
          y = False
        x += 1
      elif spot == "tm" and row1[1] == 0:
        row1[1] = 2
        draw_ghost(0,100)
        if win_check2(p1,p2,row1,row2,row3,b) == True:
          b = 1
          y = False
        x += 1
      elif spot == "tr" and row1[2] == 0:
        row1[2] = 2
        draw_ghost(200,100)
        if win_check2(p1,p2,row1,row2,row3,b) == True:
          b = 1
          y = False
        x += 1
      elif spot == "bl" and row3[0] == 0:
        row3[0] = 2
        draw_ghost(-200,-200)
        if win_check2(p1,p2,row1,row2,row3,b) == True:
          b = 1
          y = False
        x += 1
      elif spot == "bm" and row3[1] == 0:
        row3[1] = 2
        draw_ghost(0,-200)
        if win_check2(p1,p2,row1,row2,row3,b) == True:
          b = 1
          y = False
        x += 1
      elif spot == "br" and row3[2] == 0:
        row3[2] = 2
        draw_ghost(200,-200)
        if win_check2(p1,p2,row1,row2,row3,b) == True:
          b = 1
          y = False
        x += 1
      elif spot == "ml" and row2[0] == 0:
        row2[0] = 2
        draw_ghost(-200,-50)
        if win_check2(p1,p2,row1,row2,row3,b) == True:
          b = 1
          y = False
        x += 1
      elif spot == "mm" and row2[1] == 0:
        row2[1] = 2
        draw_ghost(0,-50)
        if win_check2(p1,p2,row1,row2,row3,b) == True:
          b = 1
          y = False
        x += 1
      elif spot == "mr" and row2[2] == 0:
        row2[2] = 2
        draw_ghost(200,-50)
        if win_check2(p1,p2,row1,row2,row3,b) == True:
          b = 1
          y = False
        x += 1
      else:
        print("Not valid move! Restart!")
        y = False

    #check for ties
    if row1[0] != 0 and row1[1] != 0 and row1[2] != 0 and row2[0] != 0 and row2[1] != 0 and row2[2] != 0 and row3[0] != 0 and row3[1] != 0 and row3[2] != 0 and x == 9:
      
      if a == 0 and b == 0:
        time.sleep(1)
        screen.resetscreen()
        screen.bgcolor("black")
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.color("purple")
        t.ht()
        t.write("It's a tie!", align="center", font=("Arial", 40, "normal"))
        y = False

#print instructions, then begin game
instructions()
tic_tac_toe()