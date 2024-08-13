import turtle
import random
import time

WIDTH, HEIGHT = 600, 600
COLORS = ["red", "green", "blue" ,"cyan" , "pink", "orange" ,"yellow" ,"black"]


def get_number_of_racers():

    racers = 0

    while True:
        racers = input("How many turtles do you want in the race: ")

        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:             
                break

            else:
                print("Please input a number between 2 and 10")
                continue

        else:
            print("Please enter a number between 2-10")
            continue
    return racers

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle racing")

def colors(racers,colors):

    random.shuffle(colors)
    racing_turtle_colors = colors[:racers]

    return racing_turtle_colors

def creating_turtles(colors):

    turtle_objects = []
    spacingX = WIDTH // (len(colors) + 1)

    for i, turtle_color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(turtle_color)
        racer.shape("turtle")
        racer.penup()
        racer.left(90)
        racer.penup()
        #set position
        racer.setpos(-WIDTH //2  + (i+1)*spacingX, -HEIGHT//2 + 20) 
        racer.pendown()
        turtle_objects.append(racer)
    
    return turtle_objects

def race(turtle_objects):
    while True:
        
        for turtle in turtle_objects:

            turtle.forward(random.randrange(1, 21))
            x, y = turtle.pos()

            if y > HEIGHT // 2 - 20 :
                return turtle_objects.index(turtle)


        

    
racers = get_number_of_racers()
init_turtle()

turtle_colors = colors(racers,COLORS)
turtle_objects = creating_turtles(turtle_colors)
index_of_the_winner = race(turtle_objects)
winner = turtle_colors[index_of_the_winner]
print(winner)
time.sleep(8)