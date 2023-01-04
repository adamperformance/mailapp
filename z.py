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


root = Tk()
root.title("Residency")
root.geometry("350x450")
root.config(background="yellow")

date = "20"
sel = StringVar()

def ppp():
    t = root.nametowidget("f3.ph.!dateentry")
    # for key in t.keys():
    #     print(key)
    x = root.nametowidget("f3.ph.!calendar")
    sel.set(f"1/1/{date}")


f3 = Frame(root, relief=RIDGE, borderwidth=3, name="f3")
f3.pack(fill=X)
frame = Frame(root, relief=RIDGE, borderwidth=3)
frame.pack(fill=X)

# PERMANENT HOME

permanent_home = LabelFrame(f3, text="Permanent Home", name="ph")
permanent_home.pack(fill=X)

ph_from_label = Label(permanent_home, text="From")
ph_from_label.grid(row=0, column=0)

ph_home_from_date = DateEntry(permanent_home, textvariable = sel, selectmode="day", year = 2000)
ph_home_from_date.grid(row=1, column=0)
ph_home_to_date = Calendar(permanent_home, year = 2030)
ph_home_to_date.grid(row=1, column=1)

button = Button(frame, text="Button", command=ppp)
button.pack()



f1 = Frame(root, relief=RIDGE, borderwidth=3, name="f1")
f1.pack(fill=X)
f2 = Frame(root, relief=RIDGE, borderwidth=3)
f2.pack(fill=X)


country_pair = []
cp = StringVar()


def comboselection(Event):
    country_pair.append(Event.widget.get())
    print(country_pair)

def key():
    eee = root.nametowidget(".f1.residency")
    cp.set(country_pair)

def combobox_values():
    for i in range(len(country_pair)):
        cp[i] = country_pair[i]
    residency["values"]=cp
    return cp

from_country = Combobox(f1, values=countries, width=15, name="f_country")
from_country.grid(row=1, column=1)
from_country.bind("<<ComboboxSelected>>", comboselection)
to_country = Combobox(f1, values=countries, width=15, name="t_country")
to_country.grid(row=2, column=1, padx=10)
to_country.bind("<<ComboboxSelected>>", comboselection)

residency_label = Label(f1, text="Residency", relief="groove").grid(row=4, column=0, sticky=W, padx=10)
residency = Combobox(f1, width=15, name="residency")
residency["values"] = combobox_values()
residency.grid(row=4, column=1)


button = Button(f2, text="Generate", command=key)
button.pack(fill=BOTH)

root.mainloop()