import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard_Turtle_crossing import Scoreboard

# TODO create a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# TODO create the player
player = Player()
# TODO listen for instructions
screen.listen()
screen.onkeypress(player.move_forward, "Up")
screen.onkeypress(player.move_backward, "Down")
carmanager = CarManager()
# TODO create scoreboard
scoreboard = Scoreboard()
scoreboard.update_score()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # TODO create and move the cars
    carmanager.create_car()
    carmanager.move_forward()
    #TODO detect collision with the cars
    for car in  carmanager.allcars:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False
    #TODO detect the cross
    if player.is_at_finish_line():
        player.goto(0,-280)
        screen.update()
        scoreboard.level_up()
        scoreboard.update_score()
        carmanager.level_up()

screen.exitonclick()