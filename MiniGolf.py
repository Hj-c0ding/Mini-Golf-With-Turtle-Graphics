#Imports ---------------------
import turtle as trtl
import math
import random as rand

#Screen Setup --------------
wn = trtl.Screen()
wn.colormode(255)
wn.bgcolor([186, 194, 188])
wn.setup(width=575, height=575, startx=0, starty=0)
wn.title("Menu")

#Turtle List of Turtles on the Field -----------------
turtleList = []

#border setup--------
wn.tracer(False)
border = trtl.Turtle()
border.width(20)
border.penup()
border.begin_poly()
border.goto(500, 0)
border.goto(500, 500)
border.goto(0, 500)
border.goto(0, 0)
border.end_poly()

#border shape change to make the playing area
bordBorder = trtl.Shape("compound")
component_one = border.get_poly()
bordBorder.addcomponent(component_one, "green", "white")
wn.addshape("Border", shape=bordBorder)
border.shape("Border")
border.goto(-250,250)
wn.tracer(True)
#---------------------

#Flag Global variable --------
wn.tracer(False)
flag = trtl.Turtle()
flag.width(20)
flag.penup()
flag.begin_poly()
flag.goto(0, 22)
flag.goto(15, 15)
flag.goto(0, 8)
flag.goto(0, 0)
flag.end_poly()

#flag custom shape change
flagBorder = trtl.Shape("compound")
component_two = flag.get_poly()
flagBorder.addcomponent(component_two, "red", "black")
wn.addshape("Flag", shape=flagBorder)
flag.shape("Flag")
flag.ht()
flag.setheading(90)
wn.tracer(True)
turtleList.append(flag)

#Hole Global Variable -----------
hole = trtl.Turtle(shape = "circle")
turtleList.append(hole)
hole.ht()

#Ghost Global Variable ----------
ghost = trtl.Turtle()
ghost.shapesize(0.25,0.25)
turtleList.append(ghost)
ghost.ht()

#Ball Global Variable -----------
ball = trtl.Turtle(shape="circle")
turtleList.append(ball)
ball.ht()

#Circle1 Global Variable ---------
circle1 = trtl.Turtle(shape="circle")
turtleList.append(circle1)
circle1.ht()

#Square1 Global Variable -----------
square1 = trtl.Turtle(shape="square")
turtleList.append(square1)
square1.ht()

#Vertical Line1 Global Variable ------------
vertLine1 = trtl.Turtle("square")
turtleList.append(vertLine1)
vertLine1.ht()

#Horizontal Line1 Global Variable ----------
horizzLine1 = trtl.Turtle("square")
turtleList.append(horizzLine1)
horizzLine1.ht()

#Exit Button Setup ------------
exitButton = trtl.Turtle(shape = "circle")
exitButton.color("white")
exitButton.penup()
wn.tracer(0)
exitButton.rt(90)
exitButton.fd(50)
wn.tracer(1)


#Play Button Setup --------------
playButton = trtl.Turtle(shape="circle")
playButton.color("white")
playButton.penup()
wn.tracer(0)
playButton.lt(90)
playButton.fd(50)
wn.tracer(1)

#Next Button Setup -----------------
nextButton = trtl.Turtle(shape="circle")
nextButton.color("white")
nextButton.penup()
nextButton.ht()
nextButton.goto(-1000, -1000)

#Back Button Setup ------------------
backButton = trtl.Turtle(shape="circle")
backButton.color("white")
backButton.penup()
backButton.ht()
backButton.goto(-1000, -1000)

#Write the Button Labels
playButton.write("PLAY", move=False, align='center', font=('Arial', 35, 'bold'))
exitButton.write("EXIT", move=False, align='center', font=('Arial', 35, 'bold'))

#highscore turtle setup ------------------
highscoreTurtle = trtl.Turtle()
highscoreTurtle.penup()
highscoreTurtle.color("white")
highscoreTurtle.ht()
highscoreTurtle.goto(125, 250)

