#--------------Importing libraries-----------------
from tkinter import *
import speech_recognition as sr
from googletrans import Translator

#-------------------Backend------------------------

r = sr.Recognizer()
t = Translator()

def speech():
     global r
     global entry
     global lbO
     global lbT

     entry.delete(0,END)
     with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            entry.insert(END , r.recognize_google(audio))
        except:
            pass


def translate():
    global entry
    global lbT
    global menu1
    global menu2

    O_result = t.translate(str(entry.get()) , dest = str(menu1.get()))
    lbO.configure(text = O_result.text)

    T_result = t.translate(str(entry.get()), src = str(menu1.get()), dest = str(menu2.get()))
    lbT.configure(text = T_result.text)
        

def reset():
    global entry
    global lbO
    global lbT
    entry.delete(0 , END)
    lbO.configure(text = " ")
    lbT.configure(text = " ")



#-------------------GUI CODE-----------------------


root = Tk()
root.title("Translator")
root.geometry("800x500")
root["background"] = "#002349"


lbH = Label(root, bg = "#002349", fg = "#ffffff", text = "Translator" , font = ("calibri", 25))
lbH.place(x = 331, y = 50)

entry = Entry(root, bg = "#ffffff", fg = "#002349",font = ("calibri", 15), width = 54)
entry.place(x = 100, y = 150)

photo = PhotoImage(file = r"C:\Users\This Pc\Desktop\python course project\micicon.png")
photocustom = photo.subsample(10,10)

btn = Button(root, image = photocustom, fg = "#957c3d", command = speech)
btn.place(x = 650, y = 150, width = 50, height = 28)

frame1 = Frame(root, borderwidth = 1, bg = "#ffffff")
frame1.place(x = 100, y = 220, height = 200, width = 295)

frame2 = Frame(root, borderwidth = 1, bg = "#ffffff")
frame2.place(x = 405, y = 220, height = 200, width = 295)


langlist = ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu']
langdic = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}

menu1 = StringVar()                                                                      
menu1.set("english")
drop1 = OptionMenu(frame1, menu1, *langlist)
drop1.configure(bg = "#ffffff" , fg = "#002349" , font = "calibri" , borderwidth = 0)
drop1.place(x = 10, y = 10)

menu2 = StringVar()                                                                      
menu2.set("spanish")
drop2 = OptionMenu(frame2, menu2, *langlist)
drop2.configure(bg = "#ffffff" , fg = "#002349" , font = "calibri" , borderwidth = 0)
drop2.place(x = 10, y = 10)


lbO = Label(frame1, bg = "#ffffff", fg = "#002349", font = "calibri")
lbO.place(x = 10, y = 50)

lbT = Label(frame2, bg = "#ffffff", fg = "#002349", font = "calibri")
lbT.place(x = 10, y = 50)


bt = Button(root, text = "translate", bg = "#002349", fg = "#ffffff", font = "calibri", borderwidth = 0, activebackground = "#002349", command = translate)
bt.place(x = 356,y = 430)


root.mainloop()

