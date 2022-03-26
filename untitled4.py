from tkinter import *
import speech_recognition as sr
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("Stuff")
root.geometry("800x700")
root.config(bg="lavender")

title = Label(root, text="Language Translator", bg="lavender", font=("times",20))
label1 = Label(root, text="Enter Text", bg="lavender", font=("times",15))
title.place(relx=0.5,rely=0.1,anchor=CENTER)
label1.place(relx=0.7,rely=0.3,anchor=CENTER)
area = Text(root, bg="lavender",font=("times",13),height=11,width=60,wrap=WORD,padx=5,pady=5,bd=0)
area.place(relx=0.7,rely=0.5,anchor=CENTER)

root.mainloop()