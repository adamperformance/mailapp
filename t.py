from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry
from country_list import *

c_tries = dict(countries_for_language('en'))

the_countries = ["Bahamas",
                "Cayman Islands",
                "Central African Republic",
                "Channel Islands",
                "Comoros",
                "Czech Republic",
                "Dominican Republic",
                "Falkland Islands",
                "Gambia",
                "Isle of Man",
                "Ivory Coast",
                "Leeward Islands",
                "Maldives",
                "Marshall Islands",
                "Netherlands",
                "Netherlands Antilles",
                "Philippines",
                "Solomon Islands",
                "Turks & Caicos Islands",
                "United Arab Emirates",
                "United Kingdom",
                "United States",
                "Virgin Islands"]

countries = []

for country in c_tries:
    if c_tries[country] in the_countries:
        countries.append(f"the {c_tries[country]}")
    else:
        countries.append(c_tries[country])


def comboselection(Event):
    country_pair.append(Event.widget.get())
    print(country_pair)

def key():
    eee = root.nametowidget(".f1.residency")


def combobox_values():
    for i in range(len(country_pair)):
        cp[i] = country_pair[i]
    # residency["values"]=cp
    return cp

def db_refresh(event):
    residency['values'] = combobox_values()

root = Tk()
root.title("Residency")
root.geometry("350x450")
root.config(background="yellow")


f1 = Frame(root, relief=RIDGE, borderwidth=3, name="f1")
f1.pack(fill=X)
f2 = Frame(root, relief=RIDGE, borderwidth=3)
f2.pack(fill=X)


country_pair = []
cp = StringVar()
cp = ["",""]

from_country = Combobox(f1, values=countries, width=15, name="f_country")
from_country.grid(row=1, column=1)
from_country.bind("<<ComboboxSelected>>", comboselection)
to_country = Combobox(f1, values=countries, width=15, name="t_country")
to_country.grid(row=2, column=1, padx=10)
to_country.bind("<<ComboboxSelected>>", comboselection)

residency_label = Label(f1, text="Residency").grid(row=4, column=0, sticky=W, padx=10)

name_selected = StringVar()
residency = Combobox(f1, width=15, name="residency", textvariable=name_selected)
residency["values"] = combobox_values()
residency.grid(row=4, column=1)
residency.bind('<FocusIn>', lambda event: db_refresh(event))

button = Button(f2, text="Generate", command=key)
button.pack(fill=BOTH)

root.mainloop()


# from tkinter import *
# from tkinter import ttk

# init_list = ['Mickey', 'Minnie', 'Donald', 'Pluto', 'Goofy']

# def db_values():
#     i = inp_var.get()
#     db_list = [x for x in init_list if i in x]
#     print(db_list)
#     # db['values'] = db_list
#     return db_list

# def db_refresh(event):
#     db['values'] = db_values()

# root = Tk()
# title_label = Label(root, text="Partial string example")
# title_label.grid(column=0, row=0)

# inp_var = StringVar()
# input_box = Entry(root, textvariable=inp_var)
# input_box.grid(column=0, row=1)

# name_selected = StringVar()
# db = ttk.Combobox(root, textvariable=name_selected)
# db['values'] = db_values()
# db.bind('<FocusIn>', lambda event: db_refresh(event))
# db.grid(column=0, row=2, sticky=EW, columnspan=3, padx=5, pady=2)

# root.mainloop()