import random
import turtle as t
print()
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(235, 239, 252), (40, 7, 178), (87, 248, 180), (219, 156, 111), (146, 6, 81), (239, 45, 119), (11, 211, 85), (12, 139, 60), (215, 115, 177), (111, 104, 234), (249, 249, 60), (55, 232, 70), (184, 179, 246), (210, 103, 11), (40, 35, 246), (159, 124, 235), (241, 45, 37), (29, 121, 144), (190, 41, 106), (138, 8, 5), (82, 247, 253), (21, 6, 101), (10, 209, 218), (94, 9, 57), (227, 166, 202), (213, 121, 28), (10, 110, 49)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
