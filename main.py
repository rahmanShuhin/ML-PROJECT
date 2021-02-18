#import required library
import speech_recognition as sr
import webbrowser
import time
import  playsound
import os
import random
from gtts import gTTS
from time import ctime
r = sr.Recognizer()
m = sr.Microphone()


#function for recognize audio input
def record_audio(ask = False):
    try:
        print("A moment of silence, please...")
        with m as source:
            if ask:
                jupitar_speak(ask)
            r.adjust_for_ambient_noise(source)

        while True:
            print("Say something!")
            with m as source:
                audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)

                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    print(u"You said 2 {}".format(value).encode("utf-8"))
                else:  # this version of Python uses unicode for strings (Python 3+)
                    print(format(value))
                    return format(value)
            except sr.UnknownValueError:
                jupitar_speak("Oops! Didn't catch that")
            except sr.RequestError as e:
                jupitar_speak("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass


#function for text to specch
def jupitar_speak(aud_string):
    tts=gTTS(text=aud_string,lang="en")
    r= random.randint(1,100000000)
    aud_file='audio-'+str(r)+'.mp3'
    tts.save(aud_file)
    playsound.playsound(aud_file)
    # print("working")
    print(aud_string)
    os.remove(aud_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        jupitar_speak('My Name Is Jupitar')
    elif 'what time is it' in voice_data:
        jupitar_speak(ctime())
    elif "open Google" in voice_data:
        url='https://google.com'
        webbrowser.get().open(url)
        jupitar_speak("ok sir")
    elif "open video" in voice_data:
        url='https://www.youtube.com'
        webbrowser.get().open(url)
        jupitar_speak("ok boss")
    elif "search" in voice_data:
        search=record_audio("What do you want to search for ?")
        url ='https://google.com/search?q=' + search
        webbrowser.get().open(url)
        jupitar_speak("Here is what i found for " + search)
    elif 'find location' in voice_data:
        location=record_audio("what is the location")
        url='https://google.nl/maps/place/' + location +'/&amp;'
        webbrowser.get().open(url)
        jupitar_speak("Here is the location of  "+ location)
    elif 'go away' in voice_data:
        jupitar_speak("Ok Bye")
        exit()


time.sleep(1)
jupitar_speak("how can i help you")
while 1:
    voice_data=record_audio()
    respond(voice_data)
