from tkinter import *
import speech_recognition as sr
from translate import Translator

root = Tk()

def speech_to_text():
    r = sr.Recognizer()

txt = ''

def trans():
    lg = Translator(from_lang = "english", to_lang = menu.get())
    convert = lg.translate(entry1.get())

    lb3 = Label(root, bg = "#00283d", fg = "#84ceeb", text = "dsfjdksf", font = "calibri")
    lb3.place(y = 330, x = 500)
    

root.title("testing tkinter")
root.geometry("1000x1000")
root["background"] = "#00283d"


lb1 = Label(root, bg = "#00283d", fg = "#84ceeb", text = "English", font = "calibri")
lb1.place(x = 400, y = 270)

lb2 = Label(root, bg = "#00283d", fg = "#84ceeb", text = "Language", font = "calibri")
lb2.place(x = 400, y = 300)

entry1 = Entry(root, bg = "#00283d", fg = "#84ceeb", highlightcolor = "#00283d")
entry1.place(x = 500, y = 270)

menu = StringVar()
menu.set("Select")
drop = OptionMenu(root, menu,"german", "french", "spanish")
drop.configure(bg = "#00283d" , fg = "#84ceeb" , font = "calibri" , highlightcolor = "#00283d" , highlightbackground = "#00283d")
drop.place(x = 499, y = 300)

if menu.get() != "Select":
    trans()

root.mainloop()


 
