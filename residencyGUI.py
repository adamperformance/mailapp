from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry
from country_list import *
from customtkinter import *


class Personal_Info(CTkFrame):
    def __init__(self, root=None, title_tk="", f_name_tk="", l_name_tk="", engagement_tk=""):
        # super().__init__(root)
        self.frame = CTkFrame(root)
        self.frame.pack(fill=Y, side=LEFT, padx=3, pady=3)

        self.title_label = CTkLabel(self.frame, text="Title")
        self.title_label.grid(row=0, column=0, sticky=W, padx=10)
        self.title_options = ["Ms.","Mr.", "Mrs."]
        self.title = CTkOptionMenu(self.frame, values=self.title_options, width=20)
        self.title.grid(row=0, column=1, sticky=W, padx=10, pady=2)

        self.f_name_label = CTkLabel(self.frame, text="First Name")
        self.f_name_label.grid(row=1, column=0, sticky=W, padx=10)
        self.f_name = CTkEntry(self.frame, width=100, textvariable=f_name_tk)
        self.f_name.grid(row=1, column=1, padx=10, pady=2)

        self.l_name_label = CTkLabel(self.frame, text="Last Name")
        self.l_name_label.grid(row=2, column=0, sticky=W, padx=10)
        self.l_name = CTkEntry(self.frame, width=100, textvariable=l_name_tk)
        self.l_name.grid(row=2, column=1, padx=10, pady=2)

        self.eng_label = CTkLabel(self.frame, text="Engagement")
        self.eng_label.grid(row=3, column=0, sticky=W, padx=10)
        self.engagement = CTkEntry(self.frame, width=100, textvariable=engagement_tk)
        self.engagement.grid(row=3, column=1, padx=10, pady=2)

    def get_value(self):
        print(self.title.get())
        print(self.f_name.get())
        print(self.l_name.get())
        print(self.engagement.get())
        return self.title.get(), self.f_name.get(), self.f_name.get(), self.engagement.get()

class Assignment_Info(CTkFrame):
    def __init__(self, root=None, countries=[]):
        self.assig_info = CTkFrame(root)
        self.assig_info.pack(fill=X, padx=3, pady=3)

        self.year=StringVar()
        self.year.set("2022")
        self.year_label = CTkLabel(self.assig_info, text="Year").grid(row=0, column=0, sticky=W, padx=10)
        self.year_values = ["2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025"]
        self.year_sel = CTkOptionMenu(self.assig_info, variable=self.year, values=self.year_values, width=15)
        self.year_sel.grid(row=0, column=1, sticky=W, padx=10, pady=2)

        self.home = StringVar()
        self.home.set("")
        self.from_country_label = CTkLabel(self.assig_info, text="From country")
        self.from_country_label.grid(row=1, column=0, sticky=W, padx=10)
        self.from_country = CTkComboBox(self.assig_info, variable=self.home, values=countries, width=100)
        self.from_country.grid(row=1, column=1, pady=2)
        self.from_country.bind("<KeyRelease>", lambda event: self.search_home(event, countries=countries))
        self.home.trace("w", self.add_country)

        self.host = StringVar()
        self.host.set("")
        self.to_country_label = CTkLabel(self.assig_info, text="To country")
        self.to_country_label.grid(row=2, column=0, sticky=W, padx=10)
        self.to_country = CTkComboBox(self.assig_info, variable=self.host, values=countries, width=100)
        self.to_country.grid(row=2, column=1, padx=10, pady=2)
        self.to_country.bind("<KeyRelease>", lambda event: self.search_host(event, countries=countries))
        self.host.trace("w",self.add_country)

        self.asstype = StringVar()
        self.asstype.set("")
        self.type_of_assignment = ["International Assignment", "Localization", "Business Trip"]
        self.assig_label = CTkLabel(self.assig_info, text="Assignment type")
        self.assig_label.grid(row=3, column=0, sticky=W, padx=10)
        self.assig_type = CTkComboBox(self.assig_info, variable=self.asstype, values=self.type_of_assignment, width=100)
        self.assig_type.grid(row=3, column=1, pady=2)

        self.country_pair = ["",""]
        self.residency = StringVar()
        self.residency.set("")
        self.residency_label = CTkLabel(self.assig_info, text="Residency").grid(row=4, column=0, sticky=W, padx=10)
        self.residency_box = CTkComboBox(self.assig_info, variable=self.residency, values=self.country_pair, width=100)
        self.residency_box.grid(row=4, column=1, pady=2)

    def get_value(self):
        print(self.year_sel.get())
        print(self.from_country.get())
        print(self.to_country.get())

    def add_country(self, *args):
        home_c = self.home.get()
        home_c = home_c.strip()
        host_c = self.host.get()
        host_c = host_c.strip()
        self.country_pair[0] = home_c
        self.country_pair[1] = host_c
        if self.country_pair[0] != "" and self.country_pair[1] != "":
            self.residency_box.configure(values=self.country_pair)

    def search_home(self, event, countries):
        value = event.widget.get()
        if value == "":
            self.from_country.configure(values=countries)
        else:
            data = []

            for country in countries:
                if value.lower() in country.lower():
                    data.append(country)
            self.from_country.configure(values=data)

    def search_host(self, event, countries):
        value = event.widget.get()
        if value == "":
            self.to_country.configure(values=countries)
        else:
            data = []

            for country in countries:
                if value.lower() in country.lower():
                    data.append(country)
            self.to_country.configure(values=data)

