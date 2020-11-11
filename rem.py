from json import loads,dumps
from os import system
import click

def read():
	with open("CLI/rmv/rmview.json","r") as f:
		data = f.read()
		f.close()

	param = loads(data)

	return param

def send(param):
	data = dumps(param, indent=4)

	with open("CLI/rmv/rmview.json","w") as f:
		f.write(data)
		f.close()

@click.command()

@click.option("--address","-l","adr",default="10.11.99.1",type=str,help="Address to Remarkable")
@click.option("--orientation","-o","rot",default="auto",type=str,help="Starting orientation, auto, portrait, landscape")

def process(adr,rot):
	param = read()
	if adr != "10.11.99.1":
		param["ssh"]["address"] = adr
	if rot != "auto":
		param["orientation"] = rot
	send(param)

	system("rmview ~/CLI/rmv/rmview.json")

if __name__ == "__main__":
	process()