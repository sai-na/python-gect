from turtle import Turtle 
t=Turtle() 

def star(t, length): 
  for count in range(5): 
    t.forward(length)
    t.right(144) 
star(t,100)