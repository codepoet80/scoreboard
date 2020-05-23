import math
import sys

# Make the whole code 3.x.x compatible too...
if sys.version[0]=="3": raw_input=input

char="*"
x=20
y=19
p1_left = 15
p2_left = 42


# A Simple clear screen command for this DEMO...
def clear():
    for n in range(0, 64, 1): print("\r\n")

def score(one, two):
	if (one == 0):
		score_zero(1)
	elif (one == 1):
		score_one(1)
	elif (one == 2):
		score_two(1)
	elif (one == 3):
		score_three(1)
	elif (one == 4):
		score_four(1)
	elif (one == 5):
		score_five(1)
	elif (one == 6):
		score_six(1)
	elif (one == 7):
		score_seven(1)
	elif (one == 8):
		score_eight(1)
	elif (one == 9):
		score_nine(1)
	elif (one == 10):
		score_win(1)
		return
	
	if (two == 0):
		score_zero(2)
	elif (two == 1):
		score_one(2)
	elif (two == 2):
		score_two(2)
	elif (two == 3):
		score_three(2)
	elif (two == 4):
		score_four(2)
	elif (two == 5):
		score_five(2)
	elif (two == 6):
		score_six(2)
	elif (two == 7):
		score_seven(2)
	elif (two == 8):
		score_eight(2)
	elif (two == 9):
		score_nine(2)
	elif (two == 10):
		clear()
		score_win(2)
		return

# This function is just basic for this DEMO but shows the power of the ANSI _Esc_ codes...
def locate(user_string="$VER: Locate_Demo.py_Version_0.00.10_(C)2007-2012_B.Walker_G0LCU.", x=0, y=0):
	# Don't allow any user errors. Python's own error detection will check for
	# syntax and concatination, etc, etc, errors.
	x=int(x)
	y=int(y)
	if x>=255: x=255
	if y>=255: y=255
	if x<=0: x=0
	if y<=0: y=0
	HORIZ=str(x)
	VERT=str(y)
	# Plot the user_string at the starting at position HORIZ, VERT...
	print("\033["+VERT+";"+HORIZ+"f"+user_string)

def score_zero(player):
    if player == 1:
        left = p1_left
    else:
        left = p2_left
    locate("███", left-4, 10)
    locate("███", left-3, 10)
    locate("███", left-2, 10)
    locate("███", left-1, 10)
    locate("███", left, 10)
    locate("███", left+1, 10)
    locate("███", left+2, 10)
    locate("███", left+3, 10)
    locate("███", left+4, 10)
    locate("███", left-5, 11)
    locate("███", left+5, 11)
    locate("███", left-5, 12)
    locate("███", left+5, 12)
    locate("███", left-5, 13)
    locate("███", left+5, 13)
    locate("███", left-5, 14)
    locate("███", left+5, 14)
    locate("███", left-5, 15)
    locate("███", left+5, 15)
    locate("███", left-5, 16)
    locate("███", left+5, 16)
    locate("███", left-5, 17)
    locate("███", left+5, 17)
    locate("███", left-5, 18)
    locate("███", left+5, 18)
    locate("███", left-5, 19)
    locate("███", left+5, 19)
    locate("███", left-5, 20)
    locate("███", left+5, 20)
    locate("███", left-5, 21)
    locate("███", left+5, 21)
    locate("███", left-5, 22)
    locate("███", left+5, 22)
    locate("███", left-5, 23)
    locate("███", left+5, 23)
    locate("███", left-5, 24)
    locate("███", left+5, 24)
    locate("███", left-5, 25)
    locate("███", left+5, 25)
    locate("███", left-5, 26)
    locate("███", left+5, 26)
    locate("███", left-5, 27)
    locate("███", left+5, 27)
    locate("███", left-5, 28)
    locate("███", left+5, 28)
    locate("███", left-5, 29)
    locate("███", left+5, 29)
    locate("███", left-4, 30)
    locate("███", left-3, 30)
    locate("███", left-2, 30)
    locate("███", left-1, 30)
    locate("███", left, 30)
    locate("███", left+1, 30)
    locate("███", left+2, 30)
    locate("███", left+3, 30)
    locate("███", left+4, 30)

