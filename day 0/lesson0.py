from turtle import *


#we want to paint a house
#step 1: draw a square
speed(5)

width(7)
color("green")
begin_fill()
forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door  

forward(70)
left(90)
color("purple")
begin_fill()
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("pink")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()       #painting right window (from our pov)
goto(190,60)
pendown()

color("blue")
begin_fill()
left(210)   
forward(80)
left(90)
forward(40)
left(90)
forward(80)
left(90)
forward(40)
end_fill()

penup()        #painting left window (from our pov)
goto(10,60)
pendown()

begin_fill()
forward(40)
left(90)
forward(80)
left(90)
forward(40)
left(90)
forward(80)
end_fill()

exitonclick()