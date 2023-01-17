from tkinter import *
from tkinter import ttk
from docx import Document
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
from customtkinter import *

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
    def __init__(self, root=None, emails=[], manager=[], reviewer=[], preparer=[],compspec=[], engagement=[], templates=[], subjects=[], bodytexts=[]):
        # super().__init__()

        #values it needs and uses
        self.emails = emails
        self.manager = manager
        self.reviewer = reviewer
        self.preparer = preparer
        self.compspec = compspec
        self.engagement = engagement
        self.templates = templates
        self.subjects = subjects
        self.bodytexts = bodytexts

        #GUI layout
        self.frame1 = CTkFrame(root)
        self.frame1.pack(fill=X, padx=2, pady=2)

        self.template = StringVar()
        self.template.set("")
        self.template_label = CTkLabel(self.frame1, text="Template?")
        self.template_label.grid(row=0,column=0, padx=3, pady=2)
        self.template_list = CTkComboBox(self.frame1, variable=self.template, values = self.templates)
        self.template_list.bind("<KeyRelease>", lambda event: self.search_template(event, templates=self.templates))
        self.template_list.grid(row=1, column=0, padx=2, pady=2)

        self.eng = StringVar()
        self.eng.set("")
        self.engagement_label = CTkLabel(self.frame1, text="Engagement?")
        self.engagement_label.grid(row=0, column=1, padx=3, pady=2)
        self.engagement_list = CTkComboBox(self.frame1, variable=self.eng, values = self.engagement)
        self.engagement_list.bind("<KeyRelease>", lambda event: self.search_engagement(event, engagement=self.engagement))
        self.engagement_list.grid(row=1, column=1, padx=2, pady=2)

        self.eng_selected = ""
        self.man_selected = ""
        self.rev_selected = ""
        self.prep_selected = ""
        self.compspec_selected = ""
        self.subj_selected = ""
        self.body_selected = ""

    def search_template(self, event, templates):
        value = event.widget.get()
        if value == "":
            self.template_list.configure(values=templates)
        else:
            data = []

            for template in templates:
                if value.lower() in template.lower():
                    data.append(template)
            self.template_list.configure(values=data)

    def search_engagement(self, event, engagement):
        value = event.widget.get()
        if value == "":
            self.engagement_list.configure(values=engagement)
        else:
            data = []

            for eng in engagement:
                if value.lower() in eng.lower():
                    data.append(eng)
            self.engagement_list.configure(values=data)

class Template_Time(CTkFrame):
    def __init__(self, root=None):
        #super().__init__()
        self.frame = CTkFrame(root)
        self.frame.pack(fill=X, padx=2, pady=2)

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