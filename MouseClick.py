import simplegui
import math

WIDTH=450
HEIGHT=300
BALL_RADIUS=20
LINE_WIDTH=3
BALL_COLOR="red"
BALL_POS=[WIDTH/2,HEIGHT/2]
ball_list=[]

def distance(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)

def click(pos):
    global BALL_COLOR,BALL_POS
    change=False
    for ball in ball_list:
        if (distance((ball[0],ball[1]),pos)<BALL_RADIUS):
            change=True
            if (ball[2]=="red"):
                ball[2]="green"
            else:
                ball[2]="red"
    if (change==False):
        ball_list.append([pos[0],pos[1],"red"])

def draw_handler(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0],ball[1]],BALL_RADIUS,LINE_WIDTH,"black",ball[2])

frame=simplegui.create_frame("Mouse test",WIDTH,HEIGHT)
frame.set_mouseclick_handler(click)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handler)
frame.start()