#!/bin/sh
echo Welcome to mail-program\n

echo What is the subject?
read SUB
echo Subject is: $SUB

echo Enter recepient adress:
read REC
echo Recepient is: $REC

echo Enter message to send:
read MSG
echo Message is: $MSG

echo $MSG | sudo ssmtp -vvv $REC