def score_one(player):
    if player == 1:
        left = p1_left
    else:
        left = p2_left
    locate("███", left, 10)
    locate("███", left, 11)
    locate("███", left-1, 11)
    locate("███", left, 12)
    locate("███", left-2, 12)
    locate("███", left, 13)
    locate("███", left-3, 13)
    locate("███", left, 14)
    locate("███", left, 15)
    locate("███", left, 16)
    locate("███", left, 17)
    locate("███", left, 18)
    locate("███", left, 19)
    locate("███", left, 20)
    locate("███", left, 21)
    locate("███", left, 22)
    locate("███", left, 23)
    locate("███", left, 24)
    locate("███", left, 25)
    locate("███", left, 26)
    locate("███", left, 27)
    locate("███", left, 28)
    locate("███", left, 29)
    locate("███", left-1, 29)
    locate("███", left+1, 29)
    locate("███", left, 30)
    locate("███", left-1, 30)
    locate("███", left-2, 30)
    locate("███", left-3, 30)
    locate("███", left+1, 30)
    locate("███", left+2, 30)
    locate("███", left+3, 30)
    
def score_two(player):
    if player == 1:
        left = p1_left
    else:
        left = p2_left
    locate("███", left-4, 10)
    locate("███", left-3, 10)
    locate("███", left-2, 10)
    locate("███", left-1, 10)
    locate("███", left+1, 10)
    locate("███", left+2, 10)
    locate("███", left+3, 10)
    locate("███", left-5, 11)
    locate("███", left+4, 11)
    locate("███", left-5, 12)
    locate("███", left+5, 12)
    locate("███", left+5, 13)
    locate("███", left+5, 14)
    locate("███", left+5, 15)
    locate("███", left+5, 16)
    locate("███", left+4, 17)
    locate("███", left+3, 18)
    locate("███", left+3, 19)
    locate("███", left+2, 20)
    locate("███", left+2, 21)
    locate("███", left+1, 22)
    locate("███", left, 23)
    locate("███", left, 24)
    locate("███", left-1, 25)
    locate("███", left-2, 26)
    locate("███", left-3, 27)
    locate("███", left-4, 28)
    locate("███", left-4, 29)
    locate("███", left-5, 29)
    locate("███", left-5, 30)
    locate("███", left-4, 30)
    locate("███", left-3, 30)
    locate("███", left-2, 30)
    locate("███", left-1, 30)
    locate("███", left, 30)
    locate("███", left+1, 30)
    locate("███", left+2, 30)
    locate("███", left+3, 30)
    locate("███", left+4, 30)
    locate("███", left+5, 30)
    
def score_three(player):
    if player == 1:
        left = p1_left
    else:
        left = p2_left
    locate("███", left-4, 10)
    locate("███", left-3, 10)
    locate("███", left-2, 10)
    locate("███", left-1, 10)
    locate("███", left-5, 11)
    locate("███", left-5, 12)
    locate("███", left+1, 10)
    locate("███", left+2, 11)
    locate("███", left+3, 12)
    locate("███", left+3, 13)
    locate("███", left+4, 14)
    locate("███", left+4, 15)
    locate("███", left+3, 16)
    locate("███", left+3, 17)
    locate("███", left+2, 18)
    locate("███", left+1, 19)
    locate("███", left, 20)
    locate("███", left-1, 20)
    locate("███", left-2, 20)
    locate("███", left, 21)
    locate("███", left-1, 21)
    locate("███", left-2, 21)
    locate("███", left+1, 22)
    locate("███", left+2, 23)
    locate("███", left+3, 24)
    locate("███", left+3, 25)
    locate("███", left+4, 26)
    locate("███", left+4, 27)
    locate("███", left+3, 28)
    locate("███", left+2, 29)
    locate("███", left+1, 30)
    locate("███", left-5, 28)
    locate("███", left-5, 29)
    locate("███", left-1, 30)
    locate("███", left-2, 30)
    locate("███", left-3, 30)
    locate("███", left-4, 30)
    
