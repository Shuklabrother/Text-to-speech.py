from androidhelper import sl4a

droid=sl4a.Android()

def speak(text):
       droid.ttsSpeak(text)

while True:
    say = input(str("Text:"))
    speak(say) 
