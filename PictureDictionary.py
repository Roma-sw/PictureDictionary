import tkinter as tk
from tkinter import ttk
from googletrans import Translator
import webbrowser
import os
import re
import urllib
import requests

def changePage(page):
    page.tkraise()

def main() -> None:
    def trans(word):
        global translated_text
        global tex
        translator = Translator()
        tex = word.get()
        text_trans = translator.translate(tex, src='en', dest='ja')
        translated_text = text_trans.text
        print(translated_text)
        page = result()
        page.tkraise()

    def result():
        # result page
        global translated_text
        global tex
        resultPage = tk.Frame(base)

        spaceLabel1 = [tk.Label(resultPage, text="") for column in range(3)]
        spaceLabel2 = [tk.Label(resultPage, text="") for column in range(3)]

        titleFont  = ("Helevetice", 18) 
        title =\
            ttk.Label(resultPage, text=translated_text, font=titleFont)

        for index in range(3):
            spaceLabel1[index].pack()
        title.pack()
        frame = ttk.Frame(resultPage)
        frame.pack()
        #open browser
        query = tex
        url = "https://www.google.co.jp/search?q="+query+"&source=lnms&tbm=isch"
        webbrowser.open(url, 0)

        for index in range(3):
            spaceLabel2[index].pack()
        # button
        againButton = ttk.Button(frame, text="           AGAIN          ", command=lambda : changePage(mainPage))
        againButton.pack()
        quitButton = ttk.Button(frame, text="           QUIT          ", command=base.quit)
        quitButton.pack()

        resultPage.grid(row=0, column=0, sticky="nsew")

        resultPage.grid(row=0, column=0, sticky="nsew")

        mainPage.tkraise()
        
        return resultPage



    base = tk.Tk()
    base.geometry('800x600')
    base.title('PictureDictionary')

    base.grid_rowconfigure(0, weight=1)
    base.grid_columnconfigure(0, weight=1)

    #main page
    mainPage = tk.Frame(base)

    spaceLabel1 = [tk.Label(mainPage, text="") for column in range(5)]

    titleFont  = ("Helevetice", 18)
    title =\
        ttk.Label(mainPage, text="Enter the word you wanna look up", font=titleFont)
    for index in range(5):
        spaceLabel1[index].pack()
    title.pack()
    frame = ttk.Frame(mainPage)
    frame.pack()

    spaceLabel2 = [tk.Label(frame, text="") for column in range(3)]
    for index in range(3):
        spaceLabel2[index].grid(row=index, column=0)

    word = tk.StringVar()
    word_entry = ttk.Entry(frame, textvariable=word, width=30)

    word_entry.grid(row=4, column=1)

    searchButton = ttk.Button(frame, text="  LOOK UP!  ", command=lambda : trans(word_entry))

    searchButton.grid(row=4, column=3)

    mainPage.grid(row=0, column=0, sticky="nsew")

    base.mainloop()

if __name__ == "__main__":
    main()