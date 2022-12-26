from docx import Document

document = Document("ctp.docx")

template = []
subject = []
bodytext = []

for paragraph in document.paragraphs:
    if paragraph.style.name == "Heading 1":
        template.append(paragraph.text)
    elif paragraph.style.name == "Heading 2":
        subject.append(paragraph.text)
    elif paragraph.style.name == "Normal":
        bodytext.append(paragraph.text)

for t, s in zip(template, subject):
    print(t, s)