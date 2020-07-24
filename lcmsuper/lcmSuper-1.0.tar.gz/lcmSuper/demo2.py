import turtle

t=turtle.Pen()
t.speed(10)
for x in range(18):
    t.penup()
    t.goto(-170+20*x,170)
    t.pendown()
    t.goto(-170+20*x,-170)

for y in range(18):
    t.penup()
    t.goto(170 ,-170+20*y)
    t.pendown()
    t.goto(-170, -170+20*y)

turtle.done()

x1=[(-400,400),(-300,200)]
y=(x1[0][0],x1[0][1])
print(y)