def score_four(player):
    if player == 1:
        left = p1_left
    else:
        left = p2_left
    locate("███", left-4, 10)
    locate("███", left+4, 10)
    locate("███", left-4, 11)
    locate("███", left+4, 11)
    locate("███", left-4, 12)
    locate("███", left+4, 12)
    locate("███", left-4, 13)
    locate("███", left+4, 13)
    locate("███", left-4, 14)
    locate("███", left+4, 14)
    locate("███", left-4, 15)
    locate("███", left+4, 15)
    locate("███", left-4, 16)
    locate("███", left+4, 16)
    locate("███", left-4, 17)
    locate("███", left+4, 17)
    locate("███", left-4, 18)
    locate("███", left+4, 18)
    locate("███", left-3, 18)
    locate("███", left-2, 18)
    locate("███", left-1, 18)
    locate("███", left, 18)
    locate("███", left+1, 18)
    locate("███", left+2, 18)
    locate("███", left+3, 18)
    locate("███", left+4, 18)
    locate("███", left+5, 18)    
    locate("███", left+4, 19)
    locate("███", left+4, 20)
    locate("███", left+4, 21)
    locate("███", left+4, 22)
    locate("███", left+4, 23)
    locate("███", left+4, 24)
    locate("███", left+4, 25)
    locate("███", left+4, 26)
    locate("███", left+4, 27)
    locate("███", left+4, 28)
    locate("███", left+4, 29)
    locate("███", left+4, 30)
    
def score_five(player):
    if player == 1:
        left = p1_left
    else:
        left = p2_left
    locate("███", left-5, 10)
    locate("███", left-4, 10)
    locate("███", left-3, 10)
    locate("███", left-2, 10)
    locate("███", left-1, 10)
    locate("███", left, 10)
    locate("███", left+1, 10)
    locate("███", left+2, 10)
    locate("███", left+3, 10)
    locate("███", left+4, 10)
    locate("███", left+5, 10)
    locate("███", left-5, 11)
    locate("███", left-5, 12)
    locate("███", left-5, 13)
    locate("███", left-5, 14)
    locate("███", left-5, 15)
    locate("███", left-5, 16)
    locate("███", left-5, 17)
    locate("███", left-5, 18)
    locate("███", left+4, 18)
    locate("███", left-3, 18)
    locate("███", left-2, 18)
    locate("███", left-1, 18)
    locate("███", left, 18)
    locate("███", left+1, 18)
    locate("███", left+2, 18)
    locate("███", left+3, 18)  
    locate("███", left+5, 19)
    locate("███", left+5, 20)
    locate("███", left+5, 21)
    locate("███", left+5, 22)
    locate("███", left+5, 23)
    locate("███", left+5, 24)
    locate("███", left+5, 25)
    locate("███", left+5, 26)
    locate("███", left+5, 27)
    locate("███", left+5, 28)
    locate("███", left+5, 29)
    locate("███", left+3, 30)
    locate("███", left+2, 30)
    locate("███", left+1, 30)
    locate("███", left, 30)
    locate("███", left-1, 30)
    locate("███", left-2, 30)
    locate("███", left-3, 30)
    locate("███", left-4, 30)
    locate("███", left-5, 29)

def score_six(player):
    if player == 1:
        left = p1_left
    else:
        left = p2_left  
    locate("███", left-3, 10)
    locate("███", left-2, 10)
    locate("███", left-1, 10)
    locate("███", left, 10)
    locate("███", left+1, 10)
    locate("███", left+2, 10)
    locate("███", left+3, 10)
    locate("███", left+4, 10)
    locate("███", left-4, 11)
    locate("███", left-5, 12)
    locate("███", left-5, 13)
    locate("███", left-5, 14)
    locate("███", left-5, 15)
    locate("███", left-5, 16)
    locate("███", left-5, 17)
    locate("███", left-5, 18)
    locate("███", left-5, 19)
    locate("███", left-5, 20)
    locate("███", left+4, 20)
    locate("███", left-3, 20)
    locate("███", left-2, 20)
    locate("███", left-1, 20)
    locate("███", left, 20)
    locate("███", left+1, 20)
    locate("███", left+2, 20)
    locate("███", left+3, 20)  
    locate("███", left+4, 20)
    locate("███", left-5, 20)
    locate("███", left+5, 21)
    locate("███", left-5, 21)
    locate("███", left+5, 22)
    locate("███", left-5, 22)
    locate("███", left+5, 23)
    locate("███", left-5, 23)
    locate("███", left+5, 24)
    locate("███", left-5, 24)
    locate("███", left+5, 25)
    locate("███", left-5, 25)
    locate("███", left+5, 26)
    locate("███", left-5, 26)
    locate("███", left+5, 27)
    locate("███", left-5, 27)
    locate("███", left+5, 28)
    locate("███", left-5, 28)
    locate("███", left+5, 29)
    locate("███", left+3, 30)
    locate("███", left+2, 30)
    locate("███", left+1, 30)
    locate("███", left, 30)
    locate("███", left-1, 30)
    locate("███", left-2, 30)
    locate("███", left-3, 30)
    locate("███", left-4, 30)
    locate("███", left-5, 29)

