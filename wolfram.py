try:
    import wolframalpha
    import webbrowser
    import time
except:
    print("Import Error")

class Query:
    def __init__(self):
        self.client=wolframalpha.Client('#your api id of wolfram here')

    def search(self,text):
        try:
            self.que=text.lower()
            res=self.client.query(self.que)
            self.output=next(res.results).text
            return self.output
        except:
            print("API Connection Poor, Searching the Web.")
            time.sleep(2)
            webbrowser.open_new_tab(self.que)

