#!/usr/bin/python3

'''
function draw_shape.
impress plebs using turtle, colosys and a little maths.
they'll think you are a god (you are, technically)
@params: none
return: none
'''

from turtle import *
import colorsys as cs

def draw_shape():
    """ function draw_shape """
    bgcolor('black')
    h = .5
    tracer(100)
    up()
    goto(-290, 0)
    down()
    w=5

    for i in range(200):
        c = cs.hsv_to_rgb(h, 1, 1)
        color(c)
        h += .005
        for o in range(5):
            fd(130)
            lt(5)
        lt(65)
        circle(330)
        lt(65)

if __name__ == '__main__':
    print(f'Drawing shape ...')
    draw_shape()
    print(f'Done.')
