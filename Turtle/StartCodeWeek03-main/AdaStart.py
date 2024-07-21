import turtle 
turtle.colormode(255)


win = turtle.Screen()
w = 750 
h = 800 
win.setup(width=w, height=h) 



win.bgcolor("seashell4")
bgImg = "FullAda_Glam.gif"
stampImg = "JustAda_Glam.gif"
win.addshape(stampImg) 

win.bgpic(bgImg) 


#=======Add your code here======

#crescent moon
moon = turtle.Turtle()
moon.shape("arrow")
moon.goto(75,25)
moon.pensize(10)
moon.speed(10)
moon.pencolor(173, 245, 255)


moon.circle(200,200) 
moon.left(300)
moon.circle(300,-80)
moon.up()

sun = turtle.Turtle()
sun.down()
sun.pensize(7)
sun.goto(-200,200)
sun.speed(12)
sun.up()

# I learned how to do this in a youtube tutorial but made it my own code (did not just copy it in)
for i in range(6):
   
      
    for color in ('#FF9000', '#FF570A'):
        sun.color(color)
         
        
        sun.down()
        sun.circle(100)
         
        
        sun.right(50)
        sun.back(50)

star = turtle.Turtle()

for i in range(5):
 
        star.color('#C3C3E6')
        star.pensize(5)
        star.forward(100)
        star.down()
 
        star.right(144)
        star.begin_fill
        star.end_fill
        

for i in range(5):
 
      
        star.goto(-100,-100)
        star.down()
        star.color('#4ADBC8')
        star.pensize(5)
        star.forward(100)
        star.down()
 
        star.right(144)
        star.begin_fill
        star.end_fill
        star.up()
     



#sun
dot = turtle.Turtle()
dot.shape("turtle")
dot.goto(-200,-200)
dot.down()
dot.pencolor('#FF570A')
dot.fillcolor("orange")
dot.width(2)
dot.speed(10)
dot.begin_fill()
dot.circle(10)
dot.end_fill()






#filled in circle
moon.up()
moon.goto(0,-200)
moon.down()
moon.color(198, 65, 145) 
moon.begin_fill() 
moon.circle(10)
moon.end_fill()



#dot
moon.up()
moon.goto(100,200)
moon.down
moon.color(244, 96, 54)
moon.dot(75)
moon.up()
#i learned this from the help article posted in the assignment


star = turtle.Turtle()

for i in range(5):
 
        star.color('#F2E863')
        star.pensize(5)
        star.forward(300)
        star.down()
 
        star.right(144)
        star.begin_fill
        star.end_fill

moon = turtle.Turtle()
moon.up()
moon.goto(-100,-200)
moon.down
moon.color(173, 245, 255)
moon.dot(95)

moon.up()
moon.goto(190,-140)
moon.pensize(12)
moon.down()
moon.color('#DA627D')
moon.circle(100,150)
moon.up()




#=======Clean up code (do not change)======

moon.done()