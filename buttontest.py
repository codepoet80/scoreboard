import datetime
from gpiozero import Button

#init our gpio pins
b1pin = 2
b2pin = 5
button1 = Button(b1pin)
button2 = Button(b2pin)

def b1pressed():
	print(str(datetime.datetime.now().time()) + " - Button at GPIO " + str(b1pin) + " pressed")

def b2pressed():
	print(str(datetime.datetime.now().time()) + " - Button at GPIO " + str(b2pin) + " pressed")

#wait for input
button1.when_pressed = b1pressed
button2.when_pressed = b2pressed
input() #wait for enter key to exit program.
