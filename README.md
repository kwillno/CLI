# Introduction

This is a repository for my own CLI(Command Line Interfaces). I am using the click python library for handling of arguments.  
The project is built for Linux, specifically using Bash on Linux Mint 19.3

# Setup

To start using this repo yourself, clone it into your home-directory and copy the contents of aliases.txt into your .bash_aliases file. 

# Usage

After adding aliases the commands can be used from any directory:

```
$ newton -eq 4*x**2 -3 -deq 8*x -x0 2
x=0.8660254037844387

$ newton -eq 4*x**2-3 -deq 8*x -x0 2 -v -tol 1.e-5
k =  0, x =  2.000000000000000, f(x) =  1.300e+01
k =  1, x =  1.187500000000000, f(x) =  2.641e+00
k =  2, x =  0.909539473684211, f(x) =  3.090e-01
k =  3, x =  0.867066301037404, f(x) =  7.216e-03
k =  4, x =  0.866026028573506, f(x) =  4.329e-06


Result:
x=0.8660260285735061, number of iterations=5
```

## Todo:

- Adding auto-scaling plots
- Restructure with Math-directory
- Add integrating functions (Simpson, RK)
- Add automatic setup-script (Setting up aliases)
