from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('700x350')
root.resizable(0, 0)
root.iconbitmap('src/icon.png')
root['bg'] = 'skyblue'

root.title('Language translator')
Label(root, text="Language Translator", font="Arial 20 bold").pack()

Label(root, text="Enter Text", font="arial 13 bold", bg="white smoke").place(x=100, y=90)
Input_text = Entry(root, width=30)
Input_text.place(x=30, y=130)
Input_text.get()

Label(root, text="Output", font="arial 13 bold", bg="white smoke").place(x=500, y=90)
Output_text = Text(root, font="arial 10", height=5, wrap=WORD, padx=5, pady=5, width=40)
Output_text.place(x=400, y=130)

language = list(LANGUAGES.values())

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=30, y=160)
dest_lang.set("Choose Language")


def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(), dest=dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)


trans_btn = Button(root, text="Translate", font="arial 12 bold", pady=5, command=Translate, bg="orange", activebackground="green", )
trans_btn.place(x=100, y=200)

root.mainloop()
