
from datetime import datetime

# variables from program
title = "Mr."
f_name = "Norbert"
l_name = "Adam"
year = "2022"
home_country = "Hungary"
host_country = "Antarctica"
assignment_type = "international assignment"
residency = "Antarctica"
PH_home_f = "1/1/22"
PH_home_t = "12/31/22"
PH_host_f = "2/1/22"
PH_host_t = "10/30/22"
spouse_COVI = "spouse_host"
children_COVI = "children_host"
payroll_COVI = "payroll_home"
soc_sec_COVI = "soc_sec_home"
assets_COVI = "assets_home"
family_move = "3/1/22"
child_number = "4"
tax_date = ""
host_days = "300"
home_days = "65"

exceed183 = "Yes"
type_of_DTT = "12 months"
up_from = "from"


# variables created from user input

engagement = "Deloitte"
full_name = title + " " + f_name + " " + l_name
last_name = title + " " + l_name

home_PH_f= datetime.strptime(PH_home_f, '%m/%d/%y')
home_PH_t = datetime.strptime(PH_home_t, '%m/%d/%y')
host_PH_f = datetime.strptime(PH_host_f, '%m/%d/%y')
host_PH_t = datetime.strptime(PH_host_t, '%m/%d/%y')

other_country = ""
if home_country == "Hungary":
    other_country = host_country
else:
    other_country = home_country

his_her = ""
he_she = ""

if title == "Mr.":
    his_her = "his"
    he_she = "he"
else:
    his_her = "her"
    he_she = "she"


# Section 1 - introduction

 
introduction = f"""Dear XY! 

Hope this e-mail finds you well. 

We are contacting you regarding one of {engagement}'s assignee, {full_name}."""

# print(introduction)

# Section 2 - HU internal

internal = f"""According to local legislation {last_name} is considered a Hungarian tax resident in {year}.

Should {he_she} qualify as a tax resident in {other_country} as well for the same period, the provisions of the double tax treaty (DTT) concluded between {other_country} and Hunagry should apply.
"""

# print(internal)

# PH

PH_option = ""

if host_PH_f == "" and host_PH_t == "":
    PH_option = f"only in {home_country} throught {his_her} {assignment_type}."
elif home_PH_f == "" and home_PH_t == "":
    PH_option = f"only in {host_country} throughout {his_her} {assignment_type}."
elif home_PH_t < host_PH_f:
    PH_option = f"only in {host_country} as of the start date of {his_her} {assignment_type}."
elif host_PH_t < home_PH_f:
    PH_option = f"only in {host_country} up to the end date of {his_her} {assignment_type}."
elif host_PH_f < home_PH_t and home_PH_t < host_PH_t:
    PH_option = f"""in both countries in the {PH_host_t} - {PH_home_t} period and only in {host_country} after {PH_home_t}."""
elif home_PH_f < host_PH_t and host_PH_t < home_PH_t:
    PH_option = f"""only in {host_country} up to  {PH_home_f} and in both countries in the {PH_home_f} - {PH_host_t} period, up to the end of {his_her} {assignment_type}."""
elif home_PH_f <= host_PH_f and host_PH_t <= home_PH_t:
    PH_option = f"""in both countries throughout {his_her} {assignment_type}."""

# az utolsó opció nem jön ki, mert megegezik az utolsó előttivel


#options:
    # only in {home country} throughout {his/her} {assig_type}
    # only in {host country} throughout {his/her} {assig_type}
    # only in {host country} as of the start date of {his/her} {assig_type}
    # only in {host country} up to the end date of {his/her} {assig_type}
        # innentől nem lehet csak PH alapján reziséget eldönteni
    # in both countries in the {host_ph_start_date} - {home_ph_end_date} period and only in {host country} after {home_ph_end_date}
    # only in {host country} up to {home_ph_start_date} and in both countries in the {home_ph_start_date}-{host_ph_end_date} period, up to the end of {his/her} assignment
    # in both countries throughout {his/her} assignment 

permanent_home = f"""Based on the information available to us {last_name} had a permanent home {PH_option}"""

print(permanent_home)