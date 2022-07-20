import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


i=0
screen.listen()
screen.onkey(key="Up", fun=player.move_up)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if i%6 == 0:
        car_manager.add_car()
    i += 1

    if player.ycor() == FINISH_LINE_Y:
        player.next_level()
        car_manager.next_level()
        scoreboard.increase_score()
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

    car_manager.move_car()

    for element in car_manager.car_park:
        if element.distance(player) < 20:
            game_is_on = False
            scoreboard.end_of_game()


screen.exitonclick()