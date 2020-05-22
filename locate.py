import math
import sys

# Make the whole code 3.x.x compatible too...
if sys.version[0]=="3": raw_input=input

char="*"
x=20
y=19

# A Simple clear screen command for this DEMO...
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

locate("███", 5, 2)
locate("███", 5, 3)
locate("███", 5, 4)
locate("███", 5, 5)
locate("███", 5, 6)
locate("███", 5, 7)
locate("███", 5, 8)