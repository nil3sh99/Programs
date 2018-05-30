#first you have to install speech_recognition using terminal
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
	print('Say something')
	audio = r.listen(source)

try:
	print('I detected this: ' + r.recognize_google(audio))

except:
	pass

#if we have an audio file already and want to covert that audio file into text then...

#import speech_recognition as sr

#AF = ("file_destination")
#r = sr.Recognizer()

#with sr.AudioFile(AF) as source:
#	print('Given file says: \n')
#	audio = r.record(source)

#try:
#	print('I detected this: ' + r.recognize_google(audio))

#except:
#	pass
