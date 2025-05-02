from turtle import Screen
from game import Game
from mato import Mato
from point import Point
from points import Points
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Nokia")
screen.tracer(0)

game = Game()
mato = Mato()
point = Point()
points = Points()

def game_over():
    points.game_over_text()
    game.end_game()

screen.listen()
screen.onkey(mato.up, "Up")
screen.onkey(mato.down, "Down")
screen.onkey(mato.left, "Left")
screen.onkey(mato.right, "Right")
screen.onkey(game_over, "Escape")

while game.game_is_on:
    screen.update()
    time.sleep(0.1)
    mato.move()

    # Detect collision with point
    if mato.head.distance(point) < 20:
        point.refresh()
        mato.grow_mato()
        points.set_score()
    
    # Detect collision with playfield boundaries
    if mato.head.xcor() > 380 or mato.head.xcor() < -390 or mato.head.ycor() > 290 or mato.head.ycor() < -280:
        mato.teleport_mato()

screen.exitonclick()
