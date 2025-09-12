import turtle
import random
turtle.Screen().bgcolor('black')
turtle.Screen().setup(600, 600)
turtle.Screen().title('Rendom Pattern')


p = turtle.Turtle()
p.pensize(2)
size = 0


colors = ['red', 'pink', 'green', 'blue', 'orange', 'purple', 'yellow', 'Absolute Zero', 'Blue-Green', 'Bronze', 'Dark Red', 'Dark Orange', 'Dark green', 'Dark blue', ]


while True:
    p.color(random.choice(colors))
    for _ in range(5):
       p.forward(size + 1)
       p.left(90)
       size = size - 5
    size += 1