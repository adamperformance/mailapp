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
    print(sex_radio.get())
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


pers_info = LabelFrame(f1, text="Personal info")
pers_info.pack(fill=X)

name_label = Label(pers_info, text="Name")
name_label.pack()
placeholder_text1= StringVar()
f_name = Entry(pers_info, textvariable=placeholder_text1)
f_name.insert(0, "First Name")
f_name.pack(pady=10)
placeholder_text2= StringVar()
l_name = Entry(pers_info, textvariable=placeholder_text2)
l_name.insert(0, "Last Name")
l_name.pack(pady=10)

label = Label(pers_info, text="Sex?")
label.pack()
sex_radio = StringVar()
sex_m = Radiobutton(pers_info, text="Male", variable=sex_radio, value="M", )
sex_m.pack()
sex_f = Radiobutton(pers_info, text="Female", variable=sex_radio, value="F")
sex_f.pack()

family_info = LabelFrame(f2, text="Family Information")
family_info.pack(fill=X)

married_label = Label(family_info, text="Marital status")
married_label.pack()
married_info = StringVar()
married_y = Radiobutton(family_info, variable=married_info, value="Y", text="Yes")
married_y.pack()
married_n = Radiobutton(family_info, variable=married_info, value="N", text="No")
married_n.pack()
children_label = Label(family_info, text="Number of children")
children_label.pack()
num_children = Entry(family_info)
num_children.pack()
fam_move_label = Label(family_info, text="Family move date")
fam_move_label.pack()
fam_move_date = DateEntry(family_info)
fam_move_date.pack()

assig_info = LabelFrame(f3, text="Assignment Information")
assig_info.pack(fill=X)

assig_label = Label(assig_info, text="Assignment type", relief="groove").pack()
assig_type = Combobox(assig_info, values=type_of_assignment).pack()

from_country_label = Label(assig_info, text="From country", relief="sunken").pack()
from_country = Combobox(assig_info, values=countries).pack()
to_country_label = Label(assig_info, text="To country", relief="sunken").pack()
to_country = Combobox(assig_info, values=countries).pack()


date_label1 = Label(f4, text="Start date").pack(side=LEFT)
start_date = DateEntry(f4)
start_date.pack(side=LEFT)

date_label2 = Label(f4, text="End date").pack(side=LEFT)
end_date = DateEntry(f4).pack(side=LEFT)


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

button = Button(f6, text="Generate", command=get_values)
button.pack()

root.mainloop()