def score_seven(player):
    if player == 1:
        left = p1_left
    else:
        left = p2_left
    locate("███", left-6, 10)
    locate("███", left-5, 10)
    locate("███", left-4, 10)
    locate("███", left-3, 10)
    locate("███", left-2, 10)
    locate("███", left-1, 10)
    locate("███", left, 10)
    locate("███", left+1, 10)
    locate("███", left+2, 10)
    locate("███", left+3, 10)
    locate("███", left+4, 10)
    locate("███", left+5, 10)
    locate("███", left+4, 11)
    locate("███", left+5, 11)
    locate("███", left+4, 12)
    locate("███", left+4, 13)
    locate("███", left+4, 14)
    locate("███", left+3, 15)
    locate("███", left+3, 16)
    locate("███", left+3, 17)
    locate("███", left+3, 18)
    locate("███", left+2, 19)
    locate("███", left+2, 20)
    locate("███", left+2, 21)
    locate("███", left+2, 22)
    locate("███", left+2, 23)
    locate("███", left+2, 24)
    locate("███", left+2, 25)
    locate("███", left+1, 26)
    locate("███", left+1, 27)
    locate("███", left+1, 28)
    locate("███", left, 29)
    locate("███", left, 30)

def score_eight(player):
    if player == 1:
        left = p1_left
    else:
        left = p2_left
    locate("███", left-3, 10)
    locate("███", left-2, 10)
    locate("███", left-1, 10)
    locate("███", left, 10)
    locate("███", left+1, 10)
    locate("███", left+2, 10)
    locate("███", left+3, 10)
    locate("███", left+4, 10)
    locate("███", left-5, 11)
    locate("███", left+5, 11)
    locate("███", left-5, 12)
    locate("███", left+5, 12)
    locate("███", left-5, 13)
    locate("███", left+5, 13)
    locate("███", left-5, 14)
    locate("███", left+5, 14)
    locate("███", left-5, 15)
    locate("███", left+5, 15)
    locate("███", left-5, 16)
    locate("███", left+5, 16)
    locate("███", left-5, 17)
    locate("███", left+5, 17)
    locate("███", left-5, 18)
    locate("███", left+5, 18)
    locate("███", left-5, 19)
    locate("███", left+5, 19)
    locate("███", left-2, 20)
    locate("███", left-1, 20)
    locate("███", left, 20)
    locate("███", left+1, 20)
    locate("███", left+2, 20)
    locate("███", left+5, 21)
    locate("███", left-5, 21)
    locate("███", left+5, 22)
    locate("███", left-5, 22)
    locate("███", left+5, 23)
    locate("███", left-5, 23)
    locate("███", left+5, 24)
    locate("███", left-5, 24)
    locate("███", left+5, 25)
    locate("███", left-5, 25)
    locate("███", left+5, 26)
    locate("███", left-5, 26)
    locate("███", left+5, 27)
    locate("███", left-5, 27)
    locate("███", left+5, 28)
    locate("███", left-5, 28)
    locate("███", left+5, 29)
    locate("███", left+3, 30)
    locate("███", left+2, 30)
    locate("███", left+1, 30)
    locate("███", left, 30)
    locate("███", left-1, 30)
    locate("███", left-2, 30)
    locate("███", left-3, 30)
    locate("███", left-4, 30)
    locate("███", left-5, 29)

