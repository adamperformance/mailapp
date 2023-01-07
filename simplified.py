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
residency = ""

PH_home_f = ""
PH_home_t = ""
PH_host_f = ""
PH_host_t = ""

spouse_COVI = ""
children_COVI = ""
payroll_COVI = ""
soc_sec_COVI = ""
assets_COVI = ""
family_move = ""
child_number = ""
tax_date = ""

host_days = ""
home_days = ""

exceed183 = ""
type_of_DTT = ""
up_from = ""


country_pair = []
resid_pair = []
to_from = ["up to","from"]
yes_no = ["yes","no"]
dtt = ["calendar", "12 months"]
cp = ["",""]


# FUNCTIONS USED THROUGHOUT THE PROGRAM

def comboselection(event):
    
    if len(country_pair) < 2:
        country_pair.append(event.widget.get())
    else:
        if event.widget == root.nametowidget(".!frame2.!labelframe.!combobox2"):
            country_pair[0] = event.widget.get()
        elif event.widget == root.nametowidget(".!frame2.!labelframe.!combobox3"):
            country_pair[1] = event.widget.get()

def combobox_values():
    for i in range(len(country_pair)):
        cp[i] = country_pair[i]
    return cp

def db_refresh(event):
    residency_box['values'] = combobox_values()


def print_all():
    title = title_tk.get()
    f_name = f_name_tk.get()
    l_name = l_name_tk.get()
    year = year_tk.get()
    home_country = home_country_tk.get()
    host_country = host_country_tk.get()
    assignment_type = assignment_type_tk.get()
    residency = residency_tk.get()
    PH_home_f = PH_home_f_tk.get()
    PH_home_t = PH_home_t_tk.get()
    PH_host_f = PH_host_f_tk.get()
    PH_host_t = PH_host_t_tk.get()
    spouse_COVI = COVI_spouse.get()
    children_COVI = COVI_children.get()
    payroll_COVI = COVI_payroll.get()
    soc_sec_COVI = COVI_socsec.get()
    assets_COVI = COVI_assets.get()
    family_move = family_move_tk.get()
    child_number = child_number_tk.get()
    tax_date = tax_date_tk.get()
    home_days = home_days_tk.get()
    host_days = host_days_tk.get()
    exceeds183 = exceed183_tk.get()
    type_of_DTT = type_of_DTT_tk.get()
    up_from = up_from_tk.get()

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
    print(spouse_COVI)
    print(children_COVI)
    print(payroll_COVI)
    print(soc_sec_COVI)
    print(assets_COVI)
    print(child_number)
    print(family_move)
    print(tax_date)
    print(host_days)
    print(home_days)
    print(exceeds183)
    print(type_of_DTT)
    print(up_from)



# GUI CREATION
root = Tk()
root.title("Residency")
root.geometry("350x695")
root.config(background="green")

# TK variable declaration
# cp = StringVar()

title_tk = StringVar()
f_name_tk = StringVar()
l_name_tk = StringVar()

year_tk = StringVar()
home_country_tk = StringVar()
host_country_tk = StringVar()
assignment_type_tk = StringVar()
residency_tk = StringVar()

PH_home_f_tk = StringVar()
PH_home_t_tk = StringVar()
PH_host_f_tk = StringVar()
PH_host_t_tk = StringVar()

COVI_spouse = StringVar()
COVI_children = StringVar()
COVI_payroll = StringVar()
COVI_socsec = StringVar()
COVI_assets = StringVar()
child_number_tk = StringVar()
family_move_tk = StringVar()

tax_date_tk = StringVar()

host_days_tk = StringVar()
home_days_tk = StringVar()
exceed183_tk = StringVar()
type_of_DTT_tk = StringVar()
up_from_tk = StringVar()


