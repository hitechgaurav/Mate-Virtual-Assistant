try:
    import requests
    import time
    import re
    from bs4 import BeautifulSoup
except Exception as e:
    print(e)
class show:
    def __init__(self, city):
        self.city=city
        self.link="https://in.bookmyshow.com/"+city+"/movies"

    def getshow(self):
        input=requests.get(self.link)
        page=input.content
        #print(page)
        soup=BeautifulSoup(page)
        x = str(soup.find_all('div',{'class':'card-title'}))
        content = str(re.sub("<.*?>","",x))
        return content

