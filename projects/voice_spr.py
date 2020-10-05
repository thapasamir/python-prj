import pyttsx3
import speech_recognition as sr


#calling window voice api
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)


#making text to voice function
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

#making audio to text function
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
	if 1:
		speak("welcome to sizor paper rock game")
		speak("what is your name")
		query = get_voice().lower()
		speak(queryas)
		
		