#current score turtle setup --------------
currentScoreTurtle = trtl.Turtle()
currentScoreTurtle.penup()
currentScoreTurtle.color("white")
currentScoreTurtle.ht()
currentScoreTurtle.goto(-125, 250)

#Variables -------------------
initial = [0, 0]
prevCord = [0, 0]
numOfShots = 0
highscore = -1
rPressed = False

#Functions --------------------
def startGame(x, y):
  wn.title("Level")
  global rPressed
  if rPressed:
    rPressed = False
    wn.tracer(0)
  backButton.clear()
  nextButton.clear()
  nextButton.ht()
  backButton.ht()
  backButton.goto(-1000, -1000)
  nextButton.goto(-1000, -1000)
  wn.tracer(1)
  global numOfShots
  global highscore
  numOfShots = 0
  playButton.clear()
  exitButton.clear()
  playButton.ht()
  exitButton.ht()
  playButton.goto(1000, 1000)
  exitButton.goto(1000, 1000)
  #score setup -----------
  highscoreTurtle.clear()
  currentScoreTurtle.clear()
  if (highscore < 0):
    highscoreTurtle.write("High Score: " + "--", move=False, align='center', font=('Arial', 15, 'bold'))
  else:
    highscoreTurtle.write("High Score: " + str(highscore), move=False, align='center', font=('Arial', 15, 'bold'))
  currentScoreTurtle.write("Number of Tries: " + str(numOfShots), move=False, align='center', font=('Arial', 15, 'bold'))  
  #flag setup ---------
  flag.penup()
  wn.tracer(0)
  flag.goto(200,203.5)
  flag.st()
  wn.tracer(1)
  
  #ball setup ---------
  ball.st()
  ball.penup()
  ball.shapesize(0.5, 0.5)
  ball.color("white")
  wn.tracer(0)
  ball.goto(-200, -200)
  wn.tracer(1)
  
  #hole setup ------------
  hole.st()
  hole.penup()
  hole.color("black")
  hole.shapesize(0.75, 0.75)
  wn.tracer(0)
  hole.goto(200,200)
  wn.tracer(1)
  
  #ghost(pointer) setup --------------
  ghost.penup()
  ghost.color("white")
  ghost.ht()
  ghost.speed(0)
  ghost.shapesize(0.5, 0.5)
  
  #circle obstacle #1 setup -----------
  circle1.penup()
  circle1.st()
  circle1.color("white")
  circle1.shapesize(3, 3)
  circle1.speed(0)

  #square obstacle #1 setup -------------
  square1.penup()
  square1.st()
  square1.color("white")
  square1.shapesize(2, 2)
  square1.speed(0)

  #vertLine1 setup -----------------
  vertLine1.penup()
  vertLine1.st()
  vertLine1.color("white")
  vertLine1.speed(0)
  vertLine1.shapesize(6, 0.5)

  #horizontalLine1 setup -------------
  horizzLine1.penup()
  horizzLine1.st()
  horizzLine1.color("white")
  horizzLine1.speed(0)
  horizzLine1.shapesize(0.5, 6)
  
  #randomizer placement ------------
  wn.tracer(0)
  randomizerDone = False
  while (randomizerDone == False):
    circle1.goto(rand.randint(-220, 220), rand.randint(-220, 220))
    if (circle1.distance(ball.pos()) <= 35 or circle1.distance(hole.pos()) <= 37.5):
      continue
    else:
      square1.goto(rand.randint(-230, 230), rand.randint(-230, 230))
      squarex = square1.xcor()
      squarey = square1.ycor()
      holeToSquarexDist = abs(squarex - hole.xcor())
      holeToSquareyDist = abs(squarey - hole.ycor())
      circleToSquarexDist = abs(squarex - circle1.xcor())
      circleToSquareyDist = abs(squarey - circle1.ycor())
      if (square1.distance(ball.pos()) <= 33.3 or holeToSquarexDist <= 27.5 or holeToSquareyDist <= 27.5 or circleToSquarexDist <= 50 or circleToSquareyDist <= 50):
        continue
      else:
        vertLine1.goto(rand.randint(-190, 245), rand.randint(-135, 190))
        holeToVertLinexDist = abs(vertLine1.xcor() - hole.xcor())
        holeToVertLineyDist = abs(vertLine1.ycor() - hole.ycor())
        squareToVertLinexDist = abs(vertLine1.xcor() - square1.xcor())
        squareToVertLineyDist = abs(vertLine1.ycor() - square1.ycor())
        circleToVertLinexDist = abs(vertLine1.xcor() - circle1.xcor())
        circleToVertLineyDist = abs(vertLine1.ycor() - circle1.ycor())
        if (holeToVertLinexDist <= 12.5 or holeToVertLineyDist <= 67.5 or squareToVertLinexDist <= 25 or squareToVertLineyDist <= 80 or circleToVertLinexDist <= 35 or circleToVertLineyDist <= 90):
          continue
        else:
          horizzLine1.goto(rand.randint(-135, 190), rand.randint(-190, 245))
          holeToHorizzLinexDist = abs(horizzLine1.xcor() - hole.xcor())
          holeToHorizzLineyDist = abs(horizzLine1.ycor() - hole.ycor())
          squareToHorizzLinexDist = abs(horizzLine1.xcor() - square1.xcor())
          squareToHorizzLineyDist = abs(horizzLine1.ycor() - square1.ycor())
          circleToHorizzLinexDist = abs(horizzLine1.xcor() - circle1.xcor())
          circleToHorizzLineyDist = abs(horizzLine1.ycor() - circle1.ycor())
          vertLineToHorizzLinexDist = abs(horizzLine1.xcor() - vertLine1.xcor())
          vertLineToHorizzLineyDist = abs(horizzLine1.ycor() - vertLine1.ycor())
          if (holeToHorizzLinexDist <= 67.5 or holeToHorizzLineyDist <= 12.5 or squareToHorizzLinexDist <= 80 or squareToHorizzLineyDist <= 25 or circleToHorizzLinexDist <= 90 or circleToHorizzLineyDist <= 35 or vertLineToHorizzLinexDist <= 65 or vertLineToHorizzLineyDist <= 65):
            continue
          else: 
            randomizerDone = True
  wn.tracer(1)   
  
  #ball prompt + instructions ------------
  ball.write("Click + drag the ball to move it!", move=False, align='left', font=('Arial', 10, 'bold'))

