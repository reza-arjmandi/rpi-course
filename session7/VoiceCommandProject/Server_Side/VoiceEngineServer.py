import zmq
import time
from threading import *
import speech_recognition as sr

broadcastMSG = "None"

def Listener():
    global broadcastMSG
    while(1):
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            recognizedCommand = r.recognize_google(audio);
            print("Google Speech Recognition thinks you said " + recognizedCommand)
            if(recognizedCommand == "start"):
                broadcastMSG = "start"
            elif(recognizedCommand == "stop"):
                broadcastMSG = "stop"
            elif(recognizedCommand == "clockwise"):
                broadcastMSG = "clockwise"
            elif(recognizedCommand == "counter clockwise"):
                broadcastMSG = "counter clockwise"
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
if __name__ == "__main__":
    voiceThrad = Thread(target = Listener)
    voiceThrad.start()
    ctx = zmq.Context.instance()
    publisher = ctx.socket(zmq.PUB)
    publisher.bind("tcp://*:9999")
    counter = 0
    lastMessage = "lastMessage"
    while(1):
        if(lastMessage != broadcastMSG):
            publisher.send_string(broadcastMSG)
            print("Broadcast Message " + str(counter) + " : " + broadcastMSG)
            lastMessage = broadcastMSG
            counter += 1
            time.sleep(0.05)