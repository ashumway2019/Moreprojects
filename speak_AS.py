import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What's your favorite tv show?")

answer = pg.prompt("Enter your favorite tv show below.")

if answer == "Dawson's Creek":
    speak.Speak("Wow, my favorite tv show is " + answer + "too. Pacey is my favorite character.")
elif answer == "Gossip Girl":
    speak.Speak("Wow, my favorite tv show is " + answer + "too. Serena is my favorite character.")
elif answer == "Glee":
    speak.Speak("Wow, my favorite tv show is " + answer + "too. Rachel is my favorite character.")
elif answer == "One Tree Hill":
    speak.Speak("Wow, my favorite tv show is " + answer + "too. Lucas is my favorite character.")
else:
    speak.Speak("I haven't watched " + answer + ".")

speak.Speak("What's your favorite movie?")
movie = pg.prompt("Enter your favorirte movier below.")
speak.Speak("OK, searchiung youtube for " + movie + "trailer.")
wb.open("https://www.youtube.com/results?search_query=" + movie + " trailer")