def changeScreen():
  global rPressed
  if (rPressed):
    x = 0
    y = 0
    rPressed = False
    nextScreen(x, y)
  else:
    wn.title(" ")
    wn.tracer(1)
    for i in turtleList:
      i.ht()
    for i in turtleList:
      wn.tracer(0)
      i.goto(1000, 1000)
      wn.tracer(1)
    nextButton.goto(0, 50)
    backButton.goto(0, -50)
    backButton.write("BACK TO TITLE", move=False, align='center', font=('Arial', 35, 'bold'))
    nextButton.write("PLAY AGAIN", move=False, align='center', font=('Arial', 35, 'bold'))
    nextButton.st()
    backButton.st()
  
def backScreen():
  global numOfShots
  wn.title("Menu")
  backButton.clear()
  nextButton.clear()
  backButton.ht()
  nextButton.ht()
  backButton.goto(-1000, -1000)
  nextButton.goto(-1000, -1000)
  playButton.goto(0, 50)
  exitButton.goto(0,-50)
  playButton.write("PLAY", move=False, align='center', font=('Arial', 35, 'bold'))
  exitButton.write("EXIT", move=False, align='center', font=('Arial', 35, 'bold'))
  playButton.st()
  exitButton.st()
  numOfShots = 0
  currentScoreTurtle.clear()
  currentScoreTurtle.write("Number of Tries: " + str(numOfShots), move=False, align='center', font=('Arial', 15, 'bold'))  
def nextScreen(x, y):
  wn.tracer(0)
  backButton.clear()
  nextButton.clear()
  nextButton.ht()
  backButton.ht()
  backButton.goto(-1000, -1000)
  nextButton.goto(-1000, -1000)
  wn.tracer(1)
  startGame(x, y)
