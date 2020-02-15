#Simple GPIO Tester, by Jon Wise 12/15/2019
import re, sys, os
from gpiozero import LED
from gpiozero import Button
from time import sleep
#set some variables
b1pin = 2
b2pin = 5
ledpin = 22
delay = 0.5
#ask the system to show GPIO Pinouts
print ("Testing GPIO Pinouts . . .")
os.system("pinout")
#init some pins
button1 = Button(b1pin)
button2 = Button(b2pin)
led = LED(ledpin)
#loop testing the led and button
while True:
	#toggle led
	led.on()
	print ("\033[1;32;40m LED at GPIO " + str(ledpin) + " on                   ", end="\r")
	sleep(delay)
	led.off()
	print ("\033[1;31;40m LED at GPIO " + str(ledpin) + " off                  ", end="\r")
	sleep(delay)
	#check if button1 is pressed
	if button1.is_pressed:
		print ("\033[0;37;42m Button at GPIO " + str(b1pin) + " is pressed      ", end="\r")
	else:
		print ("\033[0;37;41m Button at GPIO " + str(b1pin) + " is not pressed  ", end="\r")
	sleep(delay)
	#check if button2 is pressed
	if button2.is_pressed:
		print ("\033[0;37;42m Button at GPIO " + str(b2pin) + " is pressed      ", end="\r")
	else:
		print ("\033[0;37;41m Button at GPIO " + str(b2pin) + " is not pressed  ", end="\r")
	#cleanup and prepare for next pass through loop
	print ("\033[1;30;40m", end="\r")
	#sys.stdout.write("\x1b[A")
	sleep(delay)
