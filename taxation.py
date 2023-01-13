
from datetime import datetime

# variables from program
title = "Mr."
f_name = "Norbert"
l_name = "Adam"
year = "2022"


tax_date = ""

# variables created from user input

engagement = "Deloitte"
full_name = title + " " + f_name + " " + l_name
last_name = title + " " + l_name



his_her = ""
he_she = ""

if title == "Mr.":
    his_her = "his"
    he_she = "he"
else:
    his_her = "her"
    he_she = "she"

yearor12 = ""
type_of_DTT = "12 months"
if type_of_DTT == "12 months":
    yearor12 = "any 12 months period beginning or ending in the tax year"
elif type_of_DTT == "calendar year":
    yearor12 = "in the calendar year"
up_from = "from"

#OUTBOUND
# home_country = "Hungary"
# host_country = "Germany"
# residency = "Germany"
# exceed183 = "Yes"
# residency = "Hungary"
# exceed183 = "Yes"
# residency = "Germany" #<<-- the option where HU non-rezi, less than 183 days in HU - whether we want to tax or not is in question!!!!
# exceed183 = "No"
# residency = "Hungary"
# exceed183 = "No"

# #INBOUND
home_country = "Germany"
host_country = "Hungary"
# residency = "Germany"
# exceed183 = "Yes"
# residency = "Hungary"
# exceed183 = "Yes"
# residency = "Germany"
# exceed183 = "No"
residency = "Hungary"
exceed183 = "No"

tax_matrix = [home_country, host_country, residency, exceed183]

x = ""

if tax_matrix[1] == "Hungary":
    if tax_matrix[2] == "Hungary":
        if tax_matrix[3] == "No":
            x = f"""the part of {his_her} income allocated to {his_her} workdays in {home_country} could only be exempted from
            taxation in {host_country} if {engagement} {home_country} qualifies as {last_name}'s
            economic employer.
            """
        elif tax_matrix[3] == "Yes":
            x = f"""as {his_her} physical presence in {home_country} exceeded 183 days in the CALENDAR YEAR
            we understand that the part of {his_her} income relating to {his_her} workdays in {home_country}
            should be taxable in {home_country} and exempted from taxation {host_country}.
            """
    elif tax_matrix[2] != "Hungary":
        if tax_matrix[3] == "No":
            x = f"""the part of {his_her} income allocated to {his_her} workdays in {host_country} could only be exempted from
            taxation in {host_country} if {engagement} {host_country} does not qualify as {last_name}'s
            economic employer.
            """
        elif tax_matrix[3] == "Yes":
            x = f"""as {his_her} physical presence in {host_country} exceeded 183 days in the CALENDAR YEAR
            we understand that the part of {his_her} income relating to {his_her} workdays in {host_country}
            should be taxable in {home_country}.
            """
elif tax_matrix[1] != "Hungary":
    if tax_matrix[2] == "Hungary":
        if tax_matrix[3] == "No":
            x = f"""the part of {his_her} income allocated to {his_her} workdays in {host_country} could only be exempted from
            taxation in {home_country} if {engagement} {host_country} qualifies as {last_name}'s
            economic employer.
            """
        elif tax_matrix[3] == "Yes":
            x = f"""as {his_her} physical presence in {host_country} exceeded 183 days in the CALENDAR YEAR
            we understand that the part of {his_her} income relating to {his_her} workdays in {host_country}
            should be taxable in {host_country} and exempted from taxation in {home_country}.
            """
    elif tax_matrix[2] != "Hungary":
        if tax_matrix[3] == "No":
            x = f"""the part of {his_her} income allocated to {his_her} workdays in {home_country} could only be exempted from
            taxation in {home_country} if {engagement} {home_country} does not qualify as {last_name}'s
            economic employer.
            """
        elif tax_matrix[3] == "Yes":
            x = f"""as {his_her} physical presence in {home_country} exceeded 183 days in the CALENDAR YEAR
            we understand that the part of {his_her} income relating to {his_her} workdays in {home_country}
            should be taxable in {home_country}."""

# print(x)

y = ""

if tax_matrix[3] == "No":
    if tax_matrix[1] == "Hungary":
        if tax_matrix[2] == "Hungary":
            #FO-->HU & HU Rezi
            y = f"""Uness you confirm that the home company qualifies as the economic employer of {last_name},
                the part of {his_her} income relating to {his_her} workdays in {host_country} could not be exempted
                from taxation in {host_country}.
            """
        elif tax_matrix[2] != "Hungary":
            #FO-->HU & FO rezi
            y = f"""Unless an economic employer analysis is performed to confirm that {engagement} {host_country}
                    does not qualify as the economic employer of {last_name}, in order to minimize tax risk and exposure
                    for both {last_name} and the company, the part of {his_her} income allocated to {his_her} workdays
                    in {host_country} should not be exempted from taxation in {host_country}.
                """
    elif tax_matrix[1] != "Hungary":
        if tax_matrix[2] == "Hungary":
            #HU-->FO & HU rezi
            y = f"""Unless you confirm that the host company qualifies as the economic employer of {last_name},
                the part of {his_her} income relating to {his_her} workdays in {host_country} could not be exempted
                from taxation in {home_country}."""
        elif tax_matrix[2] != "Hungary":
            #HU-->FO & FO rezi
            y = f"""Unless an economic employer analysis is performed to confirm that {engagement} {home_country}
                does not qualify as the economic employer of {last_name}, in order to minimize tax risk and exposure
                for both {last_name} and the company, the part of {his_her} income allocated to {his_her} workdays
                in {home_country} should not be exempted from taxation in {home_country}.
                """

# print(y)

taxation_section = ""

if exceed183 == "No":
    z = f"""Please note that, although {last_name}'s physical presence in NONREZI did not exceed 183 days
        {yearor12},
    """
elif exceed183 == "Yes":
    z = f"""Please note that as {last_name}'s physical presence in NONREZI exceeded 183 days {yearor12},
    """

print(z + " " + x + " " + y)


