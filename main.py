# import win32com.client
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry
from country_list import *
from docx import Document
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
# from cls import Personal_Info, Other_Info
from customresid import Personal_Info, Assignment_Info, PermanentHome_Info, COVI_Info, HA_Info, Taxation_Info
from customtkinter import *
from functionality import create_variables

countries = ["Bahamas",
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

set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

root = CTk()
root.title("E-mail generator")

# create notebook to make separate tabs
notebook = CTkTabview(root)
notebook.pack(pady=5, padx=5)
#place(relx=0.5, rely=0.01, anchor=N)

year_tk = IntVar()
home_country_tk = StringVar()
host_country_tk = StringVar()

# add tabs to the notepad
notebook.add("Template")
notebook.add("Residency")
notebook.add("Advisory")


frame1 = CTkFrame(notebook.tab("Residency"))
frame1.pack(pady=3)
frame2 = CTkFrame(notebook.tab("Residency"))
frame2.pack(fill=X, pady=3)

residency_personal = Personal_Info(frame1)
residency_personal.frame.pack(fill=Y, side=LEFT, padx=3, pady=3)

residency_assignment = Assignment_Info(frame1, countries=countries)

residency_PH = PermanentHome_Info(notebook.tab("Residency"))


def incl(obj):
    if obj == root.nametowidget(".!ctktabview.!ctkframe2.!ctkframe2.!ctkcheckbox"):
        if check_COVI.get() == "yes":
            residency_COVI.add_info.pack(pady=3)
        elif check_COVI.get() == "no":
            residency_COVI.add_info.pack_forget()
    elif obj == root.nametowidget(".!ctktabview.!ctkframe2.!ctkframe2.!ctkcheckbox2"):
        if check_habit.get() == "yes":
            frame3.pack(side=LEFT, pady=3)
            residency_HA.hab_abod.pack(side=LEFT, fill=Y, padx=3, pady=3)
        elif check_COVI.get() == "no":
            frame3.pack_forget()
            residency_HA.hab_abod.pack_forget()
    elif obj == root.nametowidget(".!ctktabview.!ctkframe2.!ctkframe2.!ctkcheckbox3"):
        if check_taxation.get() == "yes":
            frame3.pack(side=LEFT, fill=Y, padx=3, pady=3)
            resid_taxation.taxation_info.pack(pady=3)
        elif check_taxation.get() == "no":
            frame3.pack_forget()  # EZ A SOR LESZEDI MIND A KETTŐT - AKKOR IS, HA CSAK AZ EGYIKET NYOMOM KI!
            resid_taxation.taxation_info.pack_forget()
    print(obj)

check_COVI = StringVar()
check_habit = StringVar()
check_taxation = StringVar()

check_CV = CTkCheckBox(frame2, text="COVI", variable=check_COVI, onvalue="yes", offvalue="no")
check_CV.configure(command=lambda obj=check_CV: incl(obj))
check_CV.pack(side=LEFT, padx=25)
check_HA = CTkCheckBox(frame2, text="HA", variable=check_habit, onvalue="yes", offvalue="no")
check_HA.configure(command=lambda obj=check_HA: incl(obj))
check_HA.pack(side=LEFT, padx=25)
check_TAX = CTkCheckBox(frame2, text="TAX", variable=check_taxation, onvalue="yes", offvalue="no")
check_TAX.configure(command=lambda obj=check_TAX: incl(obj))
check_TAX.pack(side=LEFT, padx=25)



residency_COVI = COVI_Info(notebook.tab("Residency"))


frame3 = CTkFrame(notebook.tab("Residency"))
residency_HA = HA_Info(frame3)
resid_taxation = Taxation_Info(frame3)

# button = CTkButton(notebook.tab("Residency"), text="Button!", command=residency_COVI.get_value)
# button.pack()

# last_name, he_she, his_her, him_her, other_country = create_variables("Mr.","Norbert","Adam","01/01/2022","01/01/2022", "01/01/2022", "01/01/2022", "Hungary", "the Bahamas", "1")
# print(last_name)
# print(he_she)
# print(his_her)
# print(him_her)
# print(other_country)

root.mainloop()