from tkinter import *
import random

GAME_WIDTH=700
GAME_HEIGHT=700
SPEED=50
SPACE_SIZE=50
BODY_PARTS=3
SNAKE_COLOR='#00FF00'
FOOD_COLOR='#FF0000'
BACKGROUND_COLOR='#000000'


class Snake:
    def __init__(self):
        self.body_size=BODY_PARTS
        self.cordinates=[]
        self.squares=[]

        for i in range(0,BODY_PARTS):
            self.cordinates.append([0,0])


        for x, y in self.cordinates:
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag='snake')
            self.squares.append(square)





class Food:
    def __init__(self):
        x=random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y=random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE

        self.cordinates=[x,y]

        canvas.create_rectangle(x,y, x+ SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag='food')



def next_turn(snake, food):
    x,y=snake.cordinates[0]

    if direction=="up":
        y-=SPACE_SIZE


    elif direction=='down':
        y+=SPACE_SIZE



    elif direction=='left':
        x-=SPACE_SIZE

    
    elif direction=='right':
        x+=SPACE_SIZE


    snake.cordinates.insert(0,(x,y))

    square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)

    snake.squares.insert(0,square)

    del snake.cordinates[-1]

    canvas.delete(snake.squares[-1])

    window.after(SPEED, next_turn,snake, food)    

    del snake.squares[-1]
    

def check_collisions():
    pass

def game_over():
    pass

window=Tk()
window.title("snake game")
window.resizable(False,False)

score=0
direction='down'

label=Label(window,text=f'score: {score}',font=('consolas',40))
label.pack()


canvas=Canvas(window, bg=BACKGROUND_COLOR , height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


snake=Snake()
food=Food()


next_turn(snake,food)



window.mainloop()


#19.31