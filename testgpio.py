#Simple GPIO Tester, by Jon Wise 12/15/2019
import re, sys, os
from gpiozero import LED
from gpiozero import Button
from time import sleep
#ask the system to show GPIO Pinouts
print ("Testing GPIO Pinouts . . .")
os.system("pinout")
#init some pins
button1 = Button(2)
button2 = Button(3)
led = LED(17)
#loop testing the led and button
while True:
	#toggle led
	led.on()
	print ("\033[1;32;40m LED at GPIO 17 on                   ", end="\r")
	sleep(1)
	led.off()
	print ("\033[1;31;40m LED at GPIO 17 off                  ", end="\r")
	sleep(1)
	#check if button1 is pressed
	if button1.is_pressed:
		print ("\033[0;37;42m Button at GPIO 2 is pressed", end="\r")
	else:
		print ("\033[0;37;41m Button at GPIO 2 is not pressed", end="\r")
	sleep(1)
	#check if button2 is pressed
	if button2.is_pressed:
		print ("\033[0;37;42m Button at GPIO 3 is pressed", end="\r")
	else:
		print ("\033[0;37;41m Button at GPIO 3 is not pressed", end="\r")
	#cleanup and prepare for next pass through loop
	print ("\033[1;30;40m")
	sys.stdout.write("\x1b[A")
	sleep(1)
