import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(player.move, 'Up')


game_is_on = True
count = 0
while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.update()

    if count % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 290:
        scoreboard.level_up()
        player.reset()
        car_manager.increase_speed()

    for _ in range(len(car_manager.cars)):
        if car_manager.cars[_].distance(player) <= 27:
            scoreboard.game_over()
            game_is_on = False




screen.exitonclick()