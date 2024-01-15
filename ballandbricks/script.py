# powerup color
# powerup frequency



import turtle
from random import choice,randint
import time
import playsound
playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\soundtrack.wav",False)


debugging = False

turtle.tracer(0)
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1400,height=800)

# Border with Ball
chances = 3
ball = turtle.Turtle()
ball.color("white")
ball.shape("circle")
ball.shapesize(0.5)
ball.pu()
ball.goto(-380,-380)
ball.pd()
for i in range(4):
    ball.fd(760)
    ball.lt(90)
ball.pu()
ball.goto(0,-200)
ball.color("grey")

balldx = 8
balldy = 10





# pen
pen = turtle.Turtle()
pen.color("white")
pen.ht()
pen.pu()
pen.goto(400,200)
pen.write("Chances: {}".format(chances),align='left',font=("Courier",10))




# debugger
if debugging == True:
    debug = turtle.Turtle()
    debug.ht()
    debug.color('white')






# Paddle
paddle = turtle.Turtle()
paddle.color("grey")
paddle.shape("square")
paddlewidth = 40
paddlesize=3
paddle.shapesize(0.75,paddlesize)
paddle.pu()
paddle.goto(0,-350)


# Bricks
bricks = []
for i in range(350,119,-30):
    for j in range(-350,351,50):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.shapesize(1.2,2.2)
        brick.color(choice(["red","blue","yellow","white","cyan","magenta","grey","green","purple","violet"]))
        brick.pu()
        brick.goto(j,i)
        bricks.append(brick)
    
def right():
    x = paddle.xcor()
    if x < 320:
        x += 20
        paddle.setx(x)
    
def left():
    x = paddle.xcor()
    if x > -320:
        x -= 20
        paddle.setx(x)

def right2():
    x = paddle.xcor()
    if x < 320:
        x += 50
    paddle.setx(x)

def left2():
    x = paddle.xcor()
    if x > -320:
        x -= 50
    paddle.setx(x)

def blast():
    global bricks,bomb
    if bomb == True:
        playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\blast.wav",False)
        for brick in bricks:
            if ball.distance(brick) < 200:
                brick.ht()
                del bricks[bricks.index(brick)]
                bomb = False
    ball.color("grey")
    ball.shapesize(0.5)
    
wn.listen()
wn.onkeypress(right,"j")
wn.onkeypress(left,"f")
wn.onkeypress(right2,"k")
wn.onkeypress(left2,"d")
wn.onkeypress(blast,"h")


# powerups
poweronscreen = False
power = turtle.Turtle()
bomb = False
power.penup()
power.shape("square")
type = ""

def powerfunc(x,y):
    global type,power,poweronscreen
    power.st()
    type = choice(['white','orange','blue','cyan','magenta','red','green'])
    power.color(type)
    power.goto(x,y)
    poweronscreen = True




time.sleep(2)

while True:
    turtle.update()
    
    # debugging block
    if debugging == True:
        debug.clear()
        debug.write(balldy,font=("Courier",20))
    
    
    # Game completion
    if bricks == []:
        pen.clear()
        pen.home()
        pen.write("Game Complete", align="center", font=("Courier",35))
        break
    
    
    
    
    
    
    # Moving Ball
    x=ball.xcor()
    y=ball.ycor()
    ball.setx(x+balldx)
    ball.sety(y+balldy)
    
    # Border checking
    if ball.xcor() > 375:
        playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\ballbounce.wav",False)
        ball.setx(365)
        balldx *= -1
    if ball.xcor() < -375:
        playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\ballbounce.wav",False)
        ball.setx(-365)
        balldx *= -1
    if ball.ycor() > 370:
        playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\ballbounce.wav",False)
        ball.sety(370)
        balldy *= -1
    
    # Ball drop
    if ball.ycor() < -400:
        playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\miss.wav",False)
        pen.clear()
        chances -= 1
        pen.write("Chances: {}".format(chances),align="left",font=("Courier",10))
        if chances == 0:
            pen.home()
            pen.clear()
            pen.write("Game Over",align="center",font=("Courier",40))
            break
        balldy = 8
        paddlesize = 3
        paddle.shapesize(0.75,paddlesize)
        paddlewidth = 40
        ball.shapesize(0.5)
        ball.color('grey')
        ball.goto(0,0)
        time.sleep(2)
    
    # Ball and Paddle collision

    if ball.ycor() < -330 and ball.ycor() > -355 and ball.xcor() > paddle.xcor()-paddlewidth and ball.xcor() < paddle.xcor()+paddlewidth:
        if abs(balldy) > 10:
            playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\fastplay.wav",False)
        elif abs(balldy) < 5:
            playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\boing.wav",False)
        else:
            playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\smallballbounce.wav",False)
            
        balldy = abs(balldy)
        x = ball.xcor() - paddle.xcor()
        balldx = x/3
    
    
    
    # Ball and Brick collision
    for brick in bricks:
        if ball.ycor() > 109 and ball.distance(brick) < 25:
            playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\brickpop.wav",False)
            balldy *= -1
            brick.ht()
            del bricks[bricks.index(brick)]
            if poweronscreen == False:
                n = randint(1,100)
                if n % 5 == 0:
                    playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\poweruppop.wav",False)
                    x = brick.xcor()
                    y = brick.ycor()
                    powerfunc(x,y)
    
    
    # powerup in game
    if poweronscreen == True:
        y = power.ycor()
        y -= 4
        power.sety(y)
        if y < -340 and y > -365 and power.xcor() < paddle.xcor()+paddlewidth and power.xcor() > paddle.xcor()-paddlewidth:
            power.ht()
            poweronscreen = False
            if type == "red":
                ball.color("red")
                playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\powerup2.wav",False)
                balldy = abs(balldy) + 7
                paddlsize = 2
            if type == "blue":
                ball.color("blue")
                playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\ballslow.wav",False)
                balldy = abs(balldy) - 4
            if type == "magenta":
                playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\ballsizeinc.wav",False)
                paddlesize+=2
                paddle.shapesize(0.75,paddlesize)
                paddlewidth += 20
            if type == "green":
                playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\paddleshrink.wav",False)
                paddlesize-=2
                paddle.shapesize(0.75,paddlesize)
                paddlewidth -= 20
            if type == "cyan":
                playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\powerup3.wav",False)
                ball.color("cyan")
                balldy = abs(balldy) + 4
                ball.shapesize(0.1)
            if type == "white":
                ball.color("white")
                playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\ballsizeinc.wav",False)
                ball.shapesize(1)
                bomb = True
            if type == "orange":
                ball.color("orange")
                balldy = abs(balldy) + 4
                playsound.playsound("C:\\Users\\91870\\Desktop\\python games\\ballandbricks\\powerup1.wav",False)
                ball.shapesize(0.1)
            
    # powerup drop
    if power.ycor() < -400:
        power.ht()
        poweronscreen = False


    time.sleep(0.025)