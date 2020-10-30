import os.path

startline = "# -- CLI aliases --\n"
endline = "# -- END CLI --\n"

path = "../.bash_aliases"

def checkfileexists(path):
	val = os.path.exists(path)
	return val

def write(path, lines):
	with open(path,"w") as f:
		for i in range(len(lines)):
			f.write(lines[i])

def findOld(path):
	with open(path,"r") as f:
		data = f.readlines()

	start = 0
	end = 0
	for i in range(len(data)):
		if data[i] == startline:
			start = i

		if data[i] == endline:
			end = i
			
	return start, end


def replace(start,end,path):
	with open(path,"r") as f:
		data = f.readlines()

	for i in range(len(data)):
		if (i >= start) and (i <= end):
			data.pop(start)

	lines = get()

	for i in range(len(lines)):
		data.append(lines[i])

	write(path, data)

def get():
	lines = []

	lines.append(startline)

	with open("aliases.txt","r") as f:
		data = f.readlines()

	for i in range(len(data)):
		lines.append(data[i])

	lines.append(endline)

	return lines


if checkfileexists(path):

	s, e = findOld(path)

	replace(s,e,path)

	print("setup.py completed")
else:

	print("setup.py failed")
	print("Please create file .bash_aliases in home directory.")