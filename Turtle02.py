import turtle
turtle.Screen().bgcolor('blueviolet')

turtle.Screen().setup(500,600)
turtle.Screen().title('Star')

p = turtle.Turtle()
p.color('black')
p.pensize(5)
p.shape('turtle')


p.penup()
p.goto(-80, 70)
p.pendown()

for _ in range(5):
         p.forward(200)
         p.right(144)
    
turtle.done() 
