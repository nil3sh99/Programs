import time

import os

#birthday format should be 
#Mnth day    name   Surname .... without quotes

birthdayFile = '/home/nilesh/Desktop/Work/python-progs/Python-progs/birthday_reminder/rawData.txt'

def checkTodayBirthdays():
	
	fileName = open(birthdayFile, 'r')
	#open: Open a file, returning an object of the file type described in 
	#section File Objects. If the file cannot 
	#be opened, IOError is raised. When opening a file,
	#it’s preferable to use open() instead of invoking
	#the file constructor directly.
	
	today = time.strftime('%m%d')
	
	#strft : The method strftime() converts a tuple or
	#struct_time representing a time as returned by gmtime()
	#or localtime() to a string as specified by the format argument.
	
	flag = 0

	for line in fileName
		if today in line:
			line = line.split('')
			
			#split() method returns a list of strings after
			#breaking the given string by the specified sepa-
			#rator.
			flag = 1
			#flag =1 means till it is TRUE
			#flag =0 means till it is FALSE
