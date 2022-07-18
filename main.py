from turtle import Turtle,Screen
import random


screen=Screen()
screen.setup(500,400)
bet=screen.textinput(title="Make your bet",prompt="Which turtle do you think will win? Choose a color: ")
colors=["red","yellow","green","blue","orange","pink"]
y=0
tim_list=[]
for i in range(0,6):
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-235,y)
    y+=30
    tim_list.append(tim)

if bet:
    game=True

while game:
    for tim in tim_list:
        tim.forward(random.randint(1,10))
        if tim.xcor()>=235:
            winner=tim.pencolor()
            game=False

if bet==winner:
     print(f"you won!The {winner} turtle is winner")
else:
     print(f"you lost!The {winner} turtle is winner")








screen.exitonclick()