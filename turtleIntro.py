import turtle

turtle.shape("turtle")
#turtle.speed(0)

'''
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
'''
#Hexagonal Shape

for i in range(6):
    turtle.forward(100)
    turtle.left(60)

#Triangle
'''
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.backward(100)
turtle.left(60)
turtle.forward(100)
'''


turtle.exitonclick()