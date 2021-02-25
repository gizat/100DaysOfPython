import random
import turtle as t

color_list = [(133, 165, 203), (220, 149, 106), (199, 135, 147), (33, 42, 60), (43, 104, 153), (237, 212, 92), (165, 58, 48), (141, 183, 163), (151, 58, 65), (215, 81, 70), (51, 111, 90), (236, 163, 154), (168, 30, 34), (34, 61, 55), (18, 97, 70), (228, 164, 170), (157, 33, 31), (55, 46, 50), (171, 186, 220), (57, 54, 50), (33, 59, 108), (188, 101, 110), (108, 126, 157), (176, 199, 189), (34, 150, 209), (64, 65, 59)]

screen = t.Screen()
screen.colormode(255)
screen.screensize(600, 600)

timmy = t.Turtle()
timmy.hideturtle()
timmy.shape('turtle')
timmy.color('aquamarine4')
timmy.speed(0)

timmy.penup()
timmy.setheading(225)
timmy.forward(350)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen.exitonclick()


# User colorgram to grab RGB values of colors in Hirst's painting.
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)