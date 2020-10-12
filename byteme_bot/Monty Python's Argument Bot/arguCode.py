# Servo setup
from gpiozero import Servo
mouthServo = Servo(26)
global talk

# Generic imports
import time
import os
import threading
from random import randint

# Dialogflow setup
import aiy.voice.tts 
import dialogflow_v2 as dialogflow
from aiy.board import Board
from aiy.cloudspeech import CloudSpeechClient

session_client = dialogflow.SessionsClient()
session = session_client.session_path('xxxxxxx', 12345)

def getDialogResponse(text):

    text_input = dialogflow.types.TextInput(text=text, language_code='EN')
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    text = response.query_result.fulfillment_text

    return response

def talk():

    global talk
    while True:
        while talk:
            sleepTime = (randint(1, 3))/10
            mouthServo.max()
            time.sleep(sleepTime)
            mouthServo.mid()
            time.sleep(sleepTime)
        
        mouthServo.detach()

moveLidThread = threading.Thread(target=talk)
moveLidThread.start()

def say(test):
    aiy.voice.tts.say(test, lang='en-GB', volume=50, pitch=60, speed=80, device='default')

while True:

    print('Listening...')
    spokenText = client.recognize() 

    if spokenText is None:
        print('You said nothing.')
    else:
        response = getDialogResponse(spokenText)
        responseText = response.query_result.fulfillment_text

        talk = True
        say(responseText)
        talk = False

    time.sleep(0.5)# Servo setup
from gpiozero import Servo
mouthServo = Servo(26)
global talk

# Generic imports
import time
import os
import threading
from random import randint

# Dialogflow setup
import aiy.voice.tts 
import dialogflow_v2 as dialogflow
from aiy.board import Board
from aiy.cloudspeech import CloudSpeechClient

session_client = dialogflow.SessionsClient()
session = session_client.session_path('xxxxxxx', 12345)

def getDialogResponse(text):

    text_input = dialogflow.types.TextInput(text=text, language_code='EN')
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    text = response.query_result.fulfillment_text

    return response

def talk():

    global talk
    while True:
        while talk:
            sleepTime = (randint(1, 3))/10
            mouthServo.max()
            time.sleep(sleepTime)
            mouthServo.mid()
            time.sleep(sleepTime)
        
        mouthServo.detach()

moveLidThread = threading.Thread(target=talk)
moveLidThread.start()

def say(test):
    aiy.voice.tts.say(test, lang='en-GB', volume=50, pitch=60, speed=80, device='default')

while True:

    print('Listening...')
    spokenText = client.recognize() 

    if spokenText is None:
        print('You said nothing.')
    else:
        response = getDialogResponse(spokenText)
        responseText = response.query_result.fulfillment_text

        talk = True
        say(responseText)
        talk = False

    time.sleep(0.5)