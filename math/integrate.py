import click
import time as tim
import numpy as np
from matplotlib import pyplot as plt

def MonteCarlo(f,a,b,N,v,p):

	x = np.linspace(a,b)
	val = f(x)

	minval,maxval = np.min(val),np.max(val)

	if minval > 0:
		minval = 0
	if maxval < 0:
		maxval = 0

	pointsX = np.random.uniform(a,b,N)
	pointsY = np.random.uniform(minval,maxval,N)

	numpos = np.where((pointsY <= f(pointsX)) & (pointsY >= 0), True, False)
	numneg = np.where((pointsY >= f(pointsX)) & (pointsY < 0), True, False)
	
	under = sum(numpos) - sum(numneg)

	I = (under/N)*((b-a)*(maxval-minval))

	if v or p:
		print("Total: " + str(N) + "   Under: " + str(under))
	print("MonteCarlo result: " + f"{I:.5f}")

	if p:
		plt.figure(0)
		plt.plot(x,val)
		plt.plot(pointsX,pointsY,"r.")
		for i in range(len(pointsX)):
			if (pointsY[i] <= f(pointsX[i])) & (pointsY[i] >= 0) or (pointsY[i] >= f(pointsX[i])) & (pointsY[i] < 0):
				plt.plot(pointsX[i],pointsY[i],"b.")
		plt.show()

	return I

def trapz(func,a,b,v=False,N=1):
	if N == 1:
		return (b-a)*(func(a)+func(b))/2
	else:
		dx = (b-a)/N
		total = 0
		for i in range(1,N):
			total += (func(a+((i-1)*dx)) + func(a+(i*dx)))

		I = dx*total/2

		if v:
			print(f"Trapezoid result: {I:.5f}")

		return I



def adapQuadRec(func,a0,b0,a,b,tol):
    
    c = (a + b)/2
    
    Sab = trapz(func,a,b)
    Sac = trapz(func,a,c)
    Scb = trapz(func,c,b)
     
    if np.abs(Sab - Sac - Scb) < 3 * tol * (b-a)/(b0-a0):
        return trapz(func,a,c) + trapz(func,c,b)

    else:
        return (adapQuadRec(func,a0,b0,a,c,tol) + adapQuadRec(func,a0,b0,c,b,tol))



@click.command()

@click.option("--method","-m","method",type=str,default="AQ",help="Method to be used (AQ/trapz/MC)")
@click.option("--function","-f","func",required=True,type=str,help="Equation to be used")
@click.option("--lower","-a","lower",required=True,type=str,help="Lower bound")
@click.option("--upper","-b","upper",required=True,type=str,help="Upper bound")
@click.option("--number","-N","density",type=str,default="1e4",help="Number N")
@click.option("--tolerance","-tol","tolerance",type=str,default="1e-5",help="Tolerance to accept answer")
@click.option("--verbose","-v","verbose",count=True,default=False,help="Outputs all processes, not only final answer")
@click.option("--plot","-p","plot",count=True,default=False,help="Plots graph of integration")
@click.option("--time","-t","time",count=True,default=False,help="Prints time used for function to complete, do not use with -p")


def process(method,func,lower,upper,density,tolerance,verbose,plot,time):
	"""
	Approximates integral with given method.

	Methods include: 
	AQ 		: Adaptive Quadrature(default)
	trap 	: Trapezoidal approximation
	MC 		: MonteCarlo approximation

	"""
	if time:
		startTime = tim.time()

	
	f = lambda x : eval(func)
	lower,upper = float(eval(lower)),float(eval(upper))
	density = int(eval(density))
	tol = float(eval(tolerance))

	# ------------------------------------------------------------
	# Code for each method follows:

	if method == "MC":
		if plot and (density > 1e4):
			density = int(1e4)

		MonteCarlo(f,lower,upper,density,verbose,plot)

	elif method == "trapz":
		v = True

		trapz(f,lower,upper,v,density)

	elif method == "AQ":
		
		I = adapQuadRec(f,lower,upper,lower,upper,tol)
		print(f"Adaptive Quadrature result: {I:.5f}")

	if time:
		t = (tim.time()-startTime)
		print("Time used: " + f"{t:.4f}" + "s")

if __name__=="__main__":
	process()