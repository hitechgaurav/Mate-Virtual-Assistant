try:
    import random
    import datetime
    import voice
    import SpeechRecog as sr
    import time
    import intrserach
    import wolfram
    import mail
    import movie
    import temporary
except:
    print("Module Import Error")
    exit(0)

mouth=voice.Speak()
class Skeleton:
    def __init__(self):
        print("\t\t\t\t"," ----------------------------------------------- \n"
              "\t\t\t\t","|\t\t\t\t\t:: MATE ::\t\t\t\t\t |\n"
              "\t\t\t\t","|\t\t\t   the virutal assistant\t\t\t |\n"
              "\t\t\t\t","|","."*45,"|""\n\t\t\t\t |\t\t\t\t\t\t\t\t\t\t\t\t |\n\t\t\t\t |\t\t\t  "
              "Build  By GAURAV  KUMAR \t\t\t |\n\t\t\t\t |\t\t\t  Student Of RITS  Bhopal\t\t\t |"
              "\n\t\t\t\t |\t\t\t\t\t\t\t\t\t\t\t\t |\n\t\t\t\t |\t\t\t\t    0132CS171036\t\t\t\t |"
              "\n\t\t\t\t","","-"*47,"\n\n")
        self.greet=["Hi, I am MATE,  Your virtual Assistant","This is MATE","Hey! MATE in your computer"
            ,", Let me Introduce you to MATE; happy to help you","Hello User","Hi User, Mate welcomes you",
                    "Welcome to MATE world","MATE here","Mate welcomes you"]

    def  welcome(self):
        self.time=int(datetime.datetime.now().hour)
        if self.time>=4 and self.time<12:
            self.text="Good Morning, "+random.choice(self.greet)
            mouth.say(self.text)
        if self.time>=12 and self.time<16:
            self.text="Good Afternoon, "+random.choice(self.greet)
            mouth.say(self.text)
        if self.time>=16 and self.time<20:
            self.text="Good Evening, "+random.choice(self.greet)
            mouth.say(self.text)
        if self.time>=20:
            self.text="Have a peaceful night, Good Night, "+random.choice(self.greet)
            mouth.say(self.text)
        def service(self):
            mouth.say("This is what I can do for you.")
            print("\n\n\n","*"*60,"\n 1.\t\tTranslation in any ISO languages.\n","2.\t\tOS services.\n","3.\t\tMustitasking such as:-\n"
            ,"\t\t\t*\tSMS\n\t\t\t*\tEmails\n\t\t\t*\tFacebook Chat\n","4.\t\tWeather Queries and Basic Mathematics\n",
                           "5.\t\tWikipedia and Google Search","\n\n \t\t... and many more.\n","*"*60)
            time.sleep(3)
        service(self)
