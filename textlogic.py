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
ch = ""
if int(child_number) == 1:
    ch = "child"
if int(child_number) > 1:
    ch = "children"

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
him_her = ""

if title == "Mr.":
    his_her = "his"
    he_she = "he"
    him_her = "him"
else:
    his_her = "her"
    he_she = "she"
    him_her = "her"


# SECTION 1 - introduction

introduction = f"""Dear XY! 

Hope this e-mail finds you well. 

We are contacting you regarding one of {engagement}'s assignee, {full_name}."""

# print(introduction)

# SECTION 2 - HU internal stuff

internal = f"""According to local legislation {last_name} is considered a Hungarian tax resident in {year}.

Should {he_she} qualify as a tax resident in {other_country} as well for the same period, the provisions of the double tax treaty (DTT) concluded between {other_country} and Hunagry should apply.
"""

# print(internal)

# SECTION 3 - Permanent Home

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
elif host_PH_f < home_PH_f and host_PH_t < home_PH_t:
    PH_option = f"""only in {host_country} up to  {PH_home_f} and in both countries in the {PH_home_f} - {PH_host_t} period, up to the end of {his_her} {assignment_type}."""
elif home_PH_f <= host_PH_f and host_PH_t <= home_PH_t:
    PH_option = f"""in both countries throughout {his_her} {assignment_type}."""

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



# SECTION 4

COVI_matrix = [spouse_COVI, children_COVI, payroll_COVI, soc_sec_COVI, assets_COVI]

    # Step 1 - figure out family
family_setup = ""

if spouse_COVI != "" and (child_number == "" or child_number == "0"):
    family_setup = "spouse"
    if spouse_COVI == "spouse_home":
        s = f"stayed in {home_country}"
        c = f"resided in {home_country} as well"
    elif spouse_COVI == "spouse_host":
        s = f"accompanied {him_her} to {host_country}"
        c = f"shifted to {host_country} as of the move date of {him_her} {family_setup} on {family_move}"
elif spouse_COVI != "" and child_number != "" and child_number != "0":
    family_setup = f"spouse and {ch}"
    if spouse_COVI == "spouse_home" and children_COVI == "children_home":
        s = f"stayed in {home_country}"
        c = f"resided in {home_country} as well"
    elif spouse_COVI == "spouse_host" and children_COVI == "children_host":
        s = f"accompanied {him_her} to {host_country}"
        c = f"shifted to {host_country} as of the move date of {his_her} {family_setup} on {family_move}"
elif spouse_COVI == "" and child_number != "" and child_number != "0":
    family_setup == f"{ch}"

COVI_text = f"As {his_her} {family_setup} {s}, {his_her} center of vital interests {c}." 

print(COVI_text)
# set up checks --> if any of the COVI_matrix variables is "", exclude that from the final text


# SECTION 5



# SECTION 6 - Habitual Abode

habitual_abode = f"As {last_name} spent {home_days} days in {home_country} and {host_days} days in {host_country}, his habitual abode resided in {residency}."

print(habitual_abode)

# SECTION 7 - Residency Conclusion

residency_conclusion = f"In line with the above we are of the opinion that {last_name} should be considered a treaty resident in {residency}. Please confirm that you argee with our approach."

# SECTION 8 - TAXATION

tax_matrix = [home_country, host_country, residency, exceed183]

x = ""

if tax_matrix[1] == "Hungary":
    if tax_matrix[2] == "Hungary":
        if tax_matrix[3] == "No":
            x = f"""{his_her} income allocated to {his_her} {home_country} workdays could only be exempted from
            taxation in {host_country} if {engagement} {home_country} qualifies as {last_name}'s
            economic employer
            """
        else:
            x = f"""as {his_her} physical presence in {home_country} exceeded a 183 days in the CALENDAR YEAR
            we understand that the part of {his_her} income relating to {his_her} workdays in {home_country}
            should be taxable in {home_country} and exempted from taxation {host_country}.
            """
    else:
        if tax_matrix[3] == "No":
            x = f"""{his_her} income allocated to {his_her} {host_country} workdays could only be exempted from
            taxation in {host_country} if {engagement} {home_country} qualifies as {last_name}'s
            economic employer
            """
        else:
            x = f"""as {his_her} physical presence in {host_country} exceeded a 183 days in the CALENDAR YEAR
            we understand that the part of {his_her} income relating to {his_her} workdays in {host_country}
            should be taxable in {home_country}.
            """
else:
    if tax_matrix[2] == "Hungary":
        if tax_matrix[3] == "No":
            x = f"""{his_her} income allocated to {his_her} {host_country} workdays could only be exempted from
            taxation in {home_country} if {engagement} {host_country} qualifies as {last_name}'s
            economic employer
            """
        else:
            x = f"""as {his_her} physical presence in {host_country} exceeded a 183 days in the CALENDAR YEAR
            we understand that the part of {his_her} income relating to {his_her} workdays in {host_country}
            should be taxable in {host_country} and exempted from taxation {home_country}.
            """
    else:
        if tax_matrix[3] == "No":
            x = f"""{his_her} income allocated to {his_her} {home_country} workdays could only be exempted from
            taxation in {home_country} if {engagement} {home_country} does not qualify as {last_name}'s
            economic employer
            """
        else:
            x = f"""as {his_her} physical presence in {home_country} exceeded a 183 days in the CALENDAR YEAR
            we understand that the part of {his_her} income relating to {his_her} workdays in {home_country}
            should be taxable in {home_country}."""
    


#less than 183 days
    #HU is Host and FO rezi
x = f"""the part of {his_her} income allocated to {his_her} workdays in {host_country} could only 
    be exempted from taxation in {host_country} if {engagement} {host_country} does not qualify as 
    the economic employer of {last_name}"""

    #HU is host and HU rezi
y = f"""the part of {his_her} income allocated to {his_her} workdays in {host_country} could only 
    be exempted from taxation in {host_country} if {engagement} {host_country} does not qualify as 
    the economic employer of {last_name}"""

# print(x)


# SECTION 9 - Closing