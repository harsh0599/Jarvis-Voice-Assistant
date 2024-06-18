import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to handle text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process voice commands
def process_command(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif command.startswith("play"):
        song = command.split(" ", 1)[1]
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found in the music library.")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            # Listen for the wake word "Jarvis"
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for 'Jarvis'...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                word = recognizer.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Yes?")
                    # Listen for the actual command
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source)
                        print("Jarvis is active, listening for your command...")
                        audio = recognizer.listen(source, timeout=5)
                        command = recognizer.recognize_google(audio)
                        process_command(command)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")