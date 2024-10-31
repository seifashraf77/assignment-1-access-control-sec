import speech_recognition as sr

recognizer = sr.Recognizer()


def speech_recognize():
    with sr.Microphone() as source:
        print("Removing the noise")
        recognizer.adjust_for_ambient_noise(source)
        print("Hearing you ...")
        audio_data = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio_data)
            return text

        except sr.UnknownValueError:
            print("Forgive me,I don't know what you need!.")

        except sr.RequestError as e:
            print("Error!!!")


def conversation():
    not_end = True
    while not_end:
        user_input = speech_recognize()
        if user_input is not None:
            print(f"You Said: {user_input}")
            if "hello" == user_input.lower() or "hi" == user_input.lower():
                print("Siri: Hello! How can I help you today?")

            elif "how are you" == user_input.lower():
                print("Siri: I'm good , How about you!?")

            elif "what is your name" == user_input.lower():
                print("Siri: I am Siri you assisstant!")

            elif "what can you do" == user_input.lower():
                print("Siri: I can do what you want!")

            elif  "goodbye siri" == user_input.lower():
                print("Siri: Goodbye Seif ! Have a great day!")
                not_end = False

            else:
                print("Forgive me,I don't know what you need!.")

conversation()
