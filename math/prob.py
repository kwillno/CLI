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

def negbinomialFunc(x,k,p):
	if x<k:
		return False

	nb = nCrFunc(x-1,k-1)*(p**k)*((1-p)**(x-k))
	return nb

def hyperGeometricFunc(x,N,n,k):
	h = (nCrFunc(k,x) * nCrFunc(N-k,n-x))/(nCrFunc(N,n))
	return h

def poissonFunc(x,l):
	p = (((l)**(x))/(factorial(x)))*((np.e)**(-l))
	return p


@click.command()


# Input of variables
@click.option("--population","-N","N",type=int, help="The total population of the experiment.")
@click.option("--samples","-n","n",type=int, help="The total samples or experiments taken.")
@click.option("--sucess","-k","k",type=int, help="Amount of objects that give sucess in Hypergeometric model.")
@click.option("--r","-r","r",type=int, help="Helping number used in nPr and nCr.")
@click.option("--choice","-x","x",type=int, help="Choice of x in hypergeometric and binomial models.")
@click.option("--probability","-p","p",type=float, help="Probability used in binomial model.")
@click.option("--lambda","-l","l",type=float, help="Lambda for poisson distribution.")


# Input of commandflags

@click.option("--nCr","-C","nCr",count=True,default=False,help="n choose r, required arguments -n -r")
@click.option("--nPr","-P","nPr",count=True,default=False,help="n permutation r, required arguments -n -r")
@click.option("--binomial","-b","binomial",count=True,default=False,help="Binomial distribution, required arguments -x -k -p")
@click.option("--negativebinomial","-nb","negbin",count=True,default=False,help="Negative binomial distribution, required arguments -x -k -p")
@click.option("--hypergeometric","-hg","hypGeo",count=True,default=False,help="Hypergeometric distribution, required arguments -x -N -n -k")
@click.option("--poisson","-pois","poisson",count=True,default=False,help="Poisson distribution, required arguments -x -l")


def process(N,n,k,r,x,p,l,nCr,nPr,binomial,negbin,hypGeo,poisson):
	"""
	Calculates probabilities of distrubutions given parameters.
	Can also calculate nPr and nCr
	"""
	if nCr:
		print(nCrFunc(n,r))
	if nPr:
		print(nPrFunc(n,r))
	if binomial:
		print(binomialFunc(x,n,p))
	if negbin:
		print(negbinomialFunc(x,k,p))
	if hypGeo:
		print(hyperGeometricFunc(x,N,n,k))
	if poisson:
		print(poissonFunc(x,l))


if __name__=="__main__":
	process()