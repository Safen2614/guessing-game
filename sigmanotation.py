import sympy as sp
from sympy import symbols, simplify, pretty_print, sympify
# create sigma notation for th user to compuete a sum under a graph 

# take a users bounds for example x=1 to x=3 so we know when to stop 
# ask for right end point or left end point 
# ask for what graph or ask f(x)=?
GETBACKTOWORK= True

while GETBACKTOWORK:
    a =int(input("what should the left bound be?"))
    b= int(input('what should the right bound be?'))
    n= int(input('how many subintervals? (rectangles)'))
    method=input('which endpoint do you want to calculate? (say left or right)')
    if a==b:
        print("intergral is 0")
    elif n==0:
        print("can't be zero dude")
    elif method != "left" and method != "right":
        print("say left or right man")
    else:
        GETBACKTOWORK= False

graph = input('"Enter f(x), use ^ or **: "')
expr_str = graph.replace('^', '**')
deltax= (b-a)/n

  

x = symbols('x')
f = sympify(expr_str) 
sigmasum=0

for i in range(1,n+1):
        if method=="right":
            end=a + deltax*i
        else:
            end=a + deltax*(i-1)
        sigmasum+= f.subs(x, end)*deltax

print ("intergral is about ≈ " , sigmasum)



    

# use .subs(var, number)
# .subs([a, left endpoint], [b, right endpoint])
# .subs({a: 2, b: 3})
# if the user chooses teh right point then we must make 4 rectangles skipping the first point 