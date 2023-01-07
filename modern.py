from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry
from country_list import *
from customtkinter import *


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

# VERY IMPORTANT FUNCTION!!! gives you all the attributes of the event!
# def eve(event):
#     for attr in dir(event): 
#         print(attr)
#         print(getattr(event, attr))
# **************************************************



# VARIABLES USED THROUGHOUT THE PROGRAM
    # variables that will be accessed later in the program are declared here
    # should be followed by functions udpating their values

year = ""
sex = ""
f_name = ""
l_name = ""
country_pair = []
to_from = ["up to","from"]
yes_no = ["yes","no"]
dtt = ["calendar", "12 months"]

cp = ["",""]


# FUNCTIONS USED THROUGHOUT THE PROGRAM

def get_values():
    print(f_name.get())
    print(l_name.get())

    print(from_country.current())
    # print(to_country.get())
    # print(start_date.get())
    # print(end_date.get())
    return f_name.get(), l_name.get()

def get_year(event):
    year = event.widget.get()
    print(year)

def get_sex(choice):
    sex = title_tk.get()
    print(sex)

def get_name(event):

    if event.widget == ".!frame.!labelframe.l_name":
        ln = event.widget
        l_name = ln.get()
        l_name = l_name.strip()
        print(l_name)
    else:
        fn = event.widget
        f_name = fn.get()
        f_name = f_name.strip()
        print(f_name)

def get_assig_type(event):
    assignment = event.widget.get()
    print(assignment)

def comboselection(event):
    if len(country_pair) < 2:
        country_pair.append(event.widget.get())
    else:
        print(event.widget)
        if event.widget == root.nametowidget(".!frame2.!labelframe.f_country"):
            country_pair[0] = event.widget.get()
        elif event.widget == root.nametowidget(".!frame2.!labelframe.t_country"):
            country_pair[1] = event.widget.get()
    
    print(country_pair)

def combobox_values():
    for i in range(len(country_pair)):
        cp[i] = country_pair[i]
    return cp

def db_refresh(event):
    residency['values'] = combobox_values()

def get_date(event):
    x = event.widget.get()
    print(x)


def get_days(event):
    days = event.widget.get()
    print(days)


def get_tax_values(event):
    tax_values = event.widget.get()
    print(tax_values)

def include_parts(event):
    include = event.widget.get()
    print(include)

def include_checked():
    include = incl_COVI.get()
    
    print(include)

# GUI CREATION

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

root = CTk()
root.title("Residency")
root.config(background="green")

# TK variable declaration
cp = StringVar()

title_tk = StringVar()

incl_COVI = StringVar()
incl_COVI.set(False)
incl_HA = StringVar()
incl_HA.set(False)
incl_TAX = StringVar()
incl_TAX.set(False)

f0 = CTkFrame(root)
f0.pack(fill=X)
# f1 = CTkFrame(root)
# f1.pack(fill=X)
# f2 = CTkFrame(root)
# f2.pack(fill=X)
f3 = CTkFrame(root)
f3.pack(fill=X)
# f4 = CTkFrame(root)
# f4.pack(fill=X)
# f5 = CTkFrame(root)
# f5.pack(fill=X)
# f6 = CTkFrame(root)
# f6.pack(fill=X)
# f7 = CTkFrame(root)
# f7.pack(fill=X)

# PERSONAL INFORMATION

pers_info = CTkFrame(f0)
pers_info.grid(row=0, column=0)


