# utf coding: utf-8
import time

import os

#birthday format should be 
	#Mnthday    name   Surname .... without quotes
#ex : 0631
#ex : 0801

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

	for line in fileName:
		if today in line:
			line = line.split(' ')#takes in two arguments - separator, maxsplit
			
			#split() method returns a list of strings after
			#breaking the given string by the specified sepa-
			#rator.
			flag = 1
			#flag =1 means till it is TRUE
			#flag =0 means till it is FALSE
			os.system('notify-send "today birthday: ' +line[1] + ' ' + line[2] + '"' )
	if flag == 0:
			os.system('notify-send "No birthday today"')

if __name__ == '__main__':
	checkTodayBirthdays()					