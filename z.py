from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry



root = Tk()
root.title("Residency")
root.geometry("350x450")
root.config(background="yellow")

notebook = ttk.Notebook(root, width=300)
notebook.place(relx=0.5, rely=0.01, anchor=N)

first = PanedWindow(root, orient=VERTICAL)
first.pack()

second = Frame(root)
second.pack()

notebook.add(first, text="Paned")
notebook.add(second, text="Frame")

frame_left = Frame(first)
frame_left.pack(side=LEFT)

frame_right = Frame(first)
frame_right.pack(side=RIGHT)

eee = Entry(frame_left)
eee.pack()

fff = Button(frame_right)
fff.pack()

v = ["yes", "no", "maybe"]

ggg = Combobox(frame_right, values=v)
ggg.pack()

root.mainloop()