import cPickle as pickle
from msvcrt import getch, getche
def intake():
	readfile = open('persistentinfo', 'r')
	writefile = open('persistentinfo', 'wb')
	try:
		info = pickle.load(readfile)
	except EOFError:
		info = {}
	print 'What is the phone number you would like to store? Press "c" to cancel.\n'
	keypress = getche()
	if keypress == 'C' or keypress == 'c':
		main()
	elif keypress == '\r':
		print 'Number not entered! Please try again.\n\n'
		intake()
	else:
		number = raw_input()
		if number == '':
			print 'Number not entered! Please try again.\n\n'
			intake()

def main():
	print "\nHello! Thanks for using PrankCall, please choose one of the options below.\n"
	print "Press 'i' to record a phone number\n"
	print "Press 'e' to exit\n"
	keypress = ord(getch())
	if keypress == 105 or keypress == 73:
		intake()
	elif keypress == 69 or keypress == 101:
		exit()

while True:
	main()