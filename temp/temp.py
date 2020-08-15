import time
from matplotlib import pyplot as plt
import csv
import click

def printTemp(humidity):

	temp, humd = 0,0

	with open("CLI/temp/templog.txt",newline="\n") as f:
		data = csv.reader(f,delimiter=",")
		for row in f:
			tm = int(row[0:10])
			temp = float(row[11:16])
			humd = float(row[17:22])
		f.close()

	print("Last log at: " + time.ctime(tm))
	print("Temperature: {:.1f} C".format(temp))
	if humidity:
		print("Humidity: {:.1f} %".format(humd))

def plotTemp(hours,humidity,tb,hb):
	timeArr = []
	tempArr = []
	humdArr = []

	selectedTime = (60**2)*hours
	tm  = int(time.time())

	with open("CLI/temp/templog.txt",newline="\n") as f:
		data = csv.reader(f,delimiter=",")
		for row in f:
			lastTime = int(row[0:10])
			if int(row[0:10]) >= (tm - selectedTime):
				timeArr.append(-(tm -int(row[0:10]))/60**2)
				tempArr.append(float(row[11:16]))
				humdArr.append(float(row[17:22]))
		f.close()

	newTimeArr = [timeArr[0]]
	newTempArr = [tempArr[0]]
	newHumdArr = [humdArr[0]]


	for i in range(1,len(timeArr)-1):
		newTimeArr.append(timeArr[i])
		newTempArr.append((tempArr[i-1]+tempArr[i]+tempArr[i+1])/3)
		newHumdArr.append((humdArr[i-1]+humdArr[i]+humdArr[i+1])/3)

	fig,ax1 = plt.subplots()

	ax1.set_xlabel("time (hour)")
	if not tb == (0.0,0.0):
		ax1.set_ylim(tb)
	ax1.plot(newTimeArr,newTempArr,"r-",label="Temperature")
	ax1.tick_params(axis="y", labelcolor="tab:red")
	ax1.legend(loc="upper left")

	if humidity:
		ax2 = ax1.twinx()

		if not hb == (0.0,0.0):
			ax2.set_ylim(hb)
		ax2.plot(newTimeArr,newHumdArr,"b-",label="Humidity")
		ax2.tick_params(axis="y", labelcolor="tab:blue")
		ax2.legend(loc="upper right")

	plt.title(str(int(selectedTime/(60**2))) + " hours before " + time.ctime(lastTime)[4:16] + time.ctime(lastTime)[19:])
	fig.tight_layout()
	plt.show()


@click.command()

@click.option("--plot","-p","plot",count=True,help="Plot temperature and humidity for selected timeframe")
@click.option("--time","-t","timeframe",default=12,help="Timeframe for plotting")
@click.option("--humidity","-h","humidity",count=True,help="Show humidity, both in plot and console output")
@click.option("--tempbound","-tb","tempbound",default=(0.0,0.0),help="Bounds for plotting temperature")
@click.option("--humbound","-hb","humbound",default=(0.0,0.0),help="Bounds for plotting humidity")
@click.option("--verbose","-v","verbose",count=True,help="Force full output")

def process(plot,timeframe,humidity,tempbound,humbound,verbose):
	if verbose:
		printTemp(True)

	if not humbound == (0.0,0.0):
		humidity = True

	if plot:
		plotTemp(timeframe,humidity,tempbound,humbound)

	if not plot and not verbose:
		printTemp(humidity)


if __name__=="__main__":
	process()