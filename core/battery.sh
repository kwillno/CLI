#!/bin/sh
while true
do
	echo "--------------------"
	date +"%T"
	upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep "%" 
	sleep 300
done
