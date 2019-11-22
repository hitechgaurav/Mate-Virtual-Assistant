try:
    from yandex.Translater import Translater
except:
    print("Import Module Failed.")

class Translate:
    def __init__(self):
        self.tin=Translater()
        self.tin.set_key("#your yandex id here")
    def translate(self,text,target):
        try:
            self.tin.set_to_lang(target)
            self.tin.set_text(text)
            self.tin.set_from_lang(self.tin.detect_lang())
            self.r=self.tin.translate()
            return self.r
        except:
            print("Translate Failed.")
