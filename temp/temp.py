import time
from matplotlib import pyplot as plt
import csv
import click

def printTemp(humidity):

	temp, humd = 0,0

	with open("CLI/temp/templog.txt",newline="\n") as f:
		data = csv.reader(f,delimiter=",")
		for row in f:
			temp = float(row[11:16])
			humd = float(row[17:22])
		f.close()

	print("Temperature: {:.1f} C".format(temp))
	if humidity:
		print("Humidity: {:.1f} %".format(humd))

def plotTemp(hours,humidity,tbu,tbl,hbu,hbl):
	timeArr = []
	tempArr = []
	humdArr = []

	selectedTime = (60**2)*hours
	tm  = int(time.time())

	with open("CLI/temp/templog.txt",newline="\n") as f:
		data = csv.reader(f,delimiter=",")
		for row in f:
			if int(row[0:10]) >= (tm - selectedTime):
				timeArr.append(-(tm -int(row[0:10]))/60**2)
				tempArr.append(float(row[11:16]))
				humdArr.append(float(row[17:22]))
		f.close()

	fig,ax1 = plt.subplots()

	ax1.set_xlabel("time (hour)")
	ax1.set_ylim([tbl,tbu])
	ax1.plot(timeArr,tempArr,"r-",label="Temperature")
	ax1.tick_params(axis="y", labelcolor="tab:red")
	ax1.legend(loc="upper left")

	if humidity:
		ax2 = ax1.twinx()

		ax2.set_ylim([hbl,hbu])
		ax2.plot(timeArr,humdArr,"b-",label="Humidity")
		ax2.tick_params(axis="y", labelcolor="tab:blue")
		ax2.legend(loc="upper right")

	plt.title("Last " + str(int(selectedTime/(60**2))) + " hours")
	fig.tight_layout()
	plt.show()


@click.command()

@click.option("--plot","-p","plot",count=True,help="Plot temperature and humidity for selected timeframe")
@click.option("--time","-t","timeframe",default=12,help="Timeframe for plotting")
@click.option("--humidity","-h","humidity",count=True,help="Show humidity, both in plot and console output.")
@click.option("--tempboundupper","-tbu","tbu",default=28,help="Upper bound for plotting temperature.")
@click.option("--tempboundlower","-tbl","tbl",default=21,help="Lower bound for plotting temperature.")
@click.option("--humdboundupper","-hbu","hbu",default=85,help="Upper bound for plotting humidity.")
@click.option("--humdboundlower","-hbl","hbl",default=25,help="Lower bound for plotting humidity.")
@click.option("--verbose","-v","verbose",count=True,help="Force full output")

def process(plot,timeframe,humidity,tbu,tbl,hbu,hbl,verbose):
	if verbose:
		printTemp(True)
	if plot:
		plotTemp(timeframe,humidity,tbu,tbl,hbu,hbl)

	if not plot and not verbose:
		printTemp(humidity)


if __name__=="__main__":
	process()