def playButtonFunc(x, y):
  startGame(x, y)
def exitButtonFunc(x,y):
  trtl.bye()
def nextButtonFunc(x, y):
  nextScreen(x, y)
def backButtonFunc(x, y):
  backScreen()
def initialCord(x, y): #stores in the list "initial" ball position when ball is clicked
  ball.clear()
  global initial
  initial[0] = ball.xcor()
  initial[1] = ball.ycor()

def dragBall(x, y): #tells turtle "ghost" where to go to act like a pointer for aim
  global prevCord
  ghost.setheading(ball.towards(x, y)+180)
  ghost.st()
  if (prevCord[0] != x or prevCord[1] != y): #checks whether the mouse has moved and updates the pointer's position
    wn.tracer(0) #pauses screen updates
    
    #x and y to initial cordinate distances
    xdistance = abs(initial[0] - x)
    ydistance = abs(initial[1] - y)

    #tells ghost to go to the initial ball position
    ghost.goto(initial[0], initial[1])

    #conditionals that check the mouse position relative to the initial position and move the pointer forward in the opposite direction. "prevCord" is also recorded when finished
    if (x < initial[0]): 
      if (y > initial[1]):
        ghost.fd(math.sqrt((xdistance)**2 + (ydistance)**2)/2)
        prevCord[0] = x
        prevCord[1] = y
      elif (y < initial[1]):
        ghost.fd(math.sqrt((xdistance)**2 + (ydistance)**2)/2)
        prevCord[0] = x
        prevCord[1] = y
    elif (x > initial[0]):
      if (y > initial[1]):
        ghost.fd(math.sqrt((xdistance)**2 + (ydistance)**2)/2)
        prevCord[0] = x
        prevCord[1] = y
      elif (y < initial[1]):
        ghost.fd(math.sqrt((xdistance)**2 + (ydistance)**2)/2)
        prevCord[0] = x
        prevCord[1] = y
    wn.update() #resumes screen updates

