import random
import turtle

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle")
FONT = ('Arial' , 30 , 'normal')
score = 0
game_over = False

#score turtle
turtle_list = []

score_turtle = turtle.Turtle()

countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setpos(0,y)
    score_turtle.write(arg="score:0",move=False,align ="center", font=FONT)




def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="score: {}".format(score), move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)

x_coordinates = [-20, -10, 0, 10, 20]
y_cordinates = [20, 10, 0, -10]
grid_size = 10

def setup_turtles():
    for x in x_coordinates:
        for y in y_cordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
       hide_turtles()
       random.choice(turtle_list).showturtle()
       screen.ontimer(show_turtles_randomly,500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setpos(0, y - 30)
    countdown_turtle.clear()
    if time >0:
       countdown_turtle.clear()
       countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
       screen.ontimer(lambda :countdown(time-1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)


def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    turtle.tracer(1)
    show_turtles_randomly()
    countdown(10)

start_game_up()
turtle.mainloop()

