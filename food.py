from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        """All the methods comes from Turtle class that we inherited"""
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh_food_location()

    def refresh_food_location(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 360)
        self.goto(random_x, random_y)
