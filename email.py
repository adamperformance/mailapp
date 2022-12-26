# import win32com.client
from tkinter import *
from tkinter import ttk

# create window
root = Tk()
root.title("E-mail generator")
frame = Frame(root, relief=RIDGE, borderwidth=5)
frame.pack()
label = Label(frame, text="Üdvözöllek a template generálóprogramban!")
label.pack()

# open up new e-mail
# outlook = win32com.client.Dispatch('outlook.application')
# mail = outlook.CreateItem(0)

# mail.To = 'adamnorbert90@gmail.com'
# mail.Subject = 'Próba'
# mail.Body = 'Próba'

# mail.Display(True)