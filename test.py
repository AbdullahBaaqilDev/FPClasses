import tkinter as tk
from tkinter import ttk
from colorama import *
from pytube import*
ins=tk.Tk()
ins.title('DOWNLOAD')
ins.geometry('450x250+700+250')
ins.resizable(False,False)
ins.config(background='black')


en1=tk.Entry(ins,width=70)
en1.place(x=14,y=100)


def down1(url):
    YouTube(url).streams.get_audio_only().download('D:\DOWNLOAD PYTUBE')

def down2(url):
    YouTube(url).streams.get_lowest_resolution().download('D:\DOWNLOAD PYTUBE')

def search(url):
    video = YouTube(url)
    resolutions = []
    for stream in video.streams:
        resolutions.append(stream.resolution)
    
    q.config(values = resolutions)

b1=tk.Button(
    ins,
    text='AUDIO',
    width=10,
    height=0,
    font=10,
    fg='black',
    bg='green',
    command=lambda:down1(en1.get())
    )
b1.place(x=225,y=150)

b2=tk.Button(
    ins,
    text='VIDEO',
    width=10,
    height=0,
    font=10,
    fg='black',
    bg='red',
    command=lambda:down2(en1.get())
    )
b2.place(x=125,y=150)

b_search = tk.Button(
    ins,
    text='Search',
    width=10,
    height=0,
    font=10,
    fg='black',
    bg='Yellow',
    command = lambda:search(en1.get())
    )
b_search.pack()



q = ttk.Combobox(
    ins,
    values = [""]
)
q.pack()

le1=tk.Label(text='DOWNLOAD YOUTUBE @YAN',bg='black',fg='red',font=10)
le1.place(x=118,y=50)

ins.mainloop()