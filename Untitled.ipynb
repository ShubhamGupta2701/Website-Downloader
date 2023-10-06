from tkinter import *
import urllib.request
import numpy as np
import pandas as pd
import bs4
import os
import base64

win = Tk()
win.geometry("600x420")
win.title('Website Downloader')
win.call('wm', 'iconphoto', win._w,PhotoImage(file='red.png'))

Label(win,text='Website Downloader is here...',font=('Arial',20,'bold'),bg='lightblue',fg='brown').pack(padx=100,pady=50)
Label(win,text='Enter the link here : ',font=('Calibri',16,'bold'),bg='lightgrey',fg='black').place(x=40,y=140)
weblink = StringVar()
link = Entry(win,width=28,font=16,textvariable=weblink,bd=3).place(x=240,y=140)
def downloader():
    url = urllib.request.urlopen(weblink.get()).read()
    data = bs4.BeautifulSoup(url)
    heading = data.head.title.string
    print("The Name of the Website is : ",heading)
    repr(data)
    for string in data.strings:
        repr(string)
    z = data.prettify()
    try:
        with open("new.html", 'w') as f:
            f.write(data.prettify())  
            print("done")
    except UnicodeEncodeError:
        print("there are non-ascii characters in there")    
    Label(win,text="Download completed...",font=("Arial",18,"bold"),bg="lightyellow",fg="black").place(x=100,y=250)
    Label(win,text="Check out your download video in the folder.....").place(x=100,y=300)


Button(win,text='Download',font=('Impact',20,'bold'),bg='lightgreen',command=downloader).place(x=230,y=200)

win.mainloop()
