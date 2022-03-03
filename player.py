from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_forward(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)
    def move_backward(self):
        self.speed("fastest")
        self.setheading(270)
        self.forward(MOVE_DISTANCE)
    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE:
            return True
        else:
            return False
