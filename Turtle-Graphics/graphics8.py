#A cool looking spikey figure

import tkinter
import turtle

from turtle import *
color('purple', 'Red')
begin_fill()
while True:
    forward(10)
    right(10)
    backward(10)
    forward(20)
    right(20)
    backward(20)
    forward(30)
    right(30)
    backward(30)
    forward(40)
    right(40)
    backward(40)
    forward(50)
    right(50)
    backward(50)
    forward(60)
    right(60)
    backward(60)
    forward(70)
    right(70)
    backward(70)
    forward(80)
    right(80)
    backward(80)
    forward(90)
    right(90)
    backward(90)
    forward(100)
    right(100)
    backward(100)
    speed(15)
    if abs(pos()) < 1:
        break
end_fill()
done()
