from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
# import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
# screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball needs to bounce
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()


    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()