import click
import numpy as np
from math import factorial

# Functions
def nCrFunc(n,r):
	C = (factorial(n))/(factorial(r)*factorial(n-r))
	return C

def nPrFunc(n,r):
	P = (factorial(n))/(factorial(n-r))
	return P

def binomialFunc(x,n,p):
	if x > n or x < 0:
		return False

	b = nCrFunc(n,x)*(p**x)*((1-p)**(n-x))
	return b

def hyperGeometricFunc(x,N,n,k):
	h = (nCrFunc(k,x) * nCrFunc(N-k,n-x))/(nCrFunc(N,n))
	return h


@click.command()


# Input of variables
@click.option("--population","-N","N",type=int, help="The total population of the experiment.")
@click.option("--samples","-n","n",type=int, help="The total samples or experiments taken.")
@click.option("--sucess","-k","k",type=int, help="Amount of objects that give sucess in Hypergeometric model.")
@click.option("--r","-r","r",type=int, help="Helping number used in nPr and nCr.")
@click.option("--choice","-x","x",type=int, help="Choice of x in hypergeometric and binomial models.")
@click.option("--probability","-p","p",type=float, help="Probability used in binomial model.\n\n")

# Input of commandflags

@click.option("--nCr","-C","nCr",count=True,default=False,help="n choose r, required arguments -n -r")
@click.option("--nPr","-P","nPr",count=True,default=False,help="n permutation r, required arguments -n -r")
@click.option("--binomial","-b","binomial",count=True,default=False,help="Binomial distribution, required arguments -x -n -p")
@click.option("--hypergeometric","-hg","hypGeo",count=True,default=False,help="Hypergeometric distribution, required arguments -x -N -n -k")


def process(N,n,k,r,x,p,nCr,nPr,binomial,hypGeo):
	if nCr:
		print(nCrFunc(n,r))
	if nPr:
		print(nPrFunc(n,r))
	if binomial:
		print(binomialFunc(x,n,p))
	if hypGeo:
		print(hyperGeometricFunc(x,N,n,k))


if __name__=="__main__":
	process()