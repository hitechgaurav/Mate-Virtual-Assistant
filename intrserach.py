import wikipedia
import webbrowser
class InternetSearch:
    def wiki(self,query):
        try:
            self.result=wikipedia.summary(query,sentences=20)
            return self.result
        except:
            print("Sorry! Try Searching Again")
    def google(self,query):
        try:
            webbrowser.open("https:\\www.google.com\\search?q="+query)
        except:
            print("Browser Error")
