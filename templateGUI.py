from tkinter import *
from tkinter import ttk
from docx import Document
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
from customtkinter import *

# ami még  kell: év, Q, stb. kiválasztása --> szöveg update ennek megfelelően!!!

class Template_Choice(CTkFrame):
    def __init__(self, root=None):
        #supoer().__init__()
        self.frame = CTkFrame(root)
        self.frame.pack(fill=X, padx=2, pady=2)
        self.label = CTkLabel(self.frame, text="Choose a template")
        self.label.pack(side=LEFT, padx=5, pady=3)

        self.val = StringVar()
        self.val.set("")
        self.choice = CTkComboBox(self.frame, variable=self.val, values=["Compliance", "Year-End"])
        self.choice.pack(side=LEFT, padx=5, pady=3)


class Template_Frame(CTkFrame):
    def __init__(self, root=None, emails=[], manager=[], reviewer=[], preparer=[], engagement=[], templates=[], subjects=[], bodytexts=[]):
        # super().__init__()

        #values it needs and uses
        self.emails = emails
        self.manager = manager
        self.reviewer = reviewer
        self.preparer = preparer
        self.engagement = engagement
        self.templates = templates
        self.subjects = subjects
        self.bodytexts = bodytexts

        #GUI layout
        self.frame1 = CTkFrame(root)
        self.frame1.pack(fill=X)

        self.template = StringVar()
        self.template.set("")
        self.template_label = CTkLabel(self.frame1, text="Template?")
        self.template_label.grid(row=0,column=0, padx=3, pady=2)
        self.template_list = CTkComboBox(self.frame1, variable=self.template, values = self.templates)
        self.template_list.grid(row=1, column=0, padx=2, pady=2)

        self.eng = StringVar()
        self.eng.set("")
        self.engagement_label = CTkLabel(self.frame1, text="Engagement?")
        self.engagement_label.grid(row=0, column=1, padx=3, pady=2)
        self.engagement_list = CTkComboBox(self.frame1, variable=self.eng, values = self.engagement)
        self.engagement_list.grid(row=1, column=1, padx=2, pady=2)

        self.eng_selected = ""
        self.man_selected = ""
        self.rev_selected = ""
        self.prep_selected = ""
        self.subj_selected = ""
        self.body_selected = ""

class Template_Time(CTkFrame):
    def __init__(self, root=None):
        #super().__init__()
        self.frame = CTkFrame(root)
        self.frame.pack(pady=2)

        self.year_tk = StringVar()
        self.year_tk.set("")
        self.years = ["2016","2017","2018","2019","2020","2021","2022","2023","2024","2025"]
        self.year_label = CTkLabel(self.frame, text="Year")
        self.year_label.grid(row=2, column=0, padx=2, pady=2)
        self.year = CTkComboBox(self.frame, variable=self.year_tk, values=self.years)
        self.year.grid(row=3, column=0, padx=2, pady=2)

        self.qopt = ["Q1","Q2","Q3","Q4"]
        self.quar = StringVar()
        self.quar.set("")
        self.quar_label = CTkLabel(self.frame, text="Quarter")
        self.quar_label.grid(row=2, column=1, padx=2, pady=2)
        self.quar_sel = CTkComboBox(self.frame, variable=self.quar, values=self.qopt)
        self.quar_sel.grid(row=3, column=1, padx=2, pady=2)


    #     self.generate_button = CTkButton(self.frame1, text="Generálás!", command=lambda: [self.getTemplate(), self.getEngagement()])
    #     self.generate_button.pack()


    #     self.another_button = CTkButton(self.frame1, text="Print!", command=self.pri) #command=self.getRemaining)
    #     self.another_button.pack()

    # def pri(self,valami):
    #     print(valami)

    # def getTemplate(self):
    #     chosen_template = self.template_list.get()
    #     temp_num = self.template_list.current()

    #     return chosen_template, temp_num

    # def getEngagement(self):
    #     chosen_engagement = self.engagement_list.get()
    #     # eng_num = self.engagement_list.current()

    #     return chosen_engagement

    # def get_emails(self):
    #     chosen_engagement = self.engagement_list.get()

    #     pass

    # def getRemaining(self):
    #     temp_chosen, temp_num = self.getTemplate()
    #     eng_chosen, eng_num = self.getEngagement()
    #     # print(subjects[temp_num])
    #     # print(bodytexts[temp_num])
    #     # print(manager[eng_num])
    #     # print(reviewer[eng_num])
    #     # print(preparer[eng_num])
