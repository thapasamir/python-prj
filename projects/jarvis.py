#MOdule importing section
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import os
import random
#getting the voice api of computer
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

#making speak function
def bol_bc(audio):
	engine.say(audio)
	engine.runAndWait()

#greeting_function
def welcome():
	time =int(datetime.datetime.now().hour)
	if time >= 0 and time <=12:
		bol_bc("Good morning samir")
	elif time >=12 and time <=5:
		bol_bc("Good afternoon samir")
	else:
		bol_bc("good evening samir")

	bol_bc("Hello i am emo the robot from future")
	bol_bc("what can i help you")

#getting voice command and changing it into string
def get_voice():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("listenning.....")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("processing...")
		query = r.recognize_google(audio, language='en-us')
		print(f'User said:{query}\n')

	except Exception as e:
		print("Sorry i don,t understand say again..")
		return"none"
	return query

if __name__ == "__main__":
	#welcome()
	if 1:
		query = get_voice().lower()
	     #wekepedia speak
		if 'wikipedia' in query:
			bol_bc('searching in wikipedia...')
			query = query.replace("wikipedia", "")
			reasults = wikipedia.summary(query, sentences=2)
			bol_bc('according to wiki')
			print(reasults)
			bol_bc(reasults)

		elif "open youtube" in query:
			webbrowser.open("Youtube.com")

		elif "f*** you" in query:
			bol_bc('lado kha muji')
			bol_bc("madarchut")
			bol_bc("fuck you")
			bol_bc("RAndi ko chora")
			bol_bc("bahinchod")

		elif "open facebook" in query:
			webbrowser.open(facebook.com)

		elif "open facebook" in query:
			webbrowser.open(youtube.com)

		elif "play music"  in query:
			music_pat = 'F:\\music'
			songs = os.listdir(music_pat)
			song_count = 0
			for i in songs:
				song_count+=1
			rand_chooser = random.randrange(song_count)
			os.startfile(os.path.join(music_pat, songs[rand_chooser]))

		elif "the time" in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			bol_bc(f'The time is {strTime}')

		elif "sublime text" in query:
			s_path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
			os.startfile(s_path)

		





