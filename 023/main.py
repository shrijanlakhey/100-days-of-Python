import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle road crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()


screen.onkeypress(fun=player.move_up, key="Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
        
    if player.is_at_finish_line():
        scoreboard.increase_level()
        car_manager.increase_speed()
        player.go_to_start()


screen.exitonclick()