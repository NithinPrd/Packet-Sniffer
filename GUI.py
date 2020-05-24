import Tkinter as tk

m = tk.Tk()

m.title("Abhishek Packet Tracer")
button = tk.Button(m, text='Intercept', width=25, command=m.destroy)
button.pack()
m.mainloop()
