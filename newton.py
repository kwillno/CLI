import click
from numpy import *

def newton(f, df, x0, tol, max_iter):
	# Solve f(x)=0 by Newtons method
	# The output of each iteration is printed
	# Input:
	#   f, df:   The function f and its derivate f'.
	#   x0:  Initial values
	#   tol: The tolerance
	# Output:
	#   The root and the number of iterations
	x = x0
	print('k ={:3d}, x = {:18.15f}, f(x) = {:10.3e}'.format(0, x, f(x)))
	for k in range(max_iter):
		fx = f(x)
		if abs(fx) < tol:           # Accept the solution 
			break 
		x = x - fx/df(x)            # Newton-iteration
		print('k ={:3d}, x = {:18.15f}, f(x) = {:10.3e}'.format(k+1, x, f(x)))
	return x, k+1
"""
# INPUT
f = lambda x : 4*x**2 + 3*x - 1		# Function 
df = lambda x : 8*x**7+3		# Derivative of function
x0 = 0.5                  	# Starting value

x, nit = newton(f, df, x0)  # Apply Newton
print('\n\nResult:\nx={}, number of iterations={}'.format(x, nit))
"""

@click.command()

@click.option("--equation","-eq","equation",required=True,type=str,help="Equation to be used")
@click.option("--derivative", "-deq","derivative",required=True,type=str,help="Derivative of equation to be used")
@click.option("--startvalue","-x0","x0",required=True,type=float,help="Starting point for Newtons iteration method")
@click.option("--tolerance","-tol","tol",default=(1.e-20),help="Tolerance for accepting final answer")
@click.option("--iterations","-iter","iterations",default=30,help="Maximum number of iterations for function to try")


def process(equation,derivative,x0,tol,iterations):
	"""
	Processes input and output of Newtons iterative algorithm for a graphs intersection with zero.
	"""

	eq = lambda x : eval(equation)
	df = lambda x : eval(derivative)

	x,nit = newton(eq,df,x0,tol,iterations)
	print('\n\nResult:\nx={}, number of iterations={}'.format(x, nit))

	

if __name__=="__main__":
	process()