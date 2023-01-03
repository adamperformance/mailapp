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


type_of_assignment = ["international assignment", "localization"]



def get_values():
    print(f_name.get())
    print(l_name.get())

    print(from_country.current())
    # print(to_country.get())
    # print(start_date.get())
    # print(end_date.get())
    return f_name.get(), l_name.get()



# variables that will be accessed later -- should be declared here,
# should be followed by functions udpating their values
root = Tk()
root.title("Residency")
root.geometry("350x695")
root.config(background="green")

year = 2015
sex = ""
f_name = ""
l_name = ""


def get_year(event):
    year = event.widget.get()

def get_sex(event):
    sex = event.widget.get()
    print(sex)

def get_name(event):

    if event.widget == ".!frame.!labelframe.l_name":
        ln = event.widget
        l_name = ln.get()
    else:
        fn = event.widget
        f_name = fn.get()

    

def ppp():
    print(f_name)
    print(l_name)
    print(sex)

# VERY IMPORTANT FUNCTION!!! gives you all the attributes of the event!
# def eve(event):
#     for attr in dir(event): 
#         print(attr)
#         print(getattr(event, attr))
# **************************************************


f1 = Frame(root, relief=RIDGE, borderwidth=3)
f1.pack(fill=X)
f2 = Frame(root, relief=RIDGE, borderwidth=3)
f2.pack(fill=X)
f3 = Frame(root, relief=RIDGE, borderwidth=3)
f3.pack(fill=X)
f4 = Frame(root, relief=RIDGE, borderwidth=3)
f4.pack(fill=X)
f5 = Frame(root, relief=RIDGE, borderwidth=3)
f5.pack(fill=X)
f6 = Frame(root, relief=RIDGE, borderwidth=3)
f6.pack(fill=X)
f7 = Frame(root, relief=RIDGE, borderwidth=3)
f7.pack(fill=X)



# PERSONAL INFORMATION

pers_info = LabelFrame(f1, text="Personal info")
pers_info.pack(fill=X)

