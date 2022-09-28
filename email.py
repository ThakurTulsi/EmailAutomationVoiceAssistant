import smtplib  #smtp stands for simple mail transfer protocol
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices') 
voices = engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice) #Using Google's API to recognize the voice command
            print(info)
            return info.lower()


    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.starttls() #tls means transport layer security
    server.login('abc@gmail.com', 'abc')
    email = EmailMessage()
    email['From'] = 'abc@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    


email_list = { 
    'myself':'abc@gmail.com',
    'members':'abc@gmail.com',
    'classmate':'abc@gmail.com',
    'sister':'abc@gmail.com',
    'manager': 'abc@gmail.com',
    'boss': 'abc@gmail.com'
}


def get_email_info():
    talk('Hello there, to whom you want to send the email')
    name =  get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject =  get_info()
    talk('Please tell me the text of your emial')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey user, your email has been sent')
    talk('Do you want me to send more emails?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    else:
        print('Okay good bye, it was pleasure to help you')
        talk('Okay good bye, it was pleasure to help you')  




get_email_info()    