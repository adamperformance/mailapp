from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk
from tkcalendar import Calendar, DateEntry
from country_list import *


country_pair = []
resid_pair = []
to_from = ["up to","from"]
yes_no = ["yes","no"]
dtt = ["calendar", "12 months"]
cp = ["",""]


# FUNCTIONS USED THROUGHOUT THE PROGRAM

# def comboselection(event):
    
#     if len(country_pair) < 2:
#         country_pair.append(event.widget.get())
#     else:
#         if event.widget == root.nametowidget(".!frame2.!labelframe.!combobox2"):
#             country_pair[0] = event.widget.get()
#         elif event.widget == root.nametowidget(".!frame2.!labelframe.!combobox3"):
#             country_pair[1] = event.widget.get()

# def combobox_values():
#     for i in range(len(country_pair)):
#         cp[i] = country_pair[i]
#     return cp

# def db_refresh(event):
#     residency_box['values'] = combobox_values()


# def print_all():
#     title = title_tk.get()
#     f_name = f_name_tk.get()
#     l_name = l_name_tk.get()
#     year = year_tk.get()
#     home_country = home_country_tk.get()
#     host_country = host_country_tk.get()
#     assignment_type = assignment_type_tk.get()
#     residency = residency_tk.get()
#     PH_home_f = PH_home_f_tk.get()
#     PH_home_t = PH_home_t_tk.get()
#     PH_host_f = PH_host_f_tk.get()
#     PH_host_t = PH_host_t_tk.get()
#     spouse_COVI = COVI_spouse.get()
#     children_COVI = COVI_children.get()
#     payroll_COVI = COVI_payroll.get()
#     soc_sec_COVI = COVI_socsec.get()
#     assets_COVI = COVI_assets.get()
#     family_move = family_move_tk.get()
#     child_number = child_number_tk.get()
#     tax_date = tax_date_tk.get()
#     home_days = home_days_tk.get()
#     host_days = host_days_tk.get()
#     exceeds183 = exceed183_tk.get()
#     type_of_DTT = type_of_DTT_tk.get()
#     up_from = up_from_tk.get()


class Personal_Info(tk.Frame):
    def __init__(self, root=None, title_tk="", f_name_tk="", l_name_tk=""):
        self.frame1 = Frame(root)
        self.frame1.pack(fill=X)

        self.title_label = Label(self.frame1, text="Title")
        self.title_label.grid(row=0, column=0, sticky=W, padx=10)
        self.title_options = ["Ms.","Mr.", "Mrs."]
        self.title = Combobox(self.frame1, textvariable = title_tk, values=self.title_options, width=13)
        self.title.grid(row=0, column=1, sticky=W, padx=10)

        self.f_name_label = Label(self.frame1, text="First Name")
        self.f_name_label.grid(row=1, column=0, sticky=W, padx=10)
        self.f_name = Entry(self.frame1, width=15, textvariable=f_name_tk)
        self.f_name.grid(row=1, column=1, padx=10)

        self.l_name_label = Label(self.frame1, text="Last Name")
        self.l_name_label.grid(row=2, column=0, sticky=W, padx=10)
        self.l_name = Entry(self.frame1, width=15, textvariable=l_name_tk)
        self.l_name.grid(row=2, column=1, padx=10)

    def get_value(self):
        print(self.title.get())
        print(self.f_name.get())
        print(self.l_name.get())

class Other_Info(tk.Frame):
    def __init__(self, root=None, title_tk=""):
        self.frame1 = Frame(root)

        self.title_label = Label(self.frame1, text="Title")
        self.title_label.grid(row=0, column=0, sticky=W, padx=10)
        self.title_options = ["Option1","Option2","Option3"]
        self.title = Combobox(self.frame1, textvariable = title_tk, values=self.title_options, width=13)
        self.title.grid(row=0, column=1, sticky=W, padx=10)