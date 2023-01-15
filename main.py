# import win32com.client
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry
from country_list import *
from docx import Document
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
from residencyGUI import Personal_Info, Assignment_Info, PermanentHome_Info, COVI_Info, HA_Info, Taxation_Info
from residencyFunct import basic_variables, permhome_variables, introduction, internal
from residencyFunct import perm_home, covi_family, covi_other, hab_abode, resid_concl, taxation, closing
from templateGUI import Template_Choice, Template_Frame, Template_Time
from templateFunct import manager, reviewer, preparer, emails, eng_name, countries, engagement_teams
from templateFunct import templates, templates1, subjects, subjects1, bodytexts, bodytexts1
from customtkinter import *

def set_template_list(*args):
    if template_choice.val.get() == "Compliance":
        template_setup.templates = templates
        template_setup.subjects = subjects
        template_setup.bodytexts = bodytexts
        template_setup.template_list.configure(values=templates)
    elif template_choice.val.get() == "Year-End":
        template_setup.templates = templates1
        template_setup.subjects = subjects1
        template_setup.bodytexts = bodytexts1
        template_setup.template_list.configure(values=templates1)

def pri(*args):
    x = 0
    for i in range(len(template_setup.templates)):
        if template_setup.template.get() == template_setup.templates[i]:
            x = i
    template_setup.subj_selected = template_setup.subjects[x]
    template_setup.body_selected = template_setup.bodytexts[x]

    t={}
    eng = template_setup.eng.get()
    template_setup.eng_selected = eng
    for team in engagement_teams:
        if team["engagement"] == eng:
            t = team["team"]
            template_setup.man_selected = t["manager"]
            template_setup.rev_selected = t["reviewer"]
            template_setup.prep_selected = t["preparer"]

set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

root = CTk()
root.title("GES Application")

# create notebook to make separate tabs
notebook = CTkTabview(root)
notebook.pack(pady=5, padx=5)

year_tk = IntVar()
home_country_tk = StringVar()
host_country_tk = StringVar()

# add tabs to the notepad
notebook.add("Template")
notebook.add("Residency")
notebook.add("Advisory")

# Template tab

#make combo boxes searchable
template_choice = Template_Choice(notebook.tab("Template"))
template_choice.val.trace("w", set_template_list)
template_setup = Template_Frame(notebook.tab("Template"), emails, manager, reviewer, preparer, eng_name, templates, subjects, bodytexts)
template_setup.template.trace("w", pri)
template_setup.eng.trace("w", pri)
template_time = Template_Time(notebook.tab("Template"))
template_button = CTkButton(notebook.tab("Template"), text="Generate")
template_button.pack(fill=X)






# Residency tab

# whether to include the COVI/HA/TAXATION parts
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
        elif check_habit.get() == "no" and (check_taxation.get() == "no" or check_taxation.get() == ""):
            frame3.pack_forget()
            residency_HA.hab_abod.pack_forget()
        elif check_habit.get() == "no" and check_taxation.get() == "yes":
            residency_HA.hab_abod.pack_forget()
    elif obj == root.nametowidget(".!ctktabview.!ctkframe2.!ctkframe2.!ctkcheckbox3"):
        if check_taxation.get() == "yes":
            frame3.pack(side=LEFT, fill=Y, padx=3, pady=3)
            resid_taxation.taxation_info.pack(side=LEFT, pady=3)
        elif check_taxation.get() == "no" and (check_habit.get() == "no" or check_habit.get() == ""):
            frame3.pack_forget()
            resid_taxation.taxation_info.pack_forget()
        elif check_taxation.get() == "no" and check_habit.get() == "yes":
            resid_taxation.taxation_info.pack_forget()


# the function that is called when the button is pressed - this initiates all the further
# functions that run the residency determination
def collection():

    # get the basic information (name, engagement, sex)
    title = residency_personal.title.get()
    f_name = residency_personal.f_name.get()
    l_name = residency_personal.l_name.get()
    engagement = residency_personal.engagement.get()
    full_name, last_name, he_she, his_her, him_her = basic_variables(title, f_name, l_name)

    # get the assignment info (from/to/residency)
    year = residency_assignment.year.get()
    home = residency_assignment.home.get()
    host = residency_assignment.host.get()
    assigtype = residency_assignment.asstype.get()
    residency = residency_assignment.residency.get()
    other_country = ""
    if home == "Hungary":
        other_country = host
    elif host == "Hungary":
        other_country = home

    # info related to perm. home
    PH_home_f = residency_PH.home_f.get()
    PH_home_t = residency_PH.home_t.get()
    PH_host_f = residency_PH.host_f.get()
    PH_host_t = residency_PH.host_t.get()

    homeF, homeT, hostF, hostT = permhome_variables(PH_home_f,PH_home_t,PH_host_f,PH_host_t)

    #if covi/etc checked --> than execute this
    if check_COVI.get() == "yes":
        spouse = residency_COVI.spouse.get()
        children = residency_COVI.children.get()
        payroll = residency_COVI.payroll.get()
        socsec = residency_COVI.socsec.get()
        assets = residency_COVI.assets.get()
        child_number = residency_COVI.child_number.get()
        family_move = residency_COVI.family_move.get()


    # x = introduction(engagement, full_name)
    # y = internal(last_name, year, he_she, other_country)
    # z = perm_home(PH_home_f, PH_home_t, PH_host_f, PH_host_t, last_name, his_her, home, host, assigtype)
    # a = covi_family(spouse, children, child_number, family_move, his_her, him_her, home, host)
    # b = covi_other(payroll, socsec, assets, he_she, his_her, home, host)

    # print(x+y+z+a)

    if check_HA.get() == "yes":
        home_days = residency_HA.home_days.get()
        host_days = residency_HA.host_days.get()
        hab_abode(last_name, home_days, host_days, home, host, residency)

    resid_concl(last_name, residency)

    if check_TAX.get() == "yes":
        exceed = resid_taxation.exceed183.get()
        dtt = resid_taxation.dtt_type.get()
        tax_date = resid_taxation.tax_date.get()
        up_from = resid_taxation.up_from.get()
    taxation(last_name, his_her, engagement, home, host, residency, exceed)
    # construct_email(full_name, last_name, engagement)
    # get info from the additional parts

    closing()

    # CALL THE FUNCTION THAT WILL CREATE THE FINAL E-MAIL
    # THAT FUNCTION SHOULD INCLUDE ALL THE "introduction", etc. parts from residFunc

def construct_email():
    pass

frame1 = CTkFrame(notebook.tab("Residency"))
frame1.pack(pady=3)
frame2 = CTkFrame(notebook.tab("Residency"))
frame2.pack(fill=X, pady=3)

# create the 3 basic parts of the form
residency_personal = Personal_Info(frame1)
residency_assignment = Assignment_Info(frame1, countries=countries)
residency_PH = PermanentHome_Info(notebook.tab("Residency"))

# variables linked to the additional parts (COVI, HA, TAXATION)
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

button = CTkButton(notebook.tab("Residency"), text="Button!", command=collection)
button.pack()

root.mainloop()


""" HOW TO LINK FUNCTIONALITY AND INPUT?
User fills out the forms and clicks the button.
The button calls a function. This function should collesct all the info from the forms.
Store the collected info in variables and pass them to other funtions.
Other functions = functions stored in the residFunct file. """