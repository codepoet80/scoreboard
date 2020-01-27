#7-segment LED control by Caleb D, December 2019
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define LED output segments
#	TODO: The pins should be passed in from the main program as a constructor argument or property
p1NumSegPins = [17,5,19,27,22,13,6]    #aka red team
p2NumSegPins = [18,25,26,24,23,16,12]   #aka blue team
# Number shape arrays (each led number is an array within the number shape array
# the led number array (the inner array) will align with the NumSegPin array positions
# so we know which pin to set to the corresponding value in the inner array.
numShapeValues = []
numShapeValues.append([0,1,0,0,0,0,0]) #0
numShapeValues.append([1,1,1,0,1,0,1]) #1
numShapeValues.append([0,0,0,0,1,1,0]) #2
numShapeValues.append([0,0,0,0,1,0,1]) #3
numShapeValues.append([1,0,1,0,0,0,1]) #4
numShapeValues.append([0,0,0,1,0,0,1]) #5
numShapeValues.append([0,0,0,1,0,0,0]) #6
numShapeValues.append([0,1,1,0,1,0,1]) #7
numShapeValues.append([0,0,0,0,0,0,0]) #8
numShapeValues.append([0,1,0,0,0,0,0]) #9

#init our pins based on variables and arrays above
for numSegPin in p1NumSegPins:
	GPIO.setup(numSegPin, GPIO.OUT)
for numSegPin in p2NumSegPins:
	GPIO.setup(numSegPin, GPIO.OUT)

# This function looks up the led segment array for the given player and number, and which pin to set
# Then calls the GPIO function to actually set the value.
def outputscore(player, number):
    posCount = 0
    pinArrayToUse = []
    if (player == "red" or player == "1"):
        # Uncomment the line below for debugging
        #print ("debug: updating player 1 score to " + str(number) + ":")
        pinArrayToUse = p1NumSegPins
    elif (player == "blue" or player == "2"):
        # Uncomment the line below for debugging
        #print ("debug: updating player 2 score to " + str(number) + ":")
        pinArrayToUse = p2NumSegPins
    for numSegPin in pinArrayToUse:
        segValues = numShapeValues[number]
        currSegValue = segValues[posCount]
        # Uncomment the line below for debugging
        #print ("debug: GPIO.output(" + str(numSegPin) + ", " + str(currSegValue) + ")")
        GPIO.output(numSegPin, currSegValue)
        posCount = posCount + 1
    return