import pyttsx3

engine = pyttsx3.init()

while True:
    speak = str(input("🤖 What you Want me to Say? "))
    if speak.lower() == "q":
        break
    engine.say(speak)
    engine.runAndWait()




#OTHER LOGIC 

# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

# for index, voice in enumerate(voices):
#     print(f"{index}: {voice.name} - {voice.id}")
