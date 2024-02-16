import webbrowser
from Modules import say_speak as sp
import sys
import os

import wikipedia

import pyautogui





chr_path=r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chr_path))

while True:

    Query=sp.micro()
    query= Query.lower().replace(" ","")




#-------------------------------------------------------------internet searchings----------------------------------------------------


    if "google" in query:

        webbrowser.get('chrome').open_new_tab('google.com')

    elif "youtube" in query:
        sp.speak("What do you want to search on youtube ")
        webbrowser.get('chrome').open_new_tab('youtube.com')


    elif "wikipedia" in query:
        if query=="wikipedia":
            sp.speak("What do you wanna search")
            q=sp.micro().lower().replace(" ","")
            try:
                result = wikipedia.summary(q, sentences=2)
                print(result)
                sp.speak(result)

            except:
                print("404 not found try again later")

        else:
            try:
                result= wikipedia.summary(query,sentences=2)
                print(result)
                sp.speak(result)
            except:
                print("No such result")


    elif "spotify" in query:
        webbrowser.get('chrome').open_new_tab('https://open.spotify.com/')























    # ---------------------------------------------------system commands----------------------------------------------------


    elif "exit" in query:
        sys.exit()

    elif "shutdown" in query:
        os.system("shutdown /s /t 0")

    elif "taskmanager" in query:
        pyautogui.hotkey('ctrl' , 'shift' , 'esc')

    elif "tabchange" in query:
        with pyautogui.hold('alt'):
            pyautogui.press('tab')






