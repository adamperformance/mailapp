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

# VERY IMPORTANT FUNCTION!!! gives you all the attributes of the event!
# def eve(event):
#     for attr in dir(event): 
#         print(attr)
#         print(getattr(event, attr))
# **************************************************



# VARIABLES USED THROUGHOUT THE PROGRAM
    # variables that will be accessed later in the program are declared here
    # should be followed by functions udpating their values

title = ""
f_name = ""
l_name = ""
year = ""
home_country = ""
host_country = ""
assignment_type = ""

PH_home_f = ""
PH_home_t = ""
PH_host_f = ""
PH_host_t = ""
family_move = ""
tax_date = ""

child_number = ""

host_days = ""
home_days = ""

exceed183 = ""
type_of_DTT = ""
up_from = ""


country_pair = []
to_from = ["up to","from"]
yes_no = ["yes","no"]
dtt = ["calendar", "12 months"]
cp = ["",""]


# FUNCTIONS USED THROUGHOUT THE PROGRAM

def get_entry_value(event):
    if event.widget == root.nametowidget(".!frame.!labelframe.l_name"):
        l_name = event.widget.get()
        l_name = l_name.strip()
        print(l_name)
    elif event.widget == root.nametowidget(".!frame.!labelframe.f_name"):
        f_name = event.widget.get()
        f_name = f_name.strip()
        print(f_name)
    elif event.widget == root.nametowidget(".!frame3.!labelframe.childnum"):
        child_number = event.widget.get()
        print(child_number)
    elif event.widget == root.nametowidget(".!frame4.!labelframe.days_home"):
        home_days = event.widget.get()
        print(home_days)
    elif event.widget == root.nametowidget(".!frame4.!labelframe.days_host"):
        host_days = event.widget.get()
        print(host_days)

def get_date(event):
    if event.widget == root.nametowidget(".f3.ph_label.!dateentry"):
        PH_home_f = event.widget.get()
        print(PH_home_f)
    elif event.widget == root.nametowidget(".f3.ph_label.!dateentry2"):
        PH_home_t = event.widget.get()
        print(PH_home_t)
    elif event.widget == root.nametowidget(".f3.ph_label.!dateentry3"):
        PH_host_f = event.widget.get()
        print(PH_host_f)
    elif event.widget == root.nametowidget(".f3.ph_label.!dateentry4"):
        PH_host_t = event.widget.get()
        print(PH_host_t)
    elif event.widget == root.nametowidget(".!frame3.!labelframe.!dateentry"):
        family_move = event.widget.get()
        print(family_move)
    elif event.widget == root.nametowidget(".!frame5.!labelframe.!dateentry"):
        tax_date = event.widget.get()
        print(tax_date)
    
def comboselection(event):

    if event.widget == root.nametowidget(".!frame.!labelframe.title"):
        title = event.widget.get()
        print(title)
    elif event.widget == root.nametowidget(".!frame2.!labelframe.year"):
        year = event.widget.get()
        print(year)
    elif event.widget == root.nametowidget(".!frame2.!labelframe.assig_type"):
        assignment_type = event.widget.get()
        print(assignment_type)
    elif event.widget == root.nametowidget(".!frame5.!labelframe.!combobox"):
        exceed183 = event.widget.get()
        print(exceed183)
    elif event.widget == root.nametowidget(".!frame5.!labelframe.!combobox2"):
        type_of_DTT = event.widget.get()
        print(type_of_DTT)
    elif event.widget == root.nametowidget(".!frame5.!labelframe.!combobox3"):
        up_from = event.widget.get()
        print(up_from)
    elif event.widget == root.nametowidget(".!frame2.!labelframe.f_country") or root.nametowidget(".!frame2.!labelframe.t_country"):
        if len(country_pair) < 2:
            country_pair.append(event.widget.get())
        else:
            print(event.widget)
            if event.widget == root.nametowidget(".!frame2.!labelframe.f_country"):
                country_pair[0] = event.widget.get()
                home_country = event.widget.get()
            elif event.widget == root.nametowidget(".!frame2.!labelframe.t_country"):
                country_pair[1] = event.widget.get()
                host_country = event.widget.get()
        
        print(country_pair)


def combobox_values():
    for i in range(len(country_pair)):
        cp[i] = country_pair[i]
    return cp

def db_refresh(event):
    residency['values'] = combobox_values()


def get_radio(value):
    spouse = value
    print(spouse)


def include_parts(event):
    include = event.widget.get()
    print(include)

def include_checked():
    include1 = incl_COVI.get()
    include2 = incl_HA.get()
    include3 = incl_TAX.get()

    print(include1)
    print(include2)
    print(include3)

