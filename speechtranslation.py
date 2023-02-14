#--------------------------------------------------------Importing libraries---------------------------------------------------------------
from customtkinter import *
from tkinter import *
import speech_recognition as sr
from googletrans import Translator
from PIL import Image,ImageTk



#---------------------------------------------------------------Backend--------------------------------------------------------------------

# creating obejcts for Transator and Recognizer classes
r = sr.Recognizer()
t = Translator()

# function for taking speech input and converting it into text(english)
def speech():

     textbox.delete("0.0" , "end")
     with sr.Microphone() as source: # using microphone as input
        audio = r.listen(source)

        try:
            textbox.insert(END , r.recognize_google(audio)) # updating recognized text in textbox
        except:
            textbox.insert(END , "try again")



# function for translation in different langauges
def translate():


    # translating textbox text form langauge in menu1 to language in menu2
    T_result = t.translate(str(textbox.get("0.0" , "end")), src = str(menu1.get()), dest = str(menu2.get()))         

    # updating text in Text widget (frame) 
    txt.delete("1.0" , "end") 
    txt.insert(END, T_result.text) 
    print(T_result.text)

#-------------------------------------------------------------GUI CODE---------------------------------------------------------------------


# list of languages
langlist = ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu']


set_appearance_mode("system")
set_default_color_theme("blue")


root = CTk()
root.geometry("800x500")
root.title("Tranlator")

# Title label
lbT = CTkLabel(master = root, text = "Translator", font = ("cascadia code", 25))
lbT.place(x = 330, y = 50)


# dropdown menus for languages
menu1 = CTkOptionMenu(master = root, values = langlist, width = 295, variable = StringVar(value = "english"), font = ("cascadia code", 15))
menu1.place(x = 85, y = 150)

menu2 = CTkOptionMenu(master = root, values = langlist, width = 295, variable = StringVar(value = "hindi"), font = ("cascadia code", 15))
menu2.place(x = 420, y = 150)


# textbox for providing text
textbox = CTkTextbox(master = root, width = 295, height = 200, font = ("cascadia code", 20), border_width = 1)
textbox.configure(fg_color = root._fg_color)
textbox.place(x = 85, y = 200)


# label in a frame to show translated text
frame = CTkFrame(master = root, width = 295, height = 200, border_width = 1)
frame.place(x = 420, y = 200)

txt = Text(master = frame, font = ("cascadia code", 20), width = 26, height = 4, bg = "#2b2b2b", fg = "#ffffff", borderwidth = 0)
txt.place(x = 10, y = 10)

# importing image to use on microphone button
img = CTkImage(Image.open(r"C:\Users\This Pc\Desktop\python course project\darkmic.jpg") , size = (25,25))
img.configure(fg_color = root._fg_color)


# microphone button to call speech function
btM = CTkButton(master = root, text = "", width = 15, image = img, fg_color = "#242424", hover_color = "#242424", corner_radius = 15,command = speech)
btM.place(x = 90, y = 346)


# translate button to call translate function
btT = CTkButton(master = root, width = 40, text = "translate", font = ("cascadia code", 15), corner_radius = 30, command = translate)
btT.place(x = 160, y = 350)

# main loop of tkinter window
root.mainloop()