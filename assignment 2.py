import speech_recognition as sr

recognizer = sr.Recognizer()

users = {
    "admin": {"password": "admin7777", "role": "admin"},
    "user": {"password": "user7777", "role": "user"},
}


def check_access(user, password):
    if user in users and users[user]["password"] == password:
        return users[user]["role"]
    else:
        return None

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


            
def main():
    username = input("Enter the username please!")
    password = input("Enter the password please!")
    role = check_access(username, password)
    if role:
        print(f"Access for {role}")
        while True:
            command = speech_recognize()
            if command:
                if role == "admin":
                    if command == "shutdown":
                        print("shutting down.....")
                    else:
                        print("Not known Command")
                elif role == "user":
                    if command == "add":
                        print("Adding profile...")
                    else:
                        print("Not known command")
    else:
        print("denied access")


