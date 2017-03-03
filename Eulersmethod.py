#Euler's Method
#   y' = f(x,y), y(x_0) = y_0
#
#   y_n+1 = y_n + h*f(x_n, y_n)
import math

def f(x,y):
	f = -2*x*y           #f = y'
	return f


def eulersmethod(x,y,xmax):
	i = 0                                #Iteration counter
	hinput = input("Enter step size: ")  #Get step size
	h = float(hinput)                    #Convert step size to a float

	while x <= xmax:                     #Begin loop
		y = y + h*f(x,y)                 #Euler iteration
		x = x + h                        #Increment x
		
		i = i + 1                        #Add 1 to iteration counter
		
		print("Iteration = ", i)
		print("x = ", x)
		print("y = ", y)
		
	print ("f(0.5) =", y)
		
eulersmethod(0.0,2.0,0.5)                #User Euler's method for x0=0, y0=2, and xmax=0.5
