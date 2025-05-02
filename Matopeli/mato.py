from turtle import Turtle
from random import random, randint, choice

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLOR = ["white", "magenta", "purple"]

class Mato:
    def __init__(self):
        self.segments = []
        self.create_mato()
        self.head = self.segments[0] # self.create_mato() has to run before this line in order for the self.segments list to populate, so that one can refer to index at self.segments[0]

    def create_mato(self):
        for position in STARTING_POSITIONS:
            self.new_segment(position)

    def new_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        random_size_len = random()
        random_size_wid = random()
        new_segment.shapesize(stretch_len=random_size_len, stretch_wid=random_size_wid)
        new_segment.color(choice(COLOR))
        new_segment.goto(position)
        self.segments.append(new_segment)

    def grow_mato(self):
        self.new_segment(self.segments[-1].position())

    def move(self):
        # move mato starting from tail up to head
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def teleport_mato(self):
        # teleport mato to opposite end of playfield
        for seg_num in range(0, len(self.segments), 1):
            x = self.segments[seg_num].xcor()
            y = self.segments[seg_num].ycor()
        # mato went over the playfield along positive x-axis
        if x >= 400:
            self.head.teleport(x = x-800)
        # mato went over the playfield along positive y-axis
        if y >= 300:
            self.head.teleport(y = y-600)
        # mato went over the playfield along negative x-axis
        if x <= -400:
            self.head.teleport(x = x+800)
        # mato went over the playfield along negative y-axis
        if y <= -300:
            self.head.teleport(y = y+600)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
