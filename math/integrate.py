import click
import numpy as np

def MonteCarlo(f,a,b,N,v):

	res = N/(b-a)

	x = np.linspace(a,b,N)
	val = f(x)

	xlim = [a,b]
	ylim = [np.min(val),np.max(val)]

	points = np.random.rand(N,2)
	for i in range(len(points)):
		points[i][0] = points[i][0]*(xlim[1]-xlim[0]) + xlim[0]
		points[i][1] = points[i][1]*(ylim[1]-ylim[0]) + ylim[0]


	selpoints = []
	under = 0
	for i in range(N):
		if (points[i][1] >= 0) and (points[i][1] <= f(points[i][0])):
			under += 1
			selpoints.append(points[i])

		
		elif (points[i][1] < 0) and (points[i][1] >= f(points[i][0])):
			under -= 1
			selpoints.append(points[i])
		

	I = (under/N)*((xlim[1]-xlim[0])*(ylim[1]-ylim[0]))

	if v:
		print("Total: " + str(N) + "   Under: " + str(under))
	print("MonteCarlo result: " + f"{I:.5f}")

	if v:
		plt.figure(0)
		plt.plot(x,val)
		for i in range(len(points)):
			plt.plot(points[i][0],points[i][1],"r.")
		for i in range(len(selpoints)):
			plt.plot(selpoints[i][0],selpoints[i][1],"b.")
		plt.show()

	return I



@click.command()

@click.option("--function","-f","func",required=True,type=str,help="Equation to be used")
@click.option("--lower","-a","lower",required=True,type=float,help="Lower bound")
@click.option("--upper","-b","upper",required=True,type=float,help="Upper bound")
@click.option("--number","-N","density",required=True,type=int,help="Number N")
@click.option("--verbose","-v","verbose",count=True,default=False,help="Outputs all processes, not only final answer")


def process(func,lower,upper,density,verbose):
	"""
	Processes input and output of Newtons iterative algorithm for a graphs intersection with zero.
	"""
	f = lambda x : eval(func)

	MonteCarlo(f,lower,upper,density,verbose)

if __name__=="__main__":
	process()