class PermanentHome_Info(CTkFrame):
    def __init__(self, root=None):
        self.permanent_home = CTkFrame(root)
        self.permanent_home.pack(fill=X, pady=3)
        self.PHlabel = CTkLabel(self.permanent_home, text="PH", font=(None, 30))
        self.PHlabel.grid(row=0, column=0, rowspan=3, padx=5, pady=3)
        self.ph_from_label = CTkLabel(self.permanent_home, text="From").grid(row=0, column=2)
        self.ph_to_label = CTkLabel(self.permanent_home, text="To").grid(row=0, column=3)
        self.ph_home_label = CTkLabel(self.permanent_home, text="Home country").grid(row=1, column=1, sticky=W, padx=10)
        self.ph_host_label = CTkLabel(self.permanent_home, text="Host country").grid(row=2, column=1, sticky=W, padx=10)

        self.home_f = StringVar()
        self.home_f.set("")
        self.home_t = StringVar()
        self.home_t.set("")
        self.host_f = StringVar()
        self.host_f.set("")
        self.host_t = StringVar()
        self.host_t.set("")
        self.ph_home_from_date = DateEntry(self.permanent_home, textvariable=self.home_f)
        self.ph_home_from_date.grid(row=1, column=2, padx=10)
        self.ph_home_to_date = DateEntry(self.permanent_home, textvariable=self.home_t)
        self.ph_home_to_date.grid(row=1, column=3, padx=10)
        self.ph_host_from_date = DateEntry(self.permanent_home, textvariable=self.host_f)
        self.ph_host_from_date.grid(row=2, column=2, padx=10)
        self.ph_host_to_date = DateEntry(self.permanent_home, textvariable=self.host_t)
        self.ph_host_to_date.grid(row=2, column=3, padx=10)

