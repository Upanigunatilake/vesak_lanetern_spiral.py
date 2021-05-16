import turtle
turtle.bgcolor('black')
colors=['blue','yellow','red','white','orange']
turtle.speed(0)
for i in range(280):
    turtle.pencolor(colors[i%5])
    turtle.pensize(i/88 +1)
    turtle.forward(i)
    turtle.left(59)
turtle.done()