def score_nine(player):
    if player == 1:
        left = p1_left
    else:
        left = p2_left
    locate("███", left-3, 10)
    locate("███", left-2, 10)
    locate("███", left-1, 10)
    locate("███", left, 10)
    locate("███", left+1, 10)
    locate("███", left+2, 10)
    locate("███", left+3, 10)
    locate("███", left+4, 10)
    locate("███", left-5, 11)
    locate("███", left+5, 11)
    locate("███", left-5, 12)
    locate("███", left+5, 12)
    locate("███", left-5, 13)
    locate("███", left+5, 13)
    locate("███", left-5, 14)
    locate("███", left+5, 14)
    locate("███", left-5, 15)
    locate("███", left+5, 15)
    locate("███", left-5, 16)
    locate("███", left+5, 16)
    locate("███", left-5, 17)
    locate("███", left+5, 17)
    locate("███", left-5, 18)
    locate("███", left+5, 18)
    locate("███", left-5, 19)
    locate("███", left+5, 19)
    locate("███", left-3, 20)
    locate("███", left-2, 20)
    locate("███", left-1, 20)
    locate("███", left, 20)
    locate("███", left+1, 20)
    locate("███", left+2, 20)
    locate("███", left+3, 20)
    locate("███", left+5, 21)
    locate("███", left+5, 22)
    locate("███", left+5, 23)
    locate("███", left+5, 24)
    locate("███", left+5, 25)
    locate("███", left+5, 26)
    locate("███", left+5, 27)
    locate("███", left+5, 28)
    locate("███", left+5, 29)
    locate("███", left+3, 30)
    locate("███", left+2, 30)
    locate("███", left+1, 30)
    locate("███", left, 30)
    locate("███", left-1, 30)
    locate("███", left-2, 30)
    locate("███", left-3, 30)
    locate("███", left-4, 30)
    locate("███", left-5, 29)

def score_win(player):
    left = p1_left

    if player == 1:
        locate("███", left+31, 21)
        locate("███", left+30, 22)
        locate("███", left+29, 23)
        locate("███", left+28, 24)
        locate("███", left+27, 25)

        locate("███", left+31, 19)
        locate("███", left+30, 18)
        locate("███", left+29, 17)
        locate("███", left+28, 16)
        locate("███", left+27, 15)

    else:
        locate("███", left-4, 21)
        locate("███", left-3, 22)
        locate("███", left-2, 23)
        locate("███", left-1, 24)
        locate("███", left, 25)

        locate("███", left-4, 19)
        locate("███", left-3, 18)
        locate("███", left-2, 17)
        locate("███", left-1, 16)
        locate("███", left, 15)

    locate("███", left-5, 20)
    locate("███", left-4, 20)
    locate("███", left-3, 20)
    locate("███", left-2, 20)
    locate("███", left-1, 20)
    locate("███", left, 20)
    locate("███", left+1, 20)
    locate("███", left+2, 20)
    locate("███", left+3, 20)
    locate("███", left+4, 20)
    locate("███", left+5, 20)
    locate("███", left+6, 20)
    locate("███", left+7, 20)
    locate("███", left+8, 20)
    locate("███", left+9, 20)
    locate("███", left+10, 20)
    locate("███", left+11, 20)
    locate("███", left+12, 20)
    locate("███", left+13, 20)
    locate("███", left+14, 20)
    locate("███", left+15, 20)
    locate("███", left+16, 20)
    locate("███", left+17, 20)
    locate("███", left+18, 20)
    locate("███", left+19, 20)
    locate("███", left+20, 20)
    locate("███", left+21, 20)
    locate("███", left+22, 20)
    locate("███", left+23, 20)
    locate("███", left+24, 20)
    locate("███", left+25, 20)
    locate("███", left+26, 20)
    locate("███", left+27, 20)
    locate("███", left+28, 20)
    locate("███", left+29, 20)
    locate("███", left+30, 20)
    locate("███", left+31, 20)
    locate("███", left+32, 20)