from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
score = Scoreboard()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350,0))


screen.listen()
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
game_on = True
ball = Ball()


while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        score.left_score()
        ball.reset()
        ball.bounce_x()
    if ball.xcor() < -380:
        ball.reset()
        ball.bounce_x()
        score.right_score()







screen.exitonclick()