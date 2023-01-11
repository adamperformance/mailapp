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
residency_personal = Personal_Info(frame1)
residency_personal.frame.pack(fill=Y, side=LEFT, padx=3, pady=3)
residency_assignment = Assignment_Info(frame1, countries=countries)
# residency_personal = Personal_Info(notebook.tab("Residency"))
# residency_assignment = Assignment_Info(notebook.tab("Residency"), countries=countries)
residency_PH = PermanentHome_Info(notebook.tab("Residency"))
residency_COVI = COVI_Info(notebook.tab("Residency"))


frame2 = CTkFrame(notebook.tab("Residency"))
frame2.pack(pady=3)
residency_HA = HA_Info(frame2)
resid_taxation = Taxation_Info(frame2)

button = CTkButton(notebook.tab("Residency"), text="Button!", command=residency_COVI.get_value)
button.pack()

root.mainloop()