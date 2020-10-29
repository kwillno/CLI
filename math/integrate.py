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



@click.command()

@click.option("--method","-m","method",required=True,type=str,default="MC",help="Method to be used")
@click.option("--function","-f","func",required=True,type=str,help="Equation to be used")
@click.option("--lower","-a","lower",required=True,type=str,help="Lower bound")
@click.option("--upper","-b","upper",required=True,type=str,help="Upper bound")
@click.option("--number","-N","density",required=True,type=str,default="1e4",help="Number N")
@click.option("--verbose","-v","verbose",count=True,default=False,help="Outputs all processes, not only final answer")
@click.option("--plot","-p","plot",count=True,default=False,help="Plots graph of integration")
@click.option("--time","-t","time",count=True,default=False,help="Prints time used for function to complete, do not use with -p")


def process(method,func,lower,upper,density,verbose,plot,time):
	"""
	Processes input and output of Newtons iterative algorithm for a graphs intersection with zero.
	"""
	if time:
		startTime = tim.time()

	
	f = lambda x : eval(func)
	lower,upper = float(eval(lower)),float(eval(upper))

	if method == "MC":
		density = int(eval(density))

		if plot and (density > 1e4):
			density = int(1e4)

		MonteCarlo(f,lower,upper,density,verbose,plot)

	if time:
		t = (tim.time()-startTime)
		print("Time used: " + f"{t:.4f}" + "s")

if __name__=="__main__":
	process()