#!/usr/bin/env python3

import colorsys as cs
import turtle as t

t.bgcolor('black')
t.speed('fastest')
t.tracer(100)
t.pencolor('darkviolet')
h = .7
t.hideturtle()

def draw_shape():
    global h
    for i in range(4):
        global h
        for j in range(4):
            c = cs.hsv_to_rgb(h, 1, 1)
            h += .001
            t.fillcolor(c)
            t.begin_fill()
            t.fd(100)
            t.right(18)
            t.fd(100)
            t.lt(22)
            t.end_fill()


if __name__ == '__main__':
    print(f'Starting...')
    for k in range(400):
        draw_shape()
        t.goto(8, 8)
        t.rt(188)

    t.exitonclick()
    print(f'Done.')
