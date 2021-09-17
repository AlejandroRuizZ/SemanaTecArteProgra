"""Tron, classic arcade game.

Exercises

1. Make the tron players faster/slower. ya
2. Stop a tron player from running into itself. ya
3. Allow the tron player to go around the edge of the screen. -ya
4. How would you create a computer player?-

"""

from turtle import *
from freegames import square, vector
from playsound import playsound
from threading import Thread


#Función para abrir un archivo de música
def music_func():
    playsound('badGuy.mid')


#Definir función que llama audio
music = Thread(target = music_func)
music.daemon = True

#Iniciar música
music.start()

p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

def inside(head):
    "Return True if head inside screen."
    return -200 < head.x < 200 and -200 < head.y < 200


def draw():
    "Advance players and draw game."
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    if  p1head in p2body or p1head in p1body:
        print('Player blue wins!')
        return

    elif p2head in p1body or p2head in p2body:
        print('Player red wins!')
        return

    elif not inside(p1head):
        if p1xy.y>199 or p1xy.y<-199:
           p1xy.y=(p1xy.y*-1)

        elif p1xy.x>199 or p1xy.x<-199:
            p1xy.x=(p1xy.x*-1)

    elif not inside(p2head):
        if p2xy.y>199 or p2xy.y<-199:
            p2xy.y=(p2xy.y*-1)

        elif p2xy.x>199 or p2xy.x<-199:
            p2xy.x=(p2xy.x*-1)



    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 'd')
onkey(lambda: p2aim.rotate(90), 'j')
onkey(lambda: p2aim.rotate(-90), 'l')
draw()
done()