class COVI_Info(CTkFrame):
    def __init__(self, root=None):
        self.add_info = CTkFrame(root)
        # self.add_info.pack(pady=3)

        self.COVIlabel = CTkLabel(self.add_info, text="COVI", font=(None, 30))
        self.COVIlabel.grid(row=0, column=0, rowspan=5, padx=5, pady=3)
        self.home_label = CTkLabel(self.add_info, text="Home").grid(row=0, column=2, sticky=W, padx=2)
        self.host_label = CTkLabel(self.add_info, text="Host")
        self.host_label.grid(row=0, column=3, sticky=W, padx=2)
        self.spouse_label =  CTkLabel(self.add_info, text="Spouse")
        self.spouse_label.grid(row=1, column=1, sticky=W, padx=5)
        self.children_label =  CTkLabel(self.add_info, text="Children").grid(row=2, column=1, sticky=W, padx=5)
        self.payroll_label = CTkLabel(self.add_info, text="Payroll").grid(row=3, column=1, sticky=W, padx=5)
        self.soc_sec_label = CTkLabel(self.add_info, text="Soc. Sec.").grid(row=4, column=1, sticky=W, padx=5)
        self.assets_label =  CTkLabel(self.add_info, text="Assets").grid(row=5, column=1, sticky=W, padx=5)

        self.spouse = StringVar()
        self.spouse.set("")
        self.spouse_home = CTkCheckBox(self.add_info, variable=self.spouse, text=" ", onvalue="home", offvalue="", command=lambda: [self.reset()])
        self.spouse_home.grid(row=1, column=2, padx=2, sticky=NSEW)
        self.spouse_host = CTkCheckBox(self.add_info, variable=self.spouse, text=" ", onvalue="host", offvalue="", command=self.reset)
        self.spouse_host.grid(row=1, column=3, padx=2, sticky=NSEW)

        self.children = StringVar()
        self.children.set("")
        self.children_home = CTkCheckBox(self.add_info, variable=self.children, text=" ", onvalue="home", offvalue="", command=lambda:[self.reset1()])
        self.children_home.grid(row=2, column=2, padx=2)
        self.children_host = CTkCheckBox(self.add_info, variable=self.children, text=" ", onvalue="host", offvalue="", command=self.reset1)
        self.children_host.grid(row=2, column=3, padx=2)

        self.payroll = StringVar()
        self.payroll.set("")
        self.payroll_home = CTkCheckBox(self.add_info, variable=self.payroll, text=" ", onvalue="home", offvalue="", command=lambda:[self.reset2()])
        self.payroll_home.grid(row=3, column=2, padx=2)
        self.payroll_host = CTkCheckBox(self.add_info, variable=self.payroll, text=" ", onvalue="host", offvalue="", command=self.reset2)
        self.payroll_host.grid(row=3, column=3, padx=2)

        self.socsec = StringVar()
        self.socsec.set("")
        self.soc_sec_home = CTkCheckBox(self.add_info, variable=self.socsec, text=" ", onvalue="home", offvalue="", command=lambda:[self.reset3()])
        self.soc_sec_home.grid(row=4, column=2, padx=2)
        self.soc_sec_host = CTkCheckBox(self.add_info, variable=self.socsec, text=" ", onvalue="host", offvalue="", command=self.reset3)
        self.soc_sec_host.grid(row=4, column=3, padx=2)

        self.assets = StringVar()
        self.assets.set("")
        self.assets_home = CTkCheckBox(self.add_info, variable=self.assets, text=" ", onvalue="home", offvalue="", command=lambda:[self.reset4()])
        self.assets_home.grid(row=5, column=2, padx=2)
        self.assets_host = CTkCheckBox(self.add_info, variable=self.assets, text=" ", onvalue="host", offvalue="", command=self.reset4)
        self.assets_host.grid(row=5, column=3, padx=2)

        self.child_number = StringVar()
        self.child_number.set("")
        self.child_num_label = CTkLabel(self.add_info, text="No. of children").grid(row=1, column=4, padx=10)
        self.child_num = CTkEntry(self.add_info, textvariable=self.child_number, width=75)
        self.child_num.grid(row=2, column=4, padx=2)

        self.family_move = StringVar()
        self.family_move.set("")
        self.family_move_label = CTkLabel(self.add_info, text="Family move").grid(row=3,column=4, padx=10)
        self.family_move_date = DateEntry(self.add_info, textvariable=self.family_move, width=8)
        self.family_move_date.grid(row=4, column=4, padx=2)

    def get_value(self):
        print(self.spouse.get())
        print(self.children.get())
        print(self.payroll.get())
        print(self.socsec.get())
        print(self.assets.get())

    def reset(self):
        if self.spouse.get() == "home":
            self.spouse_host.deselect()
            self.spouse_home.select()
        elif self.spouse.get() == "host":
            self.spouse_home.deselect()
            self.spouse_host.select()

    def reset1(self):
        if self.children.get() == "home":
            self.children_host.deselect()
            self.children_home.select()
        elif self.children.get() == "host":
            self.children_home.deselect()
            self.children_host.select()

    def reset2(self):
        if self.payroll.get() == "home":
            self.payroll_host.deselect()
            self.payroll_home.select()
        elif self.payroll.get() == "host":
            self.payroll_home.deselect()
            self.payroll_host.select()

    def reset3(self):
        if self.socsec.get() == "home":
            self.soc_sec_host.deselect()
            self.soc_sec_home.select()
        elif self.socsec.get() == "host":
            self.soc_sec_home.deselect()
            self.soc_sec_host.select()

    def reset4(self):
        if self.assets.get() == "home":
            self.assets_host.deselect()
            self.assets_home.select()
        elif self.assets.get() == "host":
            self.assets_home.deselect()
            self.assets_host.select()


