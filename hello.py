import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'pink', 'orange', 'brown', 'green', 'blue']

def get_number_of_racers():
    """
    Prompt the user to input the number of turtles for the race.
    The number must be between 2 and 5.
    """
    while True:
        racers = input('Enter the number of turtles (2 - 5): ')
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 5:
                return racers
            else:
                print('Number not in range (2 - 5). Try again.')
        else:
            print('Input is not numeric. Try again.')

def create_turtles(colors):
    """
    Create turtle racers with the specified colors and position them at the starting line.
    """
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape('turtle')
        racer.left(90)
        racer.turtlesize(2)
        racer.penup()
        racer.color(color)
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        turtles.append(racer)
    return turtles

def race(turtles):
    """
    Conduct the race by moving each turtle forward a random distance until one reaches the finish line.
    """
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            _, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return racer.color()[0]

def init_turtle():
    """
    Initialize the turtle graphics window.
    """
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Dan\'s Turtle Race')

def main():
    """
    Main function to run the turtle race.
    """
    racers = get_number_of_racers()
    init_turtle()

    random.shuffle(COLORS)
    colors = COLORS[:racers]

    turtles = create_turtles(colors)
    winner = race(turtles)
    print(f'Turtle {winner} is the winner')

    time.sleep(8)

if __name__ == '__main__':
    main()