def print_all():
    print(title)
    print(f_name)
    print(l_name)
    print(year)
    print(home_country)
    print(host_country)
    print(assignment_type)

    print(PH_home_f)
    print(PH_home_t)
    print(PH_host_f)
    print(PH_host_t)
    print(family_move)
    print(tax_date)
    print(child_number)

    print(host_days)
    print(home_days)

    print(exceed183)
    print(type_of_DTT)
    print(up_from)


# GUI CREATION

root = Tk()
root.title("Residency")
root.geometry("350x695")
root.config(background="green")

# TK variable declaration
cp = StringVar()
incl_COVI = StringVar()
incl_COVI.set(False)
incl_HA = StringVar()
incl_HA.set(False)
incl_TAX = StringVar()
incl_TAX.set(False)
COVI_spouse = StringVar()
COVI_children = StringVar()
COVI_payroll = StringVar()
COVI_socsec = StringVar()
COVI_assets = StringVar()

f1 = Frame(root, relief=RIDGE, borderwidth=3)
f1.pack(fill=X)
f2 = Frame(root, relief=RIDGE, borderwidth=3)
f2.pack(fill=X)
f3 = Frame(root, relief=RIDGE, borderwidth=3, name="f3")
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
title.bind("<<ComboboxSelected>>", comboselection)
f_name_label = Label(pers_info, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
f_name = Entry(pers_info, width=15, name="f_name")
f_name.grid(row=1, column=1, padx=10)
f_name.bind("<KeyRelease>", get_entry_value)
l_name_label = Label(pers_info, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
l_name = Entry(pers_info, width=15, name="l_name")
l_name.grid(row=2, column=1, padx=10)
l_name.bind("<KeyRelease>", get_entry_value)

# ASSIGNMENT INFORMATION

assig_info = LabelFrame(f2, text="Assignment Information")
assig_info.pack(fill=X)

year_label = Label(assig_info, text="Year").grid(row=0, column=0, sticky=W, padx=10)
year_values = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
year_sel = Combobox(assig_info, values=year_values, width=15, name="year")
year_sel.grid(row=0, column=1, sticky=W, padx=10)
year_sel.bind("<<ComboboxSelected>>", comboselection)


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
assig_type = Combobox(assig_info, values=type_of_assignment, width=15, name="assig_type")
assig_type.grid(row=3, column=1)
assig_type.bind("<<ComboboxSelected>>", comboselection)


residency_label = Label(assig_info, text="Residency", relief="groove").grid(row=4, column=0, sticky=W, padx=10)
residency = Combobox(assig_info, width=15, name="residency")
residency.grid(row=4, column=1)
residency["values"] = combobox_values()
residency.bind('<Button>', lambda event: db_refresh(event))


# PERMANENT HOME

permanent_home = LabelFrame(f3, text="Permanent Home", name="ph_label")
permanent_home.pack(fill=X)
ph_from_label = Label(permanent_home, text="From").grid(row=0, column=1)
ph_to_label = Label(permanent_home, text="To").grid(row=0, column=2)
ph_home_label = Label(permanent_home, text="Home country").grid(row=1, column=0, sticky=W, padx=10)
ph_host_label = Label(permanent_home, text="Host country").grid(row=2, column=0, sticky=W, padx=10)

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

include_butt_COVI = Checkbutton(add_info, name="include_COVI", variable=incl_COVI, onvalue="Yes", offvalue="No", command=include_checked)
include_butt_COVI.grid(row=1, column=4)

spouse_home = Checkbutton(add_info, variable=COVI_spouse, onvalue="spouse_home", offvalue="", command=lambda: get_radio(COVI_spouse.get()))
spouse_home.grid(row=1, column=1, padx=10)

spouse_host = Checkbutton(add_info, variable=COVI_spouse, onvalue="spouse_host", offvalue="", command=lambda: get_radio(COVI_spouse.get()))
spouse_host.grid(row=1, column=2, padx=10)

children_home = Checkbutton(add_info, variable=COVI_children, onvalue="children_home", offvalue="", command=lambda: get_radio(COVI_children.get()))
children_home.grid(row=2, column=1, padx=10)
children_host = Checkbutton(add_info, variable=COVI_children, onvalue="children_host", offvalue="", command=lambda: get_radio(COVI_children.get()))
children_host.grid(row=2, column=2, padx=10)

payroll_home = Checkbutton(add_info, variable=COVI_payroll, onvalue="payroll_home", offvalue="", command=lambda: get_radio(COVI_payroll.get()))
payroll_home.grid(row=3, column=1, padx=10)
payroll_host = Checkbutton(add_info, variable=COVI_payroll, onvalue="payroll_host", offvalue="", command=lambda: get_radio(COVI_payroll.get()))
payroll_host.grid(row=3, column=2, padx=10)

soc_sec_home = Checkbutton(add_info, variable=COVI_socsec, onvalue="soc_sec_home", offvalue="", command=lambda: get_radio(COVI_socsec.get()))
soc_sec_home.grid(row=4, column=1, padx=10)
soc_sec_host = Checkbutton(add_info, variable=COVI_socsec, onvalue="soc_sec_host", offvalue="", command=lambda: get_radio(COVI_socsec.get()))
soc_sec_host.grid(row=4, column=2, padx=10)

assets_home = Checkbutton(add_info, variable=COVI_assets, onvalue="assets_home", offvalue="", command=lambda: get_radio(COVI_assets.get()))
assets_home.grid(row=5, column=1, padx=10)
assets_host = Checkbutton(add_info, variable=COVI_assets, onvalue="assets_host", offvalue="", command=lambda: get_radio(COVI_assets.get()))
assets_host.grid(row=5, column=2, padx=10)

child_num_label = Label(add_info, text="No. of children").grid(row=1, column=3, padx=10)
child_num = Entry(add_info, width=10, name="childnum")
child_num.grid(row=2, column=3, padx=10)
child_num.bind("<KeyRelease>", get_entry_value)

family_move_label = Label(add_info, text="Family move").grid(row=3,column=3, padx=10)
family_move_date = DateEntry(add_info, width=8)
family_move_date.grid(row=4, column=3, padx=10)
family_move_date.bind("<<DateEntrySelected>>", get_date)

# HABITUAL ABODE

hab_abod = LabelFrame(f5, text="Addtional info")
hab_abod.pack(fill=X)

include_label_HA = Label(hab_abod, text="Include?").grid(row=0, column=2, padx=10)
include_butt_HA = Checkbutton(hab_abod, variable=incl_HA, onvalue="Yes", offvalue="No", command=include_checked)
include_butt_HA.grid(row=1, column=2, padx=10)

days_home_label = Label(hab_abod, text="Days in Home country").grid(row=0, column=0, sticky=W, padx=10)
days_host_label = Label(hab_abod, text="Days in Host country").grid(row=1, column=0, sticky=W, padx=10)
days_home = Entry(hab_abod, width=10, name="days_home")
days_home.grid(row=0, column=1, padx=10)
days_home.bind("<KeyRelease>", get_entry_value)
days_host = Entry(hab_abod, width=10, name="days_host")
days_host.grid(row=1, column=1, padx=10)
days_host.bind("<KeyRelease>", get_entry_value)



# date_label1 = Label(f4, text="Start date")
# start_date = DateEntry(f4)

# date_label2 = Label(f4, text="End date")
# end_date = DateEntry(f4)



# TAXATION
taxation_info = LabelFrame(f6, text="Taxation")
taxation_info.pack(fill=X)

include_label_TAX = Label(taxation_info, text="Include?").grid(row=0, column=2, padx=10)
include_butt_TAX = Checkbutton(taxation_info, variable=incl_TAX, onvalue="Yes", offvalue="No", command=include_checked)
include_butt_TAX.grid(row=1, column=2, padx=10)

date_to_label = Label(taxation_info, text="Date").grid(row=3, column=0, sticky=W, padx=10)
to_from_label = Label(taxation_info, text="Up to/From").grid(row=4, column=0, sticky=W, padx=10)
days_nonrezi_label = Label(taxation_info, text="Exceed 183 days?").grid(row=1, column=0, sticky=W, padx=10)
dtt_type_label = Label(taxation_info, text="DTT Type").grid(row=2, column=0, sticky=W, padx=10)

days_nonrezi_entry = Combobox(taxation_info, values=yes_no, width=10)
days_nonrezi_entry.grid(row=1, column=1, padx=10)
days_nonrezi_entry.bind("<<ComboboxSelected>>", comboselection)
dtt_type = Combobox(taxation_info, values = dtt, width=10)
dtt_type.grid(row=2, column=1, padx=10)
dtt_type.bind("<<ComboboxSelected>>", comboselection)
date_to = DateEntry(taxation_info, width=10)
date_to.grid(row=3, column=1, padx=10)
date_to.bind("<<DateEntrySelected>>",get_date)
to_from_sel = Combobox(taxation_info, values=to_from, width=10)
to_from_sel.grid(row=4, column=1, padx=10)
to_from_sel.bind("<<ComboboxSelected>>", comboselection)

button = Button(f7, text="Generate", command=print_all)
button.pack(fill=BOTH)

root.mainloop()