title_label = Label(pers_info, text="Title").grid(row=0, column=0, sticky=W, padx=10)
title_options = ["Ms.","Mr.", "Mrs."]
title = Combobox(pers_info, values=title_options, name="title", width=13)
title.grid(row=0, column=1, sticky=W, padx=10)
title.bind("<<ComboboxSelected>>", get_sex)
f_name_label = Label(pers_info, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
f_name = Entry(pers_info, width=15, name="f_name")
f_name.grid(row=1, column=1, padx=10)
f_name.bind("<KeyRelease>", get_name)
l_name_label = Label(pers_info, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
l_name = Entry(pers_info, width=15, name="l_name")
l_name.grid(row=2, column=1, padx=10)
l_name.bind("<KeyRelease>", get_name)

# ASSIGNMENT INFORMATION

assig_info = LabelFrame(f2, text="Assignment Information")
assig_info.pack(fill=X)

year_label = Label(assig_info, text="Year").grid(row=0, column=0, sticky=W, padx=10)
year_values = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
year_sel = Combobox(assig_info, values=year_values, width=15, name="year")
year_sel.grid(row=0, column=1, sticky=W, padx=10)
year_sel.bind("<<ComboboxSelected>>", get_year)

country_pair = []

def comboselection(Event):
    country_pair.append(Event.widget.get())
    print(country_pair)


from_country_label = Label(assig_info, text="From country", relief="sunken")
from_country_label.grid(row=1, column=0, sticky=W, padx=10)
from_country = Combobox(assig_info, values=countries, width=15, name="f_country")
from_country.grid(row=1, column=1)
from_country.bind("<<ComboboxSelected>>", comboselection)
to_country_label = Label(assig_info, text="To country", relief="sunken")
to_country_label.grid(row=2, column=0, sticky=W, padx=10)
to_country = Combobox(assig_info, values=countries, width=15, name="t_country")
to_country.grid(row=2, column=1, padx=10)
to_country.bind("<<ComboboxSelected>>", comboselection)

assig_label = Label(assig_info, text="Assignment type", relief="groove").grid(row=3, column=0, sticky=W, padx=10)
assig_type = Combobox(assig_info, values=type_of_assignment, width=15, name="assig_type").grid(row=3, column=1)

residency_label = Label(assig_info, text="Residency", relief="groove").grid(row=4, column=0, sticky=W, padx=10)
residency = Combobox(assig_info, width=15, values=country_pair, name="residency").grid(row=4, column=1)

# PERMANENT HOME

permanent_home = LabelFrame(f3, text="Permanent Home")
permanent_home.pack(fill=X)
ph_from_label = Label(permanent_home, text="From").grid(row=0, column=1)
ph_to_label = Label(permanent_home, text="To").grid(row=0, column=2)
ph_home_label = Label(permanent_home, text="Home country").grid(row=1, column=0, sticky=W, padx=10)
ph_host_label = Label(permanent_home, text="Host country").grid(row=2, column=0, sticky=W, padx=10)

ph_home_from_date = DateEntry(permanent_home, name="ph_home_from", year=year, month=1, day=1).grid(row=1, column=1)
ph_home_to_date = DateEntry(permanent_home, name="ph_home_to", year=2022, month=12, day=31).grid(row=1, column=2)
ph_host_from_date = DateEntry(permanent_home, name="ph_host_from", year=2022, month=1, day=1).grid(row=2, column=1)
ph_host_to_date = DateEntry(permanent_home, name="ph_host_to", year=2022, month=12, day=31).grid(row=2, column=2)


# COVI

add_info = LabelFrame(f4, text="Addtional info")
add_info.pack(fill=X)

home_label = Label(add_info, text="Home").grid(row=0, column=1)
host_label = Label(add_info, text="Host").grid(row=0, column=2)
include_label_COVI = Label(add_info, text="Include?").grid(row=0, column=4)
spouse_label =  Label(add_info, text="Spouse").grid(row=1, column=0, sticky=W, padx=10)
children_label =  Label(add_info, text="Children").grid(row=2, column=0, sticky=W, padx=10)
payroll_label = Label(add_info, text="Payroll").grid(row=3, column=0, sticky=W, padx=10)
soc_sec_label = Label(add_info, text="Soc. Sec.").grid(row=4, column=0, sticky=W, padx=10)
assets_label =  Label(add_info, text="Assets").grid(row=5, column=0, sticky=W, padx=10)

spouse_home = Radiobutton(add_info, name="spouse_home").grid(row=1, column=1, padx=10)
spouse_host = Radiobutton(add_info, name="spouse_host").grid(row=1, column=2, padx=10)

include_butt_COVI = Checkbutton(add_info, name="include_COVI").grid(row=1, column=4)

children_home = Checkbutton(add_info).grid(row=2, column=1, padx=10)
children_host = Checkbutton(add_info).grid(row=2, column=2, padx=10)

payroll_home = Checkbutton(add_info).grid(row=3, column=1, padx=10)
payroll_host = Checkbutton(add_info).grid(row=3, column=2, padx=10)
soc_sec_home = Checkbutton(add_info).grid(row=4, column=1, padx=10)
soc_sec_host = Checkbutton(add_info).grid(row=4, column=2, padx=10)
assets_home = Checkbutton(add_info).grid(row=5, column=1, padx=10)
assets_host = Checkbutton(add_info).grid(row=5, column=2, padx=10)

child_num_label = Label(add_info, text="No. of children").grid(row=1, column=3, padx=10)
child_num = Entry(add_info, width=10).grid(row=2, column=3, padx=10)

family_move_label = Label(add_info, text="Family move").grid(row=3,column=3, padx=10)
family_move_date = DateEntry(add_info, width=8).grid(row=4, column=3, padx=10)

# HABITUAL ABODE

hab_abod = LabelFrame(f5, text="Addtional info")
hab_abod.pack(fill=X)

days_home_label = Label(hab_abod, text="Days in Home country").grid(row=0, column=0, sticky=W, padx=10)
days_host_label = Label(hab_abod, text="Days in Host country").grid(row=1, column=0, sticky=W, padx=10)
days_home = Entry(hab_abod, width=10).grid(row=0, column=1, padx=10)
days_host = Entry(hab_abod, width=10).grid(row=1, column=1, padx=10)

include_label_HA = Label(hab_abod, text="Include?").grid(row=0, column=2, padx=10)
include_butt_COVI = Checkbutton(hab_abod).grid(row=1, column=2, padx=10)


# date_label1 = Label(f4, text="Start date")
# start_date = DateEntry(f4)
# 

# date_label2 = Label(f4, text="End date")
# end_date = DateEntry(f4)


# TAXATION
taxation_info = LabelFrame(f6, text="Taxation")
taxation_info.pack(fill=X)

to_from = ["up to","from"]
yes_no = ["yes","no"]
dtt = ["calendar", "12 months"]

include_label_TAX = Label(taxation_info, text="Include?").grid(row=0, column=2, padx=10)
include_butt_TAX = Checkbutton(taxation_info).grid(row=1, column=2, padx=10)

date_to_label = Label(taxation_info, text="Date").grid(row=3, column=0, sticky=W, padx=10)
to_from_label = Label(taxation_info, text="Up to/From").grid(row=4, column=0, sticky=W, padx=10)
days_nonrezi_label = Label(taxation_info, text="Exceed 183 days?").grid(row=1, column=0, sticky=W, padx=10)
dtt_type_label = Label(taxation_info, text="DTT Type").grid(row=2, column=0, sticky=W, padx=10)

days_nonrezi_entry = Combobox(taxation_info, values=yes_no, width=10).grid(row=1, column=1, padx=10)
dtt_type = Combobox(taxation_info, values = dtt, width=10).grid(row=2, column=1, padx=10)
date_to = DateEntry(taxation_info, width=10).grid(row=3, column=1, padx=10)
to_from_sel = Combobox(taxation_info, values=to_from, width=10).grid(row=4, column=1, padx=10)

# dtt_label = Label(taxation_info, text="Calendar year or any 12 month period?")
# dtt_label.pack()
# dtt = ["calendar year", "any 12 months"]
# dtt_type = ""

# dtt_choice = 
# dtt_choice.pack()
# dtt_choice.bind("<<ComboboxSelected>>", comboselection)

# home_days_label = Label(taxation_info, text=dtt_type)
# home_days_label.pack()

#calendar days or any 12 month period?



button = Button(f7, text="Generate", command=ppp)
button.pack(fill=BOTH)

root.mainloop()