import pyttsx3
from pyttsx3.drivers import sapi5 # I don't know why this has to be here but it does for the exe to work

engine = pyttsx3.init()

def options():
    print("\nThese are the options.")
    voices = engine.getProperty("voices")

    print("What would you like to change?")
    print('''
    R - Rate
    L - Loudness
    V - Voice
    B - Back
    ''')

    choice = input()
    choice = choice.lower()

    if choice == "r":
        speed = input("What would you like the rate to be?: ")

        try:
            speed = float(speed)
        except ValueError:
            print("Please enter a valid number.")
            options()

        engine.setProperty("rate", speed)
        on_open()
        
    elif choice == "l":
        loudness = input("What would you like the volume to be? (Between 0 and 1): ")

        try:
            loudness = float(loudness)
        except ValueError:
            print("Please enter a valid number.")
            options()
        
        if loudness > 1:
            loudness = 1
            engine.setProperty("volume", loudness)
            on_open()
        elif loudness < 0:
            loudness = 0.1
            engine.setProperty("volume", loudness)
            on_open()
        else:
            engine.setProperty("volume", loudness)
            on_open()
    elif choice == "v":
        m_or_f = input("Would you like your voice to be male or female? (m/f): ")
        m_or_f = m_or_f.lower()

        if m_or_f == "m":
            engine.setProperty("voice", voices[0].id)
            on_open()
        elif m_or_f == "f":
            engine.setProperty("voice", voices[1].id)
            on_open()
        else:
            print("Please enter either m or f.")
            options() 
    elif choice == "b":
        on_open()
    else:
        print("Please select either r, l, v, or b.")
        options()


def on_open():
    print("This is a text to speech generator.")
    print("What would you like to do?\n")
    print('''
    S - Speak
    O - Options
    E - Exit
    ''')

    choice = input()
    choice = choice.lower()

    if choice == "e":
        exit()
    elif choice == "o":
        options()
    elif choice == "s":
        main()
    else:
        print("You must select either s, o, or e.")
        on_open()

def main():

    txt_to_speak = input("Enter some text: ")
    engine.say(txt_to_speak)
    engine.runAndWait()
    run_again()

def run_again():

    rerun = input("\nDo you want to run the program again? (y/n): ")
    rerun = rerun.lower()

    if rerun == "y":
        on_open()
    elif rerun == "n":
        exit()
    else:
        print("You must enter either y or n.")
        run_again()

on_open()
