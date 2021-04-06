from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
STARTING_POSITION = (330, random.randint(-250, 250))



class CarManager:
    def __init__(self):
        self.cars = []
        self.STARTING_MOVE_DISTANCE = 5


    def create_car(self):
        new_car = Turtle('square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        for car in self.cars:
            car.backward(self.STARTING_MOVE_DISTANCE)



