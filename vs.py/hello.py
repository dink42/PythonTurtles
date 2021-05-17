import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLOR = ['red', 'pink', 'orange', 'brown', 'green', 'blue']


def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of turtles (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric.. Try again: ')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number in range not in range (2 - 10): ')

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT //2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape('turtle')
        racer.left(90)
        racer.pendown()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.penup()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Dans Turtles')

racers = get_number_of_racers()
init_turtle()

create_turtles(colors=COLOR)
random.shuffle(COLOR)
color = COLOR[:racers]

winner = race(COLOR)
print(f'Turtle {winner} is the winner')
time.sleep(10)