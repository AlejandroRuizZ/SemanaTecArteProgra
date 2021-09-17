"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?- Ya
2. How can you make the snake go around the edges?- ya
3. How would you move the food? Ya
4. Change the snake to respond to mouse clicks. -ya

"""
from random import choice
from random import randrange
from turtle import clear, update, ontimer, setup, hideturtle, listen, tracer
from turtle import onkey, done
from freegames import square, vector
from playsound import playsound
from threading import Thread


#Función para abrir un archivo de música
def music_func():
    playsound('snakeMusic.mid')


#Definir función que llama audio
music = Thread(target = music_func)
music.daemon = True

#Iniciar música
music.start()

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

col = [ 'yellow', 'green', 'blue','black', 'orange', 'pink',"purple"]
sc= choice(col)
fc= choice (col)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -199 < head.x < 189 and -199 < head.y < 189
    
    
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if  head in snake:        
        square(head.x, head.y, 9, 'red')
        update()
        return

    elif not inside(head):
        if head.y>189 or head.y<-199:
            head.y=(head.y*-1)-10
        elif head.x>189 or head.x<-199:
            head.x=(head.x*-1)-10
        

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, sc)

    square(food.x, food.y, 9, fc)
    update()
    ontimer(move, 100) #CHANGE THIS VARIABLE TO ALTER SPEED OF SNAKE!!
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
onkey(lambda: aim.rotate(90),"space")
move()
done()