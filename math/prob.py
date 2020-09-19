import click
import numpy as np
from math import factorial

# Functions
def nCr(n,r):
	C = (factorial(n))/(factorial(r)*factorial(n-r))
	return C

def nPr(n,r):
	P = (factorial(n))/(factorial(n-r))
	return P

def binomial(x,n,p):
	if x > n or x < 0:
		return False

	b = nCr(n,x)*(p**x)*((1-p)**(n-x))
	return b

def hyperGeometric(x,N,n,k):
	h = (nCr(k,x) * nCr(N-k,n-x))/(nCr(N,n))
	return h


@click.command()


# Input of variables
@click.option("--population","-N","N",type=int, help="The total population of the experiment.")
@click.option("--samples","-n","n",type=int, help="The total samples or experiments taken.")
@click.option("--sucess","-k","k",type=int, help="Amount of objects that give sucess in Hypergeometric model.")
@click.option("--r","-r","r",type=int, help="Helping number used in nPr and nCr.")
@click.option("--choice","-x","x",type=int, help="Choice of x in hypergeometric and binomial models.")
@click.option("--probability","-p","p",type=float, help="Probability used in binomial model.")

# Input of commandflags

@click.option("--nCr","-C","nCr",count=True,default=False)
@click.option("--nPr","-P","nPr",count=True,default=False)
@click.option("--binomial","-b","binomial",count=True,default=False)
@click.option("--hypergeometric","-hg","hypGeo",count=True,default=False)


def process():



if __name__=="__main__":
	process()