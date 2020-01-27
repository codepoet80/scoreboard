#Simple Score Board, by Jon W, Caleb D and Ben W 1/3/2020
import os
import sevensegmentled
import buzzertones
from gpiozero import LED
from gpiozero import Button
from time import sleep
from signal import pause

#init our gpio pins
Songs = buzzertones.songs(21)
doingScore = False
player1pin = 2 #caleb uses 20
player1points = 0
player2pin = 3 #caleb uses 21
player2points = 0
button1 = Button(player1pin)
button2 = Button(player2pin)
player1led = LED(27)
player2led = LED(20)
    
#respond to goals
def player1_scored(button):
	global doingScore
	global player1points
	#make sure we don't count the score while we're in the middle of counting the score
	if (doingScore != True):
		doingScore = True
		Songs.play_song("abisong")
		player1points = player1points + 1
		player1led.blink(0.3, 0.3, 5)
		update_scoreboard()
		sleep(5)
		doingScore = False

def player2_scored(button):
	global doingScore
	global player2points
	#make sure we don't count the score while we're in the middle of counting the score
	if (doingScore != True):
		doingScore = True
		Songs.play_song("elisong")
		player2points = player2points + 1
		player2led.blink(0.3, 0.3, 5)
		update_scoreboard()
		sleep(5)
		doingScore = False

#show latest scores on scoreboard
def update_scoreboard():
    global player1points
    global player2points
    if (player1points == 9) or (player2points == 9):
        game_over()
    elif (player1points > 9) or (player2points > 9):
        reset_game()
    else:
        print ("Player 1: " + str(player1points) + ", Player 2: " + str(player2points), end="\r")
        sevensegmentled.outputscore("1", player1points)
        sevensegmentled.outputscore("2", player2points)

#do cool game over stuff
def game_over():
    print ("", end="\r\n")
    print("Game over!")
    print("Score again to start a new game...")
    return

#set or reset the game
def reset_game():
    global player1points
    global player2points
    global doingScore
    doingScore = False
    player1points = 0
    player2points = 0
    #setup the screen
    os.system("clear")
    print ("\033[0;37;44mScoreboard version 0.4 (Press Enter to exit):\033[1;36;40m")
    Songs.play_song("ballgame")
    update_scoreboard()

#main app code (no loop needed, since we're event driven)
reset_game()
#wait for input
button1.when_pressed = player1_scored
button2.when_pressed = player2_scored
input() #wait for enter key to exit program. to wait forever, use pause() instead