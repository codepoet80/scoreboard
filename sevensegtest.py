#Seven Segment LED Tester
import sevensegmentled
from time import sleep

numVal = 0
while True:
	sevensegmentled.outputscore("1", numVal)
	sevensegmentled.outputscore("2", numVal)
	numVal = numVal + 1
	if (numVal > 9):
		numVal = 0
	sleep(2)