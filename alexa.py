import speech_recognition as sr
import pyttsx3 #text to speech
import pywhatkit # it will play song from youtube
import wolframalpha

client=wplframalpha.Client("AXE468-235R7KKV22") #creates a client object for the Wolfram Alpha API using your provided API key.
listener=sr.Recognizer() #intialise a recognizer object from speech_recognition library  which will capture audio input from microphone
engine=pyttsx3.init() #initialize text to speech
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) # to recognize female voice = 1
engine.say("Hello I am Alexa")
engine.say("How can I help you")
engine.runAndWait()

def take_command():
	with sr.Microphone() as source: #microphone function takes the source of input as text or voice
		print("Listening....")
		voice=listner.listen(source) #listen function is stored in voice variable
		command=listner.recognize_google(voice) #recognise input using google's speech recognition service
		command=command.lower() #covert recognise text to lowercase
		# if 'alexa' in command: #when we say alexa then only it will listen
			print(command)
		return command

def run_alexa():
	try:
		command=take_command()#takes input
		print(command)
		if 'play' in command:
			song=command.replace('play',' ') #Extracts song name by removing play
			engine.say('playing'+song) #
			pywhatkit.playonyt(song) #uses pywhatkit to play requested song from youtube
		elif 'alexa' in command:
			command=command.replace('alexa',' ')
			query=command #assign remaining command to a variable
			res=client.query(query)  #makes a query to wolframeAlpha api
			output=next(res.result).text #retrives the texts result from api response
			print(output)
			engine.say(output)
			engine.runAndWait()

	except:
		engine.runAndWait()
		#print("Say again")
		engine.say("Sorry Please Say again")
		engine.runAndWait()

while True:
	run_alexa() #continuosly runs this function to listen for respond to user command


