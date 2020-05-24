# import tkinter as tk 
# r = tk.Tk() 
# r.title('Counting Seconds') 
# button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
# button.pack() 
# r.mainloop() 

import tkinter
from tkinter import Button
window = tkinter.Tk()
#To rename the title of the window
window.title("GUI")
#pack is used to show the object in the window
label = tkinter.Label(window, text="Hello World!", font=("Arial Bold",50))

window.geometry('350x200')

label.grid(column=0, row=0)

def clicked():
    label.configure(text="Button was clicked")

bt= Button (window, text="Enter", command=clicked)
bt.grid(column=1, row=0)

window.mainloop()