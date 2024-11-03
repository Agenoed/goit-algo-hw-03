import turtle
import math

def koch_curve(t, length, level):
    
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def snowflake(t, length, level):
 
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

# ВВід рівеня рекурсії від користувача
level = int(input("Введіть рівень рекурсії: "))

t = turtle.Turtle()
t.speed(0)  
t.color("red") 
t.penup()
t.goto(-100, 50) 
t.pendown()

snowflake(t, 200, level)

turtle.done()