title_label = CTkLabel(pers_info, text="Title").grid(row=0, column=0, sticky=W, padx=10)
title_options = ["Ms.","Mr.", "Mrs."]
title = CTkComboBox(pers_info, variable=title_tk, values=title_options, command=get_sex)
title.grid(row=0, column=1, sticky=W, padx=10)
# title.bind("<<ComboboxSelected>>", get_sex)
f_name_label = CTkLabel(pers_info, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
f_name = CTkEntry(pers_info, width=140)
f_name.grid(row=1, column=1, padx=10)
f_name.bind("<KeyRelease>", get_name)
l_name_label = CTkLabel(pers_info, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
l_name = CTkEntry(pers_info, width=140)
l_name.grid(row=2, column=1, padx=10)
l_name.bind("<KeyRelease>", get_name)

# # ASSIGNMENT INFORMATION

assig_info = CTkFrame(f0)
assig_info.grid(row=0, column=1)

year_label = CTkLabel(assig_info, text="Year").grid(row=0, column=0, sticky=W, padx=10)
year_values = ["2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025"]
year_sel = CTkComboBox(assig_info, values=year_values)
year_sel.grid(row=0, column=1, sticky=W, padx=10)
year_sel.bind("<<ComboboxSelected>>", get_year)


from_country_label = CTkLabel(assig_info, text="From country")
from_country_label.grid(row=1, column=0, sticky=W, padx=10)
from_country = CTkComboBox(assig_info, values=countries, hover=True)
from_country.grid(row=1, column=1)
from_country.bind("<<ComboboxSelected>>", comboselection)
to_country_label = CTkLabel(assig_info, text="To country")
to_country_label.grid(row=2, column=0, sticky=W, padx=10)
to_country = CTkComboBox(assig_info, values=countries)
to_country.grid(row=2, column=1, padx=10)
to_country.bind("<<ComboboxSelected>>", comboselection)

# assig_label = CTkLabel(assig_info, text="Assignment type", relief="groove").grid(row=3, column=0, sticky=W, padx=10)
# assig_type = CTkComboBox(assig_info, values=type_of_assignment, width=15, name="assig_type")
# assig_type.grid(row=3, column=1)
# assig_type.bind("<<ComboboxSelected>>", get_assig_type)


# residency_label = CTkLabel(assig_info, text="Residency", relief="groove").grid(row=4, column=0, sticky=W, padx=10)
# residency = CTkComboBox(assig_info, width=15, name="residency")
# residency.grid(row=4, column=1)
# residency["values"] = combobox_values()
# residency.bind('<Button>', lambda event: db_refresh(event))


# # PERMANENT HOME

permanent_home = CTkFrame(f3)
permanent_home.pack()
ph_from_label = CTkLabel(permanent_home, text="From").grid(row=0, column=1)
ph_to_label = CTkLabel(permanent_home, text="To").grid(row=0, column=2)
ph_home_label = CTkLabel(permanent_home, text="Home country").grid(row=1, column=0, sticky=W, padx=10)
ph_host_label = CTkLabel(permanent_home, text="Host country").grid(row=2, column=0, sticky=W, padx=10)


ph_home_from_date = DateEntry(permanent_home, name="ph_home_from", year=2015, month=1, day=1)
ph_home_from_date.grid(row=1, column=1)
ph_home_from_date.bind("<<DateEntrySelected>>", get_date)
ph_home_to_date = DateEntry(permanent_home, name="ph_home_to", year=2022, month=12, day=31)
ph_home_to_date.grid(row=1, column=2)
ph_home_to_date.bind("<<DateEntrySelected>>", get_date)
ph_host_from_date = DateEntry(permanent_home, name="ph_host_from", year=2022, month=1, day=1)
ph_host_from_date.grid(row=2, column=1)
ph_host_from_date.bind("<<DateEntrySelected>>", get_date)
ph_host_to_date = DateEntry(permanent_home, name="ph_host_to", year=2022, month=12, day=31)
ph_host_to_date.grid(row=2, column=2)
ph_host_to_date.bind("<<DateEntrySelected>>", get_date)


# # COVI

# add_info = CTkFrame(f4)
# add_info.pack(fill=X)

# home_label = CTkLabel(add_info, text="Home").grid(row=0, column=1)
# host_label = CTkLabel(add_info, text="Host").grid(row=0, column=2)
# include_label_COVI = CTkLabel(add_info, text="Include?").grid(row=0, column=4)
# spouse_label =  CTkLabel(add_info, text="Spouse").grid(row=1, column=0, sticky=W, padx=10)
# children_label =  CTkLabel(add_info, text="Children").grid(row=2, column=0, sticky=W, padx=10)
# payroll_label = CTkLabel(add_info, text="Payroll").grid(row=3, column=0, sticky=W, padx=10)
# soc_sec_label = CTkLabel(add_info, text="Soc. Sec.").grid(row=4, column=0, sticky=W, padx=10)
# assets_label =  CTkLabel(add_info, text="Assets").grid(row=5, column=0, sticky=W, padx=10)

# spouse_home = CTkRadioButton(add_info, name="spouse_home").grid(row=1, column=1, padx=10)
# spouse_host = CTkRadioButton(add_info, name="spouse_host").grid(row=1, column=2, padx=10)


# include_butt_COVI = CTkCheckBox(add_info, name="include_COVI", variable=incl_COVI, onvalue="Yes", offvalue="No", command=include_checked)
# include_butt_COVI.grid(row=1, column=4)


# children_home = CTkCheckBox(add_info).grid(row=2, column=1, padx=10)
# children_host = CTkCheckBox(add_info).grid(row=2, column=2, padx=10)

# payroll_home = CTkCheckBox(add_info).grid(row=3, column=1, padx=10)
# payroll_host = CTkCheckBox(add_info).grid(row=3, column=2, padx=10)
# soc_sec_home = CTkCheckBox(add_info).grid(row=4, column=1, padx=10)
# soc_sec_host = CTkCheckBox(add_info).grid(row=4, column=2, padx=10)
# assets_home = CTkCheckBox(add_info).grid(row=5, column=1, padx=10)
# assets_host = CTkCheckBox(add_info).grid(row=5, column=2, padx=10)

# child_num_label = CTkLabel(add_info, text="No. of children").grid(row=1, column=3, padx=10)
# child_num = CTkEntry(add_info, width=10).grid(row=2, column=3, padx=10)

# family_move_label = CTkLabel(add_info, text="Family move").grid(row=3,column=3, padx=10)
# family_move_date = DateEntry(add_info, width=8).grid(row=4, column=3, padx=10)

# # HABITUAL ABODE

# hab_abod = CTkFrame(f5)
# hab_abod.pack(fill=X)

# include_label_HA = CTkLabel(hab_abod, text="Include?").grid(row=0, column=2, padx=10)
# include_butt_HA = CTkCheckBox(hab_abod, variable=incl_HA, command=include_checked)
# include_butt_HA.grid(row=1, column=2, padx=10)

# days_home_label = CTkLabel(hab_abod, text="Days in Home country").grid(row=0, column=0, sticky=W, padx=10)
# days_host_label = CTkLabel(hab_abod, text="Days in Host country").grid(row=1, column=0, sticky=W, padx=10)
# days_home = CTkEntry(hab_abod, width=10)
# days_home.grid(row=0, column=1, padx=10)
# days_home.bind("<KeyRelease>", get_days)
# days_host = CTkEntry(hab_abod, width=10)
# days_host.grid(row=1, column=1, padx=10)
# days_host.bind("<KeyRelease>", get_days)



# # date_label1 = CTkLabel(f4, text="Start date")
# # start_date = DateEntry(f4)

# # date_label2 = CTkLabel(f4, text="End date")
# # end_date = DateEntry(f4)



# # TAXATION
# taxation_info = CTkFrame(f6)
# taxation_info.pack(fill=X)

# include_label_TAX = CTkLabel(taxation_info, text="Include?").grid(row=0, column=2, padx=10)
# include_butt_TAX = CTkCheckBox(taxation_info, variable=incl_TAX, command=include_checked)
# include_butt_TAX.grid(row=1, column=2, padx=10)

# date_to_label = CTkLabel(taxation_info, text="Date").grid(row=3, column=0, sticky=W, padx=10)
# to_from_label = CTkLabel(taxation_info, text="Up to/From").grid(row=4, column=0, sticky=W, padx=10)
# days_nonrezi_label = CTkLabel(taxation_info, text="Exceed 183 days?").grid(row=1, column=0, sticky=W, padx=10)
# dtt_type_label = CTkLabel(taxation_info, text="DTT Type").grid(row=2, column=0, sticky=W, padx=10)

# days_nonrezi_entry = CTkComboBox(taxation_info, values=yes_no, width=10)
# days_nonrezi_entry.grid(row=1, column=1, padx=10)
# days_nonrezi_entry.bind("<<ComboboxSelected>>", get_tax_values)
# dtt_type = CTkComboBox(taxation_info, values = dtt, width=10)
# dtt_type.grid(row=2, column=1, padx=10)
# dtt_type.bind("<<ComboboxSelected>>", get_tax_values)
# date_to = DateEntry(taxation_info, width=10)
# date_to.grid(row=3, column=1, padx=10)
# to_from_sel = CTkComboBox(taxation_info, values=to_from, width=10)
# to_from_sel.grid(row=4, column=1, padx=10)
# to_from_sel.bind("<<ComboboxSelected>>", get_tax_values)

# button = CTkButton(f7, text="Generate")
# button.pack(fill=BOTH)

root.mainloop()