from tkinter import *
import tkinter.font as f
import time
from tkinter import messagebox
root = Tk()
root.title("Stop Watch by Akshay")
root.geometry("350x250")
root.config(background="white")

hour = StringVar()
min = StringVar()
second = StringVar()

hour.set("00")
min.set("00")
second.set("00")

hourEntry = Entry(root,width=3,textvariable=hour)
hourEntry.place(x=50,y=50)

minEntry = Entry(root,width=3,textvariable=min)
minEntry.place(x=70,y=50)

secondEntry = Entry(root,width=3,textvariable=second)
secondEntry.place(x=90,y=50)

def submit():
    try:
        temp=int(hour.get())*3600+int(min.get())*60+int(second.get())
    except:
        print("enter the right value")
    while temp>-1:
        mins,seconds = divmod(temp,60)
        hours=00
        if mins>60:
            hours,mins=divmod(mins,60)
        hour.set(hours)
        min.set(mins)
        second.set(seconds)
        root.update()
        time.sleep(1)
        if temp == 0:
            messagebox.showinfo("countdown ends","Time is up!")
        temp=temp-1


btn = Button(root,text="Set stopwatch time",bd="5",command=submit)
btn.place(x=50,y=100)




root.mainloop()