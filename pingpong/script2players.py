import turtle
import time
from random import uniform
from playsound import playsound

turtle.tracer(0,0)

turtle.speed(0)


wn = turtle.Screen()
wn.title("PingPong")
wn.bgcolor("black")
wn.setup(height=610,width=800)

# Paddle A

pa = turtle.Turtle()
pa.pu()
pa.color("red")
pa.goto(-350,0)
pa.shape("square")
pa.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B

pb = turtle.Turtle()
pb.pu()
pb.color("blue")
pb.goto(350,0)
pb.shape("square")
pb.shapesize(stretch_wid=5, stretch_len=1)

# Ball

ball = turtle.Turtle()
ball.pu()
ball.color("white")
ball.shape("circle")
balldx = 2
balldy = 0

scoreA = 0
scoreB = 0
# Functions
# Moving the paddles

def pa_up():
    y=pa.ycor()
    y+=30
    pa.sety(y)

def pa_dn():
    y=pa.ycor()
    y-=30
    pa.sety(y)
    
def pb_up():
    y=pb.ycor()
    y+=30
    pb.sety(y)
    
def pb_dn():
    y=pb.ycor()
    y-=30
    pb.sety(y)
    
    
# Pen
    
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.color("white")
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0",align="center",font=("Courier",24))
    
    
wn.listen()
wn.onkeypress(pa_up,"w")
wn.onkeypress(pa_dn,"s")
wn.onkeypress(pb_up,"Up")
wn.onkeypress(pb_dn,"Down")



# Main game loop

while True:
    wn.update()
    
    

    
    # Move ball
    ball.setx(ball.xcor() + balldx)
    ball.sety(ball.ycor() + balldy)
    
    # Border checking
    
    if ball.ycor() > 290:
        ball.sety(290)
        balldy *= -1
        playsound('C:\\Users\\91870\\Desktop\\python games\\pingpong\\wallbounce.wav',False)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        balldy *= -1
        playsound('C:\\Users\\91870\\Desktop\\python games\\pingpong\\wallbounce.wav',False)
    
    # Ball Missing
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        balldx = -2
        scoreA += 1
        pen.clear()
        playsound('C:\\Users\\91870\\Desktop\\python games\\pingpong\\out.wav',False)
        time.sleep(1)
        pen.write("Player A: {}   Player B: {}".format(scoreA,scoreB),align="center",font=("Courier",24))
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        balldx = 2
        scoreB += 1
        pen.clear()
        playsound('C:\\Users\\91870\\Desktop\\python games\\pingpong\\out.wav',False)
        time.sleep(1)
        pen.write("Player A: {}   Player B: {}".format(scoreA,scoreB),align="center",font=("Courier",24))
    
    # paddle and ball collisions
    
    if (ball.xcor() > 330) and (ball.xcor() < 345) and (ball.ycor() < pb.ycor() + 50) and (ball.ycor() > pb.ycor() -50):
        ball.setx(330)
        balldx *=-1
        balldx -= 0.25
        ball.color("blue")
        balldy = uniform(-3,3)
        playsound('C:\\Users\\91870\\Desktop\\python games\\pingpong\\bounce.wav',False)
        
    if (ball.xcor() < -330) and (ball.xcor() > -345) and (ball.ycor() < pa.ycor() + 50) and (ball.ycor() > pa.ycor() -50):
        ball.setx(-330)
        balldx *=-1
        balldx += 0.25
        ball.color("red")
        balldy = uniform(-3,3)
        playsound('C:\\Users\\91870\\Desktop\\python games\\pingpong\\bounce.wav',False)
    time.sleep(0.017)
    
    
    if scoreA == 5:
        pen.clear()
        pen.write("Player A wins",color="red",align="center",font=("Courier",28))
        break
    if scoreB == 5:
        pen.clear()
        pen.write("Player B wins",align="center",font=("Courier",28))
        break