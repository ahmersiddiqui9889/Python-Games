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

score = 0
highscore = 0
misses = 0
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
# Functions
# Moving the paddles

def pa_up():
    y=pa.ycor()
    if y < 181:
        y+=60
        pa.sety(y)

def pa_dn():
    y=pa.ycor()
    if y > -181:
        y-=60
        pa.sety(y)
    
def pb_up():
    y=pb.ycor()
    if y < 181:
        y+=60
        pb.sety(y)
    
def pb_dn():
    y=pb.ycor()
    if y > -181:
        y-=60
        pb.sety(y)
    
    
# Border
    
border = turtle.Turtle()
border.hideturtle()
border.pu()
border.color("white")
border.goto(-380,-300)
border.pd()
for i in range(2):
    border.fd(760)
    border.lt(90)
    border.fd(600)
    border.lt(90)
border.pu()



# Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.pu()
pen.goto(0,250)
pen.color('white')
pen.write("Score: {}   Highscore: {}   Misses: {}".format(score,highscore,misses),align="center",font=("Courier",24))
    
    
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
    
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0,0)
        balldx = -2
        pen.clear()
        misses += 1
        playsound('C:\\Users\\91870\\Desktop\\python games\\pingpong\\out.wav',False)
        score = 0
        time.sleep(1)
        pen.write("Score: {}   Highscore: {}   Misses: {}".format(score,highscore,misses),align="center",font=("Courier",24))
    
    # paddle and ball collisions
    
    if (ball.xcor() > 330) and (ball.xcor() < 355) and (ball.ycor() < pb.ycor() + 50) and (ball.ycor() > pb.ycor() -50):
        ball.setx(330)
        balldx *=-1
        balldx -= 0.25
        ball.color("blue")
        score+=10
        if score > highscore:
            highscore = score
        pen.clear()
        pen.write("Score: {}   Highscore: {}   Misses: {}".format(score,highscore,misses),align="center",font=("Courier",24))
        balldy = uniform(-3,3)
        playsound('C:\\Users\\91870\\Desktop\\python games\\pingpong\\bounce.wav',False)
        
    if (ball.xcor() < -330) and (ball.xcor() > -355) and (ball.ycor() < pa.ycor() + 50) and (ball.ycor() > pa.ycor() -50):
        ball.setx(-330)
        balldx *=-1
        balldx += 0.25
        ball.color("red")
        score+=10
        if score > highscore:
            highscore = score
        pen.clear()
        pen.write("Score: {}   Highscore: {}   Misses: {}".format(score,highscore,misses),align="center",font=("Courier",24))
        balldy = uniform(-3,3)
        playsound('C:\\Users\\91870\\Desktop\\python games\\pingpong\\bounce.wav',False)
    time.sleep(0.025)
    