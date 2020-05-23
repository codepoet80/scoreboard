import math
import sys

# Make the whole code 3.x.x compatible too...
if sys.version[0]=="3": raw_input=input

char="*"
x=20
y=19
p1_left = 15
p2_left = 42

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

# A Simple clear screen command for this DEMO...
def clear():
    for n in range(0, 64, 1): print("\r\n")

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
    locate("███", left, 12)
    locate("███", left, 13)
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
    locate("███", left, 30)
    
def score_two(player):
    if player == 1:
        left = p1_left
    else:
        left = p2_left
    locate("███", left-4, 10)
    locate("███", left-3, 10)
    locate("███", left-2, 10)
    locate("███", left-1, 10)
    locate("███", left-5, 11)
    locate("███", left+1, 10)
    locate("███", left+1, 11)
    locate("███", left+3, 12)
    locate("███", left+3, 13)
    locate("███", left+3, 14)
    locate("███", left+3, 15)
    locate("███", left+2, 16)
    locate("███", left+2, 17)
    locate("███", left+2, 18)
    locate("███", left+1, 19)
    locate("███", left+1, 20)
    locate("███", left, 21)
    locate("███", left, 22)
    locate("███", left-1, 23)
    locate("███", left-1, 24)
    locate("███", left-2, 25)
    locate("███", left-3, 26)
    locate("███", left-4, 27)
    locate("███", left-5, 28)
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
    locate("███", left+1, 10)
    locate("███", left+1, 11)
    locate("███", left+1, 12)
    locate("███", left+2, 12)
    locate("███", left+3, 13)
    locate("███", left+3, 14)
    locate("███", left+3, 15)
    locate("███", left+2, 16)
    locate("███", left+2, 17)
    locate("███", left+1, 18)
    locate("███", left+1, 19)
    locate("███", left, 20)
    locate("███", left, 21)
    locate("███", left+1, 22)
    locate("███", left+1, 23)
    locate("███", left+2, 24)
    locate("███", left+2, 25)
    locate("███", left+3, 26)
    locate("███", left+3, 27)
    locate("███", left+3, 28)
    locate("███", left+2, 28)
    locate("███", left+1, 29)
    locate("███", left+1, 30)
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
    