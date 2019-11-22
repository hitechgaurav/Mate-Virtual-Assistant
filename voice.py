class Speak:
    def __init__(self):
        try:
            import pyttsx3 as spk
            self.engine=spk.init('sapi5')
            self.voice=self.engine.getProperty('voices')
            self.engine.setProperty('rate',130)
            self.engine.setProperty('volume',1)
            self.engine.setProperty('voice',self.voice[1].id)
        except:
            raise ImportError
            print("Import Settings Failed.")
    def say(self,text):
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()

