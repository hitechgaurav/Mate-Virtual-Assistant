try:
    import speech_recognition as sr

except:
    print("Import Module Failed")
class Speech:
    def __init__(self):
        self.r=sr.Recognizer()
        self.mic=sr.Microphone()
    def recognise(self):
        try:
            with self.mic as self.source:
                self.r.pause_threshold=0.5
                print("\nListening...")
                self.r.adjust_for_ambient_noise(self.source)
                self.audio=self.r.listen(self.source)
                self.result=self.r.recognize_google(self.audio)
                self.result=self.result.lower()
                return self.result
        except:
            print("!")
