from random import randint
import os

with open(f"{os.getcwd()}/CLI/iroh/data.txt") as f:
	data = f.readlines()
	f.close()

r = randint(0,len(data)-1)
print(data[r].strip())
print("- Uncle Iroh")