class Function(Skeleton):
    def __init__(self):
        self.ske=Skeleton()
        self.ske.welcome()
        self.speech=sr.Speech()
        self.crawl=intrserach.InternetSearch()
        self.ask_pattern=["How may I help you?","Need any help !","Any Instructions?",
                          "What can I do for you?"]
        self.ai=wolfram.Query()

    def intro(self):
        self.invent="5/8/2019"
        self.name=["Hi, Mate here","Hello, I am mate","Mate here to help you"]
        self.invn=["Mr.Gaurav","Gaurav Sir","I am build by Sir Gaurav"]

    #function to check wheather
    def weather_report(self, speech):
        self.weather_res=self.ai.search(speech)
        mouth.say(self.weather_res)

    #function to search anything on google or wikipedia
    def internet(self,iinput):
        if "wikipedia" or "wiki" in iinput:
            kt=x=0
            queryw=""
            for i in range(len(iinput)):
                if iinput[i]==" ":
                    x=i
                    break
            for j in range(x+1,len(iinput)):
                if iinput[j]==" ":
                    kt+=1
                if kt==2:
                    break
                queryw+=iinput[j]
            self.rest=self.crawl.wiki(queryw)
            mouth.say(self.rest)
        else:
            self.rest=self.crawl.google(iinput)
            mouth.say("Searching Information on Google : ")

    #function to retrive the speech data and see what to do
    def retrive(self, speech_data):
        try:
            if "weather" in speech_data:
                print("Calling Weather Function")
                self.weather_report(speech_data)
                self.ask()
            if "send mail" in speech_data or "email" in speech_data:
                mouth.say("what is receiver's address : ")
                self.rec=self.speech.recognise()
                self.rec=self.rec.replace(" ", "")
                print(self.rec)
                mouth.say("Is It correct credential ?")
                self.d=self.speech.recognise()
                print(self.d )
                if self.d=='yes':
                    self.post=mail._email_(self.rec)
                    mouth.say("What is the Subject : ")
                    self.subject=self.speech.recognise()
                    mouth.say("Please enter the body : ")
                    self.body=self.speech.recognise()
                    mouth.say("Do you want to send attachment ?")
                    self.t=self.speech.recognise()
                    if self.t=='no':
                        self.message=f'Subject: {self.subject}\n\n {self.body}'
                        try:
                            self.post.send_simple_mail(self.message)
                            mouth.say("Message Sent")
                            self.ask()
                        except:
                            mouth.say("Improper Connection.")
                            self.ask()
                    elif self.t == 'yes':
                        mouth.say("Please type your attchment address in your computer .")
                        self.file = input("Enter Address : ")
                        try:
                            self.post.send_complex_mail(self.subject, self.body, self.file)
                            mouth.say("Message sent")
                            self.ask()
                        except:
                            mouth.say("Improper Connection.")
                            self.ask()
                else:
                    mouth.say("Please type user's email :")
                    self.rec=input()
                    self.post=mail._email_(self.rec)
                    mouth.say("What is the Subject : ")
                    self.subject=self.speech.recognise()
                    mouth.say("Please enter the body : ")
                    self.body=self.speech.recognise()
                    mouth.say("Do you want to send attachment ?")
                    self.t=self.speech.recognise()
                    if self.t=='no':
                        self.message=f'Subject: {self.subject}\n\n {self.body}'
                        self.post.send_simple_mail(self.message)
                        self.ask()
                    elif self.t == 'yes':
                        mouth.say("Please type your attchment address in your computer .")
                        self.file = input("Enter Address : ")
                        try:
                            self.post.send_complex_mail(self.subject, self.body, self.file)
                            mouth.say("Message sent")
                            self.ask()
                        except:
                            mouth.say("Improper Connection.")
                            self.ask()
            if "movie" in speech_data or "film" in speech_data or "cinema" in speech_data:
                if "in" in speech_data:
                    self.city=""
                    self.x=speech_data.index("in")
                    for i in range(self.x+1+2, len(speech_data)):
                        self.city+=speech_data[i]
                    print(self.city)
                    self.booke=movie.show(self.city)
                    try:
                        self.result=self.booke.getshow()
                        mouth.say("Movies are : ")
                        print(self.result)
                        self.ask()
                    except Exception as e:
                        print(e)
                        self.ask()
                else:
                    mouth.say("Which City: ")
                    self.city=self.speech.recognise()
                    self.booke=movie.show(self.city)
                    try:
                        self.result=self.booke.getshow()
                        mouth.say("Movies are : ")
                        print(self.result)
                        self.ask()
                    except Exception as e:
                        print(e)
                        self.ask()
            if "what" in speech_data or "who" in speech_data or "why" in speech_data or "which" in speech_data or "where" in speech_data:
                self.result=self.ai.search(speech_data)
                mouth.say(self.result)
                self.ask()

            if "wikipedia" in speech_data or "wiki" in speech_data:
                self.result=self.crawl.wiki(speech_data)
                mouth.say(self.result)
            if "translate" in speech_data or "meaning" in speech_data:
                self.tr=temporary.Dummy()
                self.tr.check(speech_data)
                self.result=self.tr.conclude()
                mouth.say(self.result)
                self.ask()
        except Exception as e:
            print(e)
            self.ask()
    def ask(self):
        import random
        self.text=random.choice(self.ask_pattern)
        mouth.say(self.text)
        try:
            self.input=self.speech.recognise()
            print(self.input)
            self.retrive(self.input)
        except:
            mouth.say("Voice Recognition Failed !")
            mouth.say("Try Speaking Again")
            self.ask()



f=Function()
f.ask()
