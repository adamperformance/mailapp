# import win32com.client
from tkinter import *
from tkinter import ttk
from docx import Document
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

document = Document("ctp1.docx")

# get all the titles, subtitles and body texts.
templates = []
subjects = []
curr_paragraph = ""
bodytexts = []
x = 0

for paragraph in document.paragraphs:
    if paragraph.style.name == "Heading 1":
        templates.append(paragraph.text)
        x = 1
    elif paragraph.style.name == "Heading 2":
        subjects.append(paragraph.text)
        x = 2
    elif paragraph.style.name == "Normal":
        x = 0

    if x == 0:
        curr_paragraph = curr_paragraph + paragraph.text
    elif x == 1:
        bodytexts.append(curr_paragraph)
        curr_paragraph = ""

# get the teams from the excel

wb = load_workbook("GES.xlsx")
sheets = wb.sheetnames
ca = wb[sheets[1]]
email = wb[sheets[2]]

engagements = []
manager = []
reviewer = []
preparer = []

for i in range (2,5):
    engagements.append(ca[f"A{i}"].value)
    manager.append(ca[f"B{i}"].value)
    reviewer.append(ca[f"C{i}"].value)
    preparer.append(ca[f"D{i}"].value)

# create window
root = Tk()
root.title("E-mail generator")
root.geometry("700x800")
root.config(background="skyblue")


# create notebook to make separate tabs
notebook = ttk.Notebook(root, width=600)
notebook.place(relx=0.5, rely=0.01, anchor=N)

# create the 3 different tabs and the frames that each will contain
# TAB 1 for the templates
template_frame = Frame(root, relief=RIDGE, borderwidth=5, background="Pink")
template_frame.place()

frame1 = Frame(template_frame, relief=RIDGE, borderwidth=5, background="green")
frame1.config(width=1000)
frame1.grid(row=0, column=0, columnspan=3)

frame2 = Frame(template_frame, relief=RIDGE, borderwidth=5)
frame2.grid(row=1, column=0)
frame3 = Frame(template_frame, relief=RIDGE, borderwidth=5)
frame3.grid(row=2, column=1)
frame4 = Frame(template_frame, relief=RIDGE, borderwidth=5)
frame4.grid(row=3, column=2)
label = Label(frame1, text="Hello!")
label.grid(row=0, column=1)

# TAB 2 for the residency
residency_frame = Frame(root, relief=RIDGE, borderwidth=5)
residency_frame.grid()
label = Label(residency_frame, text="Üdvözöllek a reziség egyeztető e-mail generáló programban!")
label.grid()

# # TAB 3 for the advisory
advisory_frame = Frame(root, relief=RIDGE, borderwidth=5)
advisory_frame.grid()
label = Label(advisory_frame, text="Tanácsadás generáló programban!")
label.grid()

# add tabs to the notepad
notebook.add(template_frame, text="Template")
notebook.add(residency_frame, text="Residency")
notebook.add(advisory_frame, text="Advisory")

# TEMPLATE
# fill up the template tab

template_label = Label(frame1, text="Template?")
template_label.grid(row=1, column=1)
template_list = ttk.Combobox(frame1, values = templates)
template_list.grid(row=2, column=0, columnspan=3)

engagement_label = Label(frame2, text="Engagement?")
engagement_label.pack()
engagement_list = ttk.Combobox(frame2, values = engagements)
engagement_list.pack()


def getTemplate():
    chosen_template = template_list.get()    
    temp_num = template_list.current()

    return chosen_template, temp_num

def getEngagement():
    chosen_engagement = engagement_list.get()
    eng_num = engagement_list.current()

    return chosen_engagement, eng_num

generate_button = Button(frame3, text="Generálás!", command=lambda: [getTemplate(), getEngagement()])
generate_button.pack()

def getRemaining():
    temp_chosen, temp_num = getTemplate()
    eng_chosen, eng_num = getEngagement()
    print(subjects[temp_num])
    print(bodytexts[temp_num])
    print(manager[eng_num])
    print(reviewer[eng_num])
    print(preparer[eng_num])

another_button = Button(frame4, text="Print!", command=getRemaining)
another_button.pack()

# open up new e-mail
# outlook = win32com.client.Dispatch('outlook.application')
# mail = outlook.CreateItem(0)

# mail.To = 'adamnorbert90@gmail.com'
# mail.Subject = 'Próba'
# mail.Body = 'Próba'

# mail.Display(True)

root.mainloop()