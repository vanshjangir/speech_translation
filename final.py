#--------------Importing libraries-----------------
from tkinter import *
import speech_recognition as sr
from translate import Translator

#-------------------Backend------------------------

r = sr.Recognizer()

def speech():
     global lbO
     global r
     with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            entry.insert(END , r.recognize_google(audio))
        except:
            entry.insert(END , "could not reconize")


def translate():
    global entry
    global lbT
    global menu1
    global menu2

    lbO.configure(text = str(entry.get()))

    lg = Translator(from_lang = str(menu1.get()), to_lang = str(menu2.get()))
    lbT.configure(text = lg.translate(str(entry.get())))




#-------------------GUI CODE-----------------------


root = Tk()
root.title("Translator")
root.geometry("800x500")
root["background"] = "#4cbfa6"


lbH = Label(root, bg = "#4cbfa6", fg = "#17252a", text = "Translator" , font = ("calibri", 25))
lbH.place(x = 331, y = 50)

entry = Entry(root, bg = "#ffffff", fg = "#17252a",font = ("calibri", 15), width = 54)
entry.place(x = 100, y = 150)

photo = PhotoImage(file = r"C:\Users\This Pc\Desktop\python course project\micicon.png")
photocustom = photo.subsample(10,10)

btn = Button(root, image = photocustom, fg = "#17252a", command = speech)
btn.place(x = 650, y = 150, width = 50, height = 28)

frame1 = Frame(root, borderwidth = 1, bg = "#ffffff")
frame1.place(x = 100, y = 220, height = 200, width = 295)

frame2 = Frame(root, borderwidth = 1, bg = "#ffffff")
frame2.place(x = 405, y = 220, height = 200, width = 295)


menu1 = StringVar()                                                                      
menu1.set("english")
drop1 = OptionMenu(frame1, menu1, "english", "german", "french", "spanish")
drop1.configure(bg = "#4cbfa6" , fg = "#17252a" , font = "calibri" , borderwidth = 1, activebackground = "#4cbfa6")
drop1.place(x = 10, y = 10)

menu2 = StringVar()                                                                      
menu2.set("german")
drop2 = OptionMenu(frame2, menu2, "english", "german", "french", "spanish")
drop2.configure(bg = "#4cbfa6" , fg = "#17252a" , font = "calibri" , borderwidth = 1, activebackground = "#4cbfa6")
drop2.place(x = 10, y = 10)


lbO = Label(frame1, bg = "#ffffff", fg = "#17252a", font = "calibri")
lbO.place(x = 10, y = 50)

lbT = Label(frame2, bg = "#ffffff", fg = "#17252a", font = "calibri")
lbT.place(x = 10, y = 50)


btn1 = Button(frame1, text = "translate", bg = "#4cbfa6", fg = "#17252a", font = "calibri", activebackground = "#4cbfa6", command = translate)
btn1.place(x = 10, y = 150)

btn2 = Button(frame2, text = "change", bg = "#4cbfa6", fg = "#17252a", font = "calibri", activebackground = "#4cbfa6")
btn2.place(x = 10, y = 150)


root.mainloop()