class HA_Info(CTkFrame):
    def __init__(self, root=None):
        self.hab_abod = CTkFrame(root)
        # self.hab_abod.pack(side=LEFT, fill=Y, padx=3, pady=3)

        self.HAlabel = CTkLabel(self.hab_abod, text="HA", font=(None, 30))
        self.HAlabel.grid(row=0, column=0, columnspan=2, padx=3, pady=2)

        self.home_days = StringVar()
        self.home_days.set("")
        self.host_days = StringVar()
        self.host_days.set("")
        self.days_home_label = CTkLabel(self.hab_abod, text="Days in Home country").grid(row=1, column=0, sticky=W, padx=10)
        self.days_host_label = CTkLabel(self.hab_abod, text="Days in Host country").grid(row=2, column=0, sticky=W, padx=10)
        self.days_home = CTkEntry(self.hab_abod, textvariable=self.home_days, width=60)
        self.days_home.grid(row=1, column=1, padx=5, pady=2)
        self.days_host = CTkEntry(self.hab_abod, textvariable=self.host_days, width=60)
        self.days_host.grid(row=2, column=1, padx=5, pady=2)

class Taxation_Info(CTkFrame):
    def __init__(self, root=None):
        self.taxation_info = CTkFrame(root)
        # self.taxation_info.pack(pady=3)

        self.TAXlabel = CTkLabel(self.taxation_info, text="TAXATION", font=(None, 30))
        self.TAXlabel.grid(row=0, column=0, columnspan=2, padx=3, pady=2)

        self.date_to_label = CTkLabel(self.taxation_info, text="Date").grid(row=3, column=0, sticky=W, padx=10)
        self.to_from_label = CTkLabel(self.taxation_info, text="Up to/From").grid(row=4, column=0, sticky=W, padx=10)
        self.days_nonrezi_label = CTkLabel(self.taxation_info, text="Exceed 183 days?").grid(row=1, column=0, sticky=W, padx=10)
        self.dtt_type_label = CTkLabel(self.taxation_info, text="DTT Type").grid(row=2, column=0, sticky=W, padx=10)

        self.exceed183 = StringVar()
        self.exceed183.set("")
        self.dtt_type = StringVar()
        self.dtt_type.set("")
        self.tax_date = StringVar()
        self.tax_date.set("")
        self.up_from = StringVar()
        self.up_from.set("")
        self.yes_no = ["Yes", "No"]
        self.days_nonrezi_entry = CTkComboBox(self.taxation_info, variable=self.exceed183, values=self.yes_no, width=100)
        self.days_nonrezi_entry.grid(row=1, column=1, padx=5, pady=2)
        self.dtt = ["Any 12 month", "Calendar year"]
        self.dtt_type = CTkComboBox(self.taxation_info, variable=self.dtt_type, values = self.dtt, width=100)
        self.dtt_type.grid(row=2, column=1, padx=5, pady=2)
        self.date_to = DateEntry(self.taxation_info, variable=self.tax_date) #, width=10)
        self.date_to.grid(row=3, column=1, padx=5, pady=2)
        self.to_from = ["from", "to"]
        self.to_from_sel = CTkComboBox(self.taxation_info, variable=self.up_from, values=self.to_from, width=100)
        self.to_from_sel.grid(row=4, column=1, padx=5, pady=2)
        # super().__init__()