def yeet(x, y): #tells where ball to go on release
  wn.tracer(1)
  for i in turtleList: #clears any unwanted writing
    i.clear()
  global numOfShots
  global highscore
  ghost.ht()
  distance = (math.sqrt((x-initial[0])**2 + (y-initial[1])**2))*2
  tempdistance = 0
  ball.setheading(ball.towards(x, y)-180)
  while(tempdistance < (distance/2)):
    wn.tracer(0)
    #border collision -------------------- 
    #left wall ---------------------------
    if (ball.xcor() < -245):
      if (ball.heading() > 90 and ball.heading() < 180):
        ball.setheading(180 - ball.heading())
      elif (ball.heading() > 180 and ball.heading() < 270):
        ball.setheading(360-(ball.heading()-180))
      else:
        ball.setheading(ball.heading() + 180)
    #right wall --------------------------
    elif (ball.xcor() > 245):
      if (ball.heading() > 0 and ball.heading() < 90):
        ball.setheading(180 - ball.heading())
      elif (ball.heading() < 360 and ball.heading() > 270):
        ball.setheading(180 + (360-ball.heading()))
      else:
        ball.setheading(ball.heading() + 180)
    #top wall ----------------------------
    elif (ball.ycor() > 245):
      if (ball.heading() > 90 and ball.heading() < 180):
        ball.setheading(180 + (180 - ball.heading()))
      elif (ball.heading() < 90 and ball.heading() > 0):
        ball.setheading(360-ball.heading())
      else:
        ball.setheading(ball.heading() + 180)
    #bottom wall -------------------------
    elif (ball.ycor() < -245):
      if (ball.heading() < 360 and ball.heading() > 270):
        ball.setheading(360-ball.heading())
      elif (ball.heading() < 270 and ball.heading() > 180):
        ball.setheading(180-(ball.heading()-180))
      else:
        ball.setheading(ball.heading() + 180)
        
    #circle collision-------------------------
    if (abs(circle1.xcor() - ball.xcor()) <= 35 and abs(circle1.ycor() - ball.ycor()) <= 35):
      bounceHeading = circle1.towards(ball.pos())
      ball.setheading(bounceHeading)

    #square collision -----------------------
    leftSideX = square1.xcor() - 20
    rightSideX = square1.xcor() + 20
    topSideY = square1.ycor() + 20
    bottomSideY = square1.ycor() - 20
    #left side
    if (ball.xcor() > (leftSideX-5) and bottomSideY <= ball.ycor() <= topSideY and ball.xcor() < leftSideX):
      if (ball.heading() > 0 and ball.heading() < 90):
        ball.setheading(180 - ball.heading())
      elif (ball.heading() < 360 and ball.heading() > 270):
        ball.setheading(180 + (360-ball.heading()))
      else:
        ball.setheading(ball.heading() + 180)
    #right side
    elif (ball.xcor() <= (rightSideX+5) and bottomSideY <= ball.ycor() <= topSideY and ball.xcor() > rightSideX):
      if (ball.heading() > 90 and ball.heading() < 180):
        ball.setheading(180 - ball.heading())
      elif (ball.heading() > 180 and ball.heading() < 270):
        ball.setheading(360-(ball.heading()-180))
      else:
        ball.setheading(ball.heading() + 180)
    #top side
    elif (ball.xcor() <= rightSideX and ball.xcor() >= leftSideX and ball.ycor() <= (topSideY+5) and ball.ycor() > topSideY):
      if (ball.heading() < 360 and ball.heading() > 270):
        ball.setheading(360-ball.heading())
      elif (ball.heading() < 270 and ball.heading() > 180):
        ball.setheading(180-(ball.heading()-180))
      else:
        ball.setheading(ball.heading() + 180)
    #bottom side
    elif (ball.xcor() <= rightSideX and ball.xcor() >= leftSideX and ball.ycor() >= (bottomSideY-5) and ball.ycor() < bottomSideY):
      if (ball.heading() > 90 and ball.heading() < 180):
        ball.setheading(180 + (180 - ball.heading()))
      elif (ball.heading() < 90 and ball.heading() > 0):
        ball.setheading(360-ball.heading())
      else:
        ball.setheading(ball.heading() + 180)
        
    #vertLine1 collision -------------
    leftSideX = vertLine1.xcor() - 5
    rightSideX = vertLine1.xcor() + 5
    topSideY = vertLine1.ycor() + 60
    bottomSideY = vertLine1.ycor() - 60
    #left side 
    if (ball.xcor() > (leftSideX-5) and bottomSideY <= ball.ycor() <= topSideY and ball.xcor() < leftSideX):
      if (ball.heading() > 0 and ball.heading() < 90):
        ball.setheading(180 - ball.heading())
      elif (ball.heading() < 360 and ball.heading() > 270):
        ball.setheading(180 + (360-ball.heading()))
      else:
        ball.setheading(ball.heading() + 180)
    #right side
    elif (ball.xcor() <= (rightSideX+5) and bottomSideY <= ball.ycor() <= topSideY and ball.xcor() > rightSideX):
      if (ball.heading() > 90 and ball.heading() < 180):
        ball.setheading(180 - ball.heading())
      elif (ball.heading() > 180 and ball.heading() < 270):
        ball.setheading(360-(ball.heading()-180))
      else:
        ball.setheading(ball.heading() + 180)
    #top side
    elif (ball.xcor() <= rightSideX and ball.xcor() >= leftSideX and ball.ycor() <= (topSideY+5) and ball.ycor() > topSideY):
      if (ball.heading() < 360 and ball.heading() > 270):
        ball.setheading(360-ball.heading())
      elif (ball.heading() < 270 and ball.heading() > 180):
        ball.setheading(180-(ball.heading()-180))
      else:
        ball.setheading(ball.heading() + 180)
    #bottom side
    elif (ball.xcor() <= rightSideX and ball.xcor() >= leftSideX and ball.ycor() >= (bottomSideY-5) and ball.ycor() < bottomSideY):
      if (ball.heading() > 90 and ball.heading() < 180):
        ball.setheading(180 + (180 - ball.heading()))
      elif (ball.heading() < 90 and ball.heading() > 0):
        ball.setheading(360-ball.heading())
      else:
        ball.setheading(ball.heading() + 180)
        
    #horizzLine1 collision -------------
    leftSideX = horizzLine1.xcor() - 60
    rightSideX = horizzLine1.xcor() + 60
    topSideY = horizzLine1.ycor() + 5
    bottomSideY = horizzLine1.ycor() - 5
    #left side 
    if (ball.xcor() > (leftSideX-5) and bottomSideY <= ball.ycor() <= topSideY and ball.xcor() < leftSideX):
      if (ball.heading() > 0 and ball.heading() < 90):
        ball.setheading(180 - ball.heading())
      elif (ball.heading() < 360 and ball.heading() > 270):
        ball.setheading(180 + (360-ball.heading()))
      else:
        ball.setheading(ball.heading() + 180)
    #right side
    elif (ball.xcor() <= (rightSideX+5) and bottomSideY <= ball.ycor() <= topSideY and ball.xcor() > rightSideX):
      if (ball.heading() > 90 and ball.heading() < 180):
        ball.setheading(180 - ball.heading())
      elif (ball.heading() > 180 and ball.heading() < 270):
        ball.setheading(360-(ball.heading()-180))
      else:
        ball.setheading(ball.heading() + 180)
    #top side
    elif (ball.xcor() <= rightSideX and ball.xcor() >= leftSideX and ball.ycor() <= (topSideY+5) and ball.ycor() > topSideY):
      if (ball.heading() < 360 and ball.heading() > 270):
        ball.setheading(360-ball.heading())
      elif (ball.heading() < 270 and ball.heading() > 180):
        ball.setheading(180-(ball.heading()-180))
      else:
        ball.setheading(ball.heading() + 180)
    #bottom side
    elif (ball.xcor() <= rightSideX and ball.xcor() >= leftSideX and ball.ycor() >= (bottomSideY-5) and ball.ycor() < bottomSideY):
      if (ball.heading() > 90 and ball.heading() < 180):
        ball.setheading(180 + (180 - ball.heading()))
      elif (ball.heading() < 90 and ball.heading() > 0):
        ball.setheading(360-ball.heading())
      else:
        ball.setheading(ball.heading() + 180)
        
    #ball forward movement
    ball.fd((distance/2)/100) #(distance/2)/60 for exact distance
    wn.update()
    tempdistance += ((distance/2)/100)
    if (ball.distance(hole.pos()) < 50):
      flag.ht()
    else:
      flag.st()
    #-----------------
  wn.tracer(1)
  #checks if the ghost is still visible and hides it
  if (ghost.isvisible() == True):
    ghost.ht()

  #Updating Current Number of Tries
  numOfShots += 1
  currentScoreTurtle.clear()
  currentScoreTurtle.write("Number of Tries: " + str(numOfShots), move=False, align='center', font=('Arial', 15, 'bold'))
  
  
  #ball goes into the hole----------------
  if (abs(ball.pos()[0] - hole.pos()[0]) < 12 and abs(ball.pos()[1] - hole.pos()[1]) < 12):
    ball.shapesize(0.25, 0.25)
    ball.goto(hole.pos())
    wn.delay(20)
    wn.tracer(0)
    if (numOfShots < highscore or highscore < 0):
      highscore = numOfShots
      highscoreTurtle.clear()
      highscoreTurtle.write("High Score: " + str(highscore), move=False, align='center', font=('Arial', 15, 'bold'))
    changeScreen()
#-------------
def reset():
  global rPressed
  rPressed = True
  x = 0
  y = 0
  nextScreen(x, y)

#Events ------------------------------
#-----------------------
exitButton.onclick(exitButtonFunc)
playButton.onclick(playButtonFunc)
wn.listen()
backButton.onclick(backButtonFunc)
nextButton.onclick(nextButtonFunc)
ball.onclick(initialCord)
ball.ondrag(dragBall)
ball.onrelease(yeet)
wn.onkeypress(reset, "r")

#Listen and Mainloop Functions -------------
wn.listen()
wn.mainloop()