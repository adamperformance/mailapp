from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry
from country_list import *
from cls import Personal_Info, Other_Info

# GUI CREATION
root = Tk()
root.title("Residency")
root.config(background="green")

def valami():
    if check_info.get() == "yes":
        f2.frame1.pack()
    elif check_info.get() == "no":
        f2.frame1.pack_forget()



title_tk = StringVar()
f_name_tk = StringVar()
l_name_tk = StringVar()
check_info = StringVar()

f1 = Personal_Info(root)
f2 = Other_Info(root)
# f2.frame1.pack()

button = Button(root, text="Push me!", command=lambda: f1.get_value())
button.pack()

check = Checkbutton(root, text="Other info?", variable=check_info, onvalue="yes", offvalue="no", command=valami)
check.pack()

root.mainloop()