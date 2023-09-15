import player
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()


screen.listen()
screen.onkeypress(player.go_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    #Detect collissions with car
    for car in car_manager.all_cars:
        if car.distance(player) <25:
            game_is_on=False
            scoreboard.game_over()

    #Detect if player has reached other side
    if player.ycor()>280:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()












screen.exitonclick()