import turtle

# wn = turtle.Screen()
# wn.bgcolor("light green")
# wn.title("Turtle")
# skk = turtle.Turtle()

# skk.forward(100)
# turtle.done

# skk = turtle.Turtle()
# for i in range(4):
#     skk.forward(50)
#     skk.right(90)

# turtle.done()

wn = turtle.Screen() 
wn.bgcolor("light green") 
skk = turtle.Turtle() 
skk.color("blue") 

def sqrfunc(size): 
	for i in range(4): 
		skk.fd(size) 
		skk.left(90) 
		size = size + 5

sqrfunc(6) 
sqrfunc(26) 
sqrfunc(46) 
sqrfunc(66) 
sqrfunc(86) 
sqrfunc(106) 
sqrfunc(126) 
sqrfunc(146) 