incl_COVI = StringVar()
incl_COVI.set(False)
incl_HA = StringVar()
incl_HA.set(False)
incl_TAX = StringVar()
incl_TAX.set(False)


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
title = Combobox(pers_info, textvariable = title_tk, values=title_options, width=13)
title.grid(row=0, column=1, sticky=W, padx=10)
f_name_label = Label(pers_info, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
f_name = Entry(pers_info, width=15, textvariable=f_name_tk)
f_name.grid(row=1, column=1, padx=10)
l_name_label = Label(pers_info, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
l_name = Entry(pers_info, width=15, textvariable=l_name_tk)
l_name.grid(row=2, column=1, padx=10)


# ASSIGNMENT INFORMATION

assig_info = LabelFrame(f2, text="Assignment Information")
assig_info.pack(fill=X)

year_label = Label(assig_info, text="Year").grid(row=0, column=0, sticky=W, padx=10)
year_values = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
year_sel = Combobox(assig_info, textvariable=year_tk, values=year_values, width=15)
year_sel.grid(row=0, column=1, sticky=W, padx=10)


from_country_label = Label(assig_info, text="From country", relief="sunken")
from_country_label.grid(row=1, column=0, sticky=W, padx=10)
from_country = Combobox(assig_info, textvariable=home_country_tk, values=countries, width=15)
from_country.grid(row=1, column=1)
from_country.bind("<<ComboboxSelected>>", comboselection)
to_country_label = Label(assig_info, text="To country", relief="sunken")
to_country_label.grid(row=2, column=0, sticky=W, padx=10)
to_country = Combobox(assig_info, textvariable=host_country_tk, values=countries, width=15)
to_country.grid(row=2, column=1, padx=10)
to_country.bind("<<ComboboxSelected>>", comboselection)

assig_label = Label(assig_info, text="Assignment type", relief="groove").grid(row=3, column=0, sticky=W, padx=10)
assig_type = Combobox(assig_info, textvariable=assignment_type_tk, values=type_of_assignment, width=15)
assig_type.grid(row=3, column=1)


residency_label = Label(assig_info, text="Residency", relief="groove").grid(row=4, column=0, sticky=W, padx=10)
residency_box = Combobox(assig_info, textvariable=residency_tk, width=15)
residency_box.grid(row=4, column=1)
residency_box["values"] = combobox_values()
residency_box.bind('<Button>', lambda event: db_refresh(event))


# PERMANENT HOME

permanent_home = LabelFrame(f3, text="Permanent Home", name="ph_label")
permanent_home.pack(fill=X)
ph_from_label = Label(permanent_home, text="From").grid(row=0, column=1)
ph_to_label = Label(permanent_home, text="To").grid(row=0, column=2)
ph_home_label = Label(permanent_home, text="Home country").grid(row=1, column=0, sticky=W, padx=10)
ph_host_label = Label(permanent_home, text="Host country").grid(row=2, column=0, sticky=W, padx=10)

ph_home_from_date = DateEntry(permanent_home, textvariable=PH_home_f_tk, year=2022, month=1, day=1)
ph_home_from_date.grid(row=1, column=1)
ph_home_to_date = DateEntry(permanent_home, textvariable=PH_home_t_tk, year=2022, month=12, day=31)
ph_home_to_date.grid(row=1, column=2)
ph_host_from_date = DateEntry(permanent_home, textvariable=PH_host_f_tk, year=2022, month=1, day=1)
ph_host_from_date.grid(row=2, column=1)
ph_host_to_date = DateEntry(permanent_home, textvariable=PH_host_t_tk, year=2022, month=12, day=31)
ph_host_to_date.grid(row=2, column=2)


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

include_butt_COVI = Checkbutton(add_info, name="include_COVI", variable=incl_COVI, onvalue="Yes", offvalue="No")
include_butt_COVI.grid(row=1, column=4)

spouse_home = Checkbutton(add_info, variable=COVI_spouse, onvalue="spouse_home", offvalue="")
spouse_home.grid(row=1, column=1, padx=10)

spouse_host = Checkbutton(add_info, variable=COVI_spouse, onvalue="spouse_host", offvalue="")
spouse_host.grid(row=1, column=2, padx=10)

children_home = Checkbutton(add_info, variable=COVI_children, onvalue="children_home", offvalue="")
children_home.grid(row=2, column=1, padx=10)
children_host = Checkbutton(add_info, variable=COVI_children, onvalue="children_host", offvalue="")
children_host.grid(row=2, column=2, padx=10)

payroll_home = Checkbutton(add_info, variable=COVI_payroll, onvalue="payroll_home", offvalue="")
payroll_home.grid(row=3, column=1, padx=10)
payroll_host = Checkbutton(add_info, variable=COVI_payroll, onvalue="payroll_host", offvalue="")
payroll_host.grid(row=3, column=2, padx=10)

soc_sec_home = Checkbutton(add_info, variable=COVI_socsec, onvalue="soc_sec_home", offvalue="")
soc_sec_home.grid(row=4, column=1, padx=10)
soc_sec_host = Checkbutton(add_info, variable=COVI_socsec, onvalue="soc_sec_host", offvalue="")
soc_sec_host.grid(row=4, column=2, padx=10)

assets_home = Checkbutton(add_info, variable=COVI_assets, onvalue="assets_home", offvalue="")
assets_home.grid(row=5, column=1, padx=10)
assets_host = Checkbutton(add_info, variable=COVI_assets, onvalue="assets_host", offvalue="")
assets_host.grid(row=5, column=2, padx=10)

child_num_label = Label(add_info, text="No. of children").grid(row=1, column=3, padx=10)
child_num = Entry(add_info, textvariable=child_number_tk, width=10)
child_num.grid(row=2, column=3, padx=10)


family_move_label = Label(add_info, text="Family move").grid(row=3,column=3, padx=10)
family_move_date = DateEntry(add_info, textvariable=family_move_tk, width=8)
family_move_date.grid(row=4, column=3, padx=10)

# HABITUAL ABODE

hab_abod = LabelFrame(f5, text="Addtional info")
hab_abod.pack(fill=X)

include_label_HA = Label(hab_abod, text="Include?").grid(row=0, column=2, padx=10)
include_butt_HA = Checkbutton(hab_abod, variable=incl_HA, onvalue="Yes", offvalue="No")
include_butt_HA.grid(row=1, column=2, padx=10)

days_home_label = Label(hab_abod, text="Days in Home country").grid(row=0, column=0, sticky=W, padx=10)
days_host_label = Label(hab_abod, text="Days in Host country").grid(row=1, column=0, sticky=W, padx=10)
days_home = Entry(hab_abod, textvariable=home_days_tk, width=10)
days_home.grid(row=0, column=1, padx=10)
days_host = Entry(hab_abod, textvariable=host_days_tk, width=10)
days_host.grid(row=1, column=1, padx=10)


# TAXATION
taxation_info = LabelFrame(f6, text="Taxation")
taxation_info.pack(fill=X)

include_label_TAX = Label(taxation_info, text="Include?").grid(row=0, column=2, padx=10)
include_butt_TAX = Checkbutton(taxation_info, variable=incl_TAX, onvalue="Yes", offvalue="No")
include_butt_TAX.grid(row=1, column=2, padx=10)

date_to_label = Label(taxation_info, text="Date").grid(row=3, column=0, sticky=W, padx=10)
to_from_label = Label(taxation_info, text="Up to/From").grid(row=4, column=0, sticky=W, padx=10)
days_nonrezi_label = Label(taxation_info, text="Exceed 183 days?").grid(row=1, column=0, sticky=W, padx=10)
dtt_type_label = Label(taxation_info, text="DTT Type").grid(row=2, column=0, sticky=W, padx=10)

days_nonrezi_entry = Combobox(taxation_info, textvariable=exceed183_tk, values=yes_no, width=10)
days_nonrezi_entry.grid(row=1, column=1, padx=10)
dtt_type = Combobox(taxation_info, textvariable=type_of_DTT_tk, values = dtt, width=10)
dtt_type.grid(row=2, column=1, padx=10)
date_to = DateEntry(taxation_info, textvariable=tax_date_tk, width=10)
date_to.grid(row=3, column=1, padx=10)
to_from_sel = Combobox(taxation_info, textvariable=up_from_tk, values=to_from, width=10)
to_from_sel.grid(row=4, column=1, padx=10)


button = Button(f7, text="Generate", command=print_all)
button.pack(fill=BOTH)

root.mainloop()


