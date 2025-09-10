import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "play aditya" in c :
        webbrowser.open("https://youtu.be/yyUodifWNxU?feature=shared")
    elif "play teju" in c :
        webbrowser.open("https://youtu.be/Ov0YGGSY6gY?feature=shared")
    elif "stop listening" in c:
        speak("Goodbye Aditya")
        exit()
    else:
        speak("I didn't understand the command.")

if __name__ == "__main__":
    speak("Hi Aditya")
    while True:
        print("Recognizing wake word...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening for 'Jarvis'...")
                audio = recognizer.listen(source, timeout=8, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
                print("Heard:", word)

            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    print("Jarvis Active..")
                    audio = recognizer.listen(source, timeout=8, phrase_time_limit=6)
                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    processcommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except Exception as e:
            print("Error:", e)
