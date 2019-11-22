import translate
import SpeechRecog

class Dummy:
    def __init__(self):
        self.spk=SpeechRecog.Speech()
        self.tr=translate.Translate()
        self.languages={'Azerbaijan': 'az', 'Malayalam': 'ml', 'Albanian': 'sq', 'Maltese': 'mt', 'Amharic': 'am', 'Macedonian': 'mk', 'English': 'en', 'Maori': 'mi', 'Arabic': 'ar', 'Marathi': 'mr', 'Armenian': 'hy', 'Mari': 'mhr', 'Afrikaans': 'af', 'Mongolian': 'mn', 'Basque': 'eu', 'German': 'de', 'Bashkir': 'ba', 'Nepali': 'ne', 'Belarusian': 'be', 'Norwegian': 'no', 'Bengali': 'bn', 'Punjabi': 'pa', 'Burmese': 'my', 'Papiamento': 'pap', 'Bulgarian': 'bg', 'Persian': 'fa', 'Bosnian': 'bs', 'Polish': 'pl', 'Welsh': 'cy', 'Portuguese': 'pt', 'Hungarian': 'hu', 'Romanian': 'ro', 'Vietnamese': 'vi', 'Russian': 'ru', 'Haitian': 'ht', 'Cebuano': 'ceb', 'Galician': 'gl', 'Serbian': 'sr', 'Dutch': 'nl', 'Sinhala': 'si', 'HillMari': 'mrj', 'Slovakian': 'sk', 'Greek': 'el', 'Slovenian': 'sl', 'Georgian': 'ka', 'Swahili': 'sw', 'Gujarati': 'gu', 'Sundanese': 'su', 'Danish': 'da', 'Tajik': 'tg', 'Hebrew': 'he', 'Thai': 'th', 'Yiddish': 'yi', 'Tagalog': 'tl', 'Indonesian': 'id', 'Tamil': 'ta', 'Irish': 'ga', 'Tatar': 'tt', 'Italian': 'it', 'Telugu': 'te', 'Icelandic': 'is', 'Turkish': 'tr', 'Spanish': 'es', 'Udmurt': 'udm', 'Kazakh': 'kk', 'Uzbek': 'uz', 'Kannada': 'kn', 'Ukrainian': 'uk', 'Catalan': 'ca', 'Urdu': 'ur', 'Kyrgyz': 'ky', 'Finnish': 'fi', 'Chinese': 'zh', 'French': 'fr', 'Korean': 'ko', 'Hindi': 'hi', 'Xhosa': 'xh', 'Croatian': 'hr', 'Khmer': 'km', 'Czech': 'cs', 'Laotian': 'lo', 'Swedish': 'sv', 'Latin': 'la', 'Scottish': 'gd', 'Latvian': 'lv', 'Estonian': 'et', 'Lithuanian': 'lt', 'Esperanto': 'eo', 'Luxembourgish': 'lb', 'Javanese': 'jv', 'Malagasy': 'mg', 'Japanese': 'ja', 'Malay': 'ms'}
        self.languages={k.lower():v.lower() for k,v in self.languages.items()}
        self.detectlang=""
        self.detecttext=""
    def check(self, data):
        self.text=data
        self.typet=""
        def slicing():
            for i in range(len(self.text)-1,-1,-1):
                if(ord(self.text[i-len(self.text)])==32):
                    break;
                else:
                    self.typet+=self.text[i-len(self.text)]
            for k in range(len(self.typet)-1,-1,-1):
                self.detectlang+=self.typet[k]

            if "translate" in self.text:
                index=self.text.index(" ")
                for i in range(index+1,len(self.text)):
                    if("in" in self.text[i]+self.text[i+1] and ord(self.text[i-1])==32):
                        break
                    else:
                        self.detecttext+=self.text[i]
            if "meaning of" in self.text:
                index=self.text.index("of")
                index+=2
                for i in range(index+1,len(self.text)):
                    if("in" in self.text[i]+self.text[i+1] and ord(self.text[i-1])==32):
                        break
                    else:
                        self.detecttext+=self.text[i]
        slicing()
    def conclude(self):
        self.result=self.tr.translate(self.detecttext,self.languages.get(self.detectlang))
        return self.result


