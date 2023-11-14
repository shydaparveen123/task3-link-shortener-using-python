import pyshorteners
from tkinter import *

win = Tk()
win.geometry("400x270")
win.configure(bg="pink")
#button
def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)

#label. for entering user url

Label(win,text="Enter your url Link", font="impack 17 bold", bg="black",fg="white"). pack(fill="x")

# entry box
entry1 = Entry(win, font="10",bd=3,width=40)
entry1.pack(pady=30)

# bottom
Button(win, text="Click Me", font= "impack 12 bold",bg="blue", fg="white", width="14",command=short).pack()
# entry
entry2= Entry(win, font="impack 16 bold", bg="pink", width=24,bd=0)
entry2.pack(pady=30)
mainloop()