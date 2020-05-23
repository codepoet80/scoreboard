#Simple Score Board, by Jon W, Caleb D and Ben W 1/3/2020
import os
import buzzertones
import drawscore
from gpiozero import Button
from time import sleep
from signal import pause

#init our gpio pins and variables
Songs = buzzertones.songs(26)
resetPin = 21
player1pin = 12
player1points = 0
player2pin = 16
player2points = 0
button1 = Button(player1pin)
button2 = Button(player2pin)
buttonReset = Button(resetPin)
doingScore = False

#respond to goals
def player1_scored(button):
	global doingScore
	global player1points
	#make sure we don't count the score while we're in the middle of counting the score
	if (doingScore != True):
		doingScore = True
		Songs.play_song("justbuzz1")
		player1points = player1points + 1
		update_scoreboard()
		sleep(1)
		doingScore = False

def player2_scored(button):
	global doingScore
	global player2points
	#make sure we don't count the score while we're in the middle of counting the score
	if (doingScore != True):
		doingScore = True
		Songs.play_song("justbuzz2")
		player2points = player2points + 1
		update_scoreboard()
		sleep(1)
		doingScore = False

#show latest scores on scoreboard
def update_scoreboard():
    global player1points
    global player2points
    if (player2points > 9) or (player1points > 9):
        drawscore.clear()
        drawscore.score(player1points, player2points)
        game_over()
    elif (player1points >= 10) or (player2points >= 10):
        reset_game()
    else:
        drawscore.clear()
        drawscore.score(player1points, player2points)

#do cool game over stuff
def game_over():
    global player1points
    global player2points
    if (player1points > player2points):
        Songs.play_song("abisong")
    else:
        Songs.play_song("elisong")
    sleep(2)
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
    print ("\033[0;37;44mScoreboard version 0.5 (Press Enter to exit):\033[1;36;40m")
    Songs.play_song("ballgame")
    update_scoreboard()

#main app code (no loop needed, since we're event driven)
reset_game()
#wait for input
button1.when_pressed = player1_scored
button2.when_pressed = player2_scored
buttonReset.when_pressed = reset_game
pause() #wait for enter key to exit program. to wait forever, use pause() instead
