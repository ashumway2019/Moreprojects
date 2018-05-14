import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Tell me what video to look for.")
    print("Listening...")
    audio = r.listen(source)
    print("Thinking...")
try:
    words = r.recognize_google(audio)
    speak.Speak("OK, let's look for " + r.recognize_google(audio))
    wb.open("https://www.youtube.com/results?search_query=" + words)

except sr.UnknownValueError:
    print("Google Speech Recognitioin could not understand audio")
except sr.Requesterror as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

