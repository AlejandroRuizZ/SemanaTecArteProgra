"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?- Ya
2. How can you make the snake go around the edges?- 
3. How would you move the food? Ya
4. Change the snake to respond to mouse clicks. -ya

"""
from random import choice
from random import random
from random import randrange
from turtle import *
from freegames import square, vector
from playsound import playsound
from threading import Thread


#Función para abrir un archivo de música
def music_func():
    playsound('musicSnake2.mid')


#Definir función que llama audio
music = Thread(target = music_func)
music.daemon = True

#Iniciar música
music.start()

food = vector(0, 0)
snake = [vector(10, 0)]
snake2= [vector(-10, 0)]
aim = vector(0, -10)
aim2= vector(0, -10)
col = [ 'yellow', 'green', 'blue','black', 'orange', 'pink',"purple"]

fc= choice (col)
if fc=="blue":
    fc= choice(col)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def change2(x,y):
    "Change snake2 direction."
    aim2.x = x
    aim2.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -199 < head.x < 189 and -199 < head.y < 189

    
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    head2 = snake2[-1].copy()
    head2.move(aim2)

    if  head in snake:
        square(head.x, head.y, 9, 'red')
        print("Player 2 wins!")
        update()
        return

    if  head2 in snake2:
        square(head2.x, head2.y, 9, 'red')
        print("Player 1 wins!")
        update()
        return

    elif not inside(head):
        if head.y>189 or head.y<-199:
            head.y=(head.y*-1)-10

        elif head.x>189 or head.x<-199:
            head.x=(head.x*-1)-10
    
    elif not inside(head2):
        if head2.y>189 or head2.y<-199:
            head2.y=(head2.y*-1)-10

        elif head2.x>189 or head2.x<-199:
            head2.x=(head2.x*-1)-10

    snake.append(head)
    snake2.append(head2)
    
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    if head2 == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake2.pop(0)
    
    clear()

    for body in snake:
        square(body.x, body.y, 9, "green")

    square(food.x, food.y, 9, fc)

    for body2 in snake2:
        square(body2.x, body2.y, 9, "blue")

    if  head in snake2:
        square(head.x, head.y, 9, 'red')
        print('Player blue wins!')
        return

    elif head2 in snake:
       square(head2.x, head2.y, 9, 'red')
       print('Player red wins!')
       return

    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
tracer(False)
listen()
onkey(lambda: aim.rotate(90), 'Right')
onkey(lambda: aim.rotate(-90), 'Left')
onkey(lambda: aim2.rotate(-90), 'a')
onkey(lambda: aim2.rotate(90), "d")
move()
done()