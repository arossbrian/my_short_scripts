from turtle import *
penup()
goto(-140,140)
# for step in range(6):
#     write(step)
#     forward(20)
for step in range(10):
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)



#This ensures that the window stays up for as long as its not clicked
# You can also use exitonclick()
# done()
exitonclick()