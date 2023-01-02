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




root = Tk()
root.title("Residency")
root.geometry("350x700")
root.config(background="green")

f1 = Frame(root, relief=RIDGE, borderwidth=3)
f1.pack(fill=X)
f2 = Frame(root, relief=RIDGE, borderwidth=3)
f2.pack(fill=X)
f3 = Frame(root, relief=RIDGE, borderwidth=3)
f3.pack(fill=X)
f4 = Frame(root, relief=RIDGE, borderwidth=3)
f4.pack()
f5 = Frame(root, relief=RIDGE, borderwidth=3)
f5.pack(fill=X)
f6 = Frame(root, relief=RIDGE, borderwidth=3)
f6.pack()
f7 = Frame(root, relief=RIDGE, borderwidth=3)
f7.pack()


pers_info = LabelFrame(f1, text="Personal info")
pers_info.pack(fill=X)

title_label = Label(pers_info, text="Title")
title_label.grid(row=0, column=0, sticky=W, padx=10)
title_options = ["Ms.","Mr.", "Mrs."]
title = Combobox(pers_info, values=title_options, width=13)
title.grid(row=0, column=1, sticky=W, padx=10)
f_name_label = Label(pers_info, text="First Name")
f_name_label.grid(row=1, column=0, sticky=W, padx=10)
l_name_label = Label(pers_info, text="Last Name")
l_name_label.grid(row=2, column=0, sticky=W, padx=10)
f_name = Entry(pers_info, width=15)
f_name.grid(row=1, column=1, padx=10)
l_name = Entry(pers_info, width=15)
l_name.grid(row=2, column=1, padx=10)



assig_info = LabelFrame(f2, text="Assignment Information")
assig_info.pack(fill=X)

year_label = Label(assig_info, text="Year")
year_label.grid(row=0, column=0, sticky=W, padx=10)
year_values = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
year = Combobox(assig_info, values=year_values, width=15)
year.grid(row=0, column=1, sticky=W, padx=10)

country_pair = []

def comboselection(Event):
    country_pair.append(Event.widget.get())
    print(country_pair)


from_country_label = Label(assig_info, text="From country", relief="sunken")
from_country_label.grid(row=1, column=0, sticky=W, padx=10)
from_country = Combobox(assig_info, values=countries, width=15)
from_country.grid(row=1, column=1)
from_country.bind("<<ComboboxSelected>>", comboselection)
to_country_label = Label(assig_info, text="To country", relief="sunken")
to_country_label.grid(row=2, column=0, sticky=W, padx=10)
to_country = Combobox(assig_info, values=countries, width=15)
to_country.grid(row=2, column=1, padx=10)
to_country.bind("<<ComboboxSelected>>", comboselection)

assig_label = Label(assig_info, text="Assignment type", relief="groove")
assig_label.grid(row=3, column=0, sticky=W, padx=10)
assig_type = Combobox(assig_info, values=type_of_assignment, width=15)
assig_type.grid(row=3, column=1)

residency_label = Label(assig_info, text="Residency", relief="groove")
residency_label.grid(row=4, column=0, sticky=W, padx=10)
residency = Combobox(assig_info, width=15)
residency.grid(row=4, column=1)
residency.bind("<<ComboboxSelected>>", residency.config(values=country_pair))

# permanent home


permanent_home = LabelFrame(f3, text="Permanent Home")
permanent_home.pack(fill=X)
ph_from_label = Label(permanent_home, text="From")
ph_from_label.grid(row=0, column=1)
ph_to_label = Label(permanent_home, text="To")
ph_to_label.grid(row=0, column=2)
ph_home_label = Label(permanent_home, text="Home country")
ph_home_label.grid(row=1,column=0)
ph_host_label = Label(permanent_home, text="Host country")
ph_host_label.grid(row=2,column=0)

ph_home_from_date = DateEntry(permanent_home)
ph_home_from_date.grid(row=1, column=1)
ph_home_to_date = DateEntry(permanent_home)
ph_home_to_date.grid(row=1, column=2)
ph_host_from_date = DateEntry(permanent_home)
ph_host_from_date.grid(row=2, column=1)
ph_host_to_date = DateEntry(permanent_home)
ph_host_to_date.grid(row=2, column=2)


# COVI info

add_info = LabelFrame(f5, text="Addtional info")
add_info.pack(fill=X)

add_info_left = Frame(add_info)
# add_info_left.pack(side=LEFT)
add_info_left.grid(row=0, column=0, padx=10)
perm_home_label = Label(add_info_left, text="Permanent Home").pack()
payroll_label = Label(add_info_left, text="Payroll").pack()
soc_sec_label = Label(add_info_left, text="Soc. Sec.").pack()


add_info_center = Frame(add_info)
# add_info_center.pack(side=LEFT)
add_info_center.grid(row=0, column=1, padx=10)
home_label = Label(add_info_center, text="Home")
home_label.pack()


add_info_right = Frame(add_info)
# add_info_right.pack(side=LEFT)
add_info_right.grid(row=0, column=2, padx=10)
host_label = Label(add_info_right, text="Host")
host_label.pack()

perm_home_home = Checkbutton(add_info_center).pack()
perm_home_host = Checkbutton(add_info_right).pack()

payroll_home = Checkbutton(add_info_center).pack()
payroll_host = Checkbutton(add_info_right).pack()
soc_sec_home = Checkbutton(add_info_center).pack()
soc_sec_host = Checkbutton(add_info_right).pack()

# family_info = LabelFrame(f2, text="Family Information")
# family_info.pack(fill=X)

# married_label = Label(family_info, text="Marital status")
# married_label.pack()
# married_info = StringVar()
# married_y = Radiobutton(family_info, variable=married_info, value="Y", text="Yes")
# married_y.pack()
# married_n = Radiobutton(family_info, variable=married_info, value="N", text="No")
# married_n.pack()
# children_label = Label(family_info, text="Number of children")
# children_label.pack()
# num_children = Entry(family_info)
# num_children.pack()
# fam_move_label = Label(family_info, text="Family move date")
# fam_move_label.pack()
# fam_move_date = DateEntry(family_info)
# fam_move_date.pack()


# date_label1 = Label(f4, text="Start date").pack(side=LEFT)
# start_date = DateEntry(f4)
# start_date.pack(side=LEFT)

# date_label2 = Label(f4, text="End date").pack(side=LEFT)
# end_date = DateEntry(f4).pack(side=LEFT)





home_comp_info = LabelFrame(f6, text="Home country info")
home_comp_info.pack()
dtt_label = Label(home_comp_info, text="Calendar year or any 12 month period?")
dtt_label.pack()
dtt = ["calendar year", "any 12 months"]

dtt_type = ""


dtt_choice = Combobox(home_comp_info, values = dtt)
dtt_choice.pack()
dtt_choice.bind("<<ComboboxSelected>>", comboselection)

home_days_label = Label(home_comp_info, text=dtt_type)
home_days_label.pack()

#calendar days or any 12 month period?



button = Button(f7, text="Generate", command=get_values)
button.pack()

root.mainloop()