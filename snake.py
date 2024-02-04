from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Starting Segment for Snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        """We set the previous snake to out of area"""
        for seg in self.segments:
            seg.goto(1000, 100)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """To move the snake properly we need to replace the segment's position from last through the first"""
        for seg_num in range(len(self.segments) - 1, 0, -1):  # For Loop will loop from last index to first
            """We need to store the next step's coordinates starting from the second last index"""
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # We place the last segment with the one in front of it
        self.segments[0].forward(MOVE_DISTANCE)  # Lastly, we need to move the first segment one step forward so the rest segments does not collide

    """Controlling the head of the Snake"""
    def up(self):
        """If head is not moving DOWN snake can move UP"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """If head is not moving UP snake can move DOWN"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """If head is not moving RIGHT snake can move LEFT"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """If head is not moving LEFT snake can move RIGHT"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)