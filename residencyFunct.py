from datetime import datetime


# Create the variables used below from user input

def basic_variables(title, first_name, last_name): 
    # create the "Mr. Adam" name to be used
    full_name = title + " " + first_name + " " + last_name
    last_name = title + " " + last_name

    # based on sex, create the he/his/him/she/her/her variables
    if title == "Mr.":
        his_her = "his"
        he_she = "he"
        him_her = "him"
    else:
        his_her = "her"
        he_she = "she"
        him_her = "her"

    return full_name, last_name, he_she, his_her, him_her

   
def permhome_variables(PH_home_f, PH_home_t, PH_host_f, PH_host_t):
    # convert provided dates to datetime
    home_PH_f = datetime.strptime(PH_home_f, '%m/%d/%y')
    home_PH_f = home_PH_f.strftime('%d %B %Y')
    home_PH_t = datetime.strptime(PH_home_t, '%m/%d/%y')
    home_PH_t = home_PH_t.strftime('%d %B %Y')
    host_PH_f = datetime.strptime(PH_host_f, '%m/%d/%y')
    host_PH_f = host_PH_f.strftime('%d %B %Y')
    host_PH_t = datetime.strptime(PH_host_t, '%m/%d/%y')
    host_PH_t = host_PH_t.strftime('%d %B %Y')

    return home_PH_f, home_PH_t, host_PH_f, host_PH_t


# SECTION 1 - introduction
def introduction(engagement, full_name):
    introduction = f"""Dear XY! 

Hope this e-mail finds you well. 

We are contacting you regarding one of {engagement}'s assignee, {full_name}."""

    return introduction

# SECTION 2 - HU internal stuff

def internal(last_name, year, he_she, other_country):

    internal = f"""According to local legislation {last_name} is considered a Hungarian tax resident in {year}.

Should {he_she} qualify as a tax resident in {other_country} as well for the same period, the provisions of the double tax treaty (DTT) concluded between {other_country} and Hunagry should apply.
    """
    return internal


# SECTION 3 - PH

def perm_home(home_f, home_t, host_f, host_t, last_name, his_her, home_country, host_country, assignment_type):
    PH_option = ""

    m, d, y = home_f.split("/")
    y = "20" + y
    home_PH_f = datetime(int(y),int(m),int(d))
    m, d, y = home_t.split("/")
    y = "20" + y
    home_PH_t = datetime(int(y),int(m),int(d))
    m, d, y = host_f.split("/")
    y = "20" + y
    host_PH_f = datetime(int(y),int(m),int(d))
    m, d, y = host_t.split("/")
    y = "20" + y
    host_PH_t = datetime(int(y),int(m),int(d))

    if host_PH_f == "" and host_PH_t == "":
        PH_option = f"only in {home_country} throught {his_her} {assignment_type}."
    elif home_PH_f == "" and home_PH_t == "":
        PH_option = f"only in {host_country} throughout {his_her} {assignment_type}."
    elif home_PH_t < host_PH_f:
        PH_option = f"only in {host_country} as of the start date of {his_her} {assignment_type}."
    elif host_PH_t < home_PH_f:
        PH_option = f"only in {host_country} up to the end date of {his_her} {assignment_type}."
    elif host_PH_f < home_PH_t and home_PH_t < host_PH_t:
        PH_option = f"""in both countries in the {host_PH_t} - {home_PH_t} period and only in {host_country} after {home_PH_t}."""
    elif home_PH_f < host_PH_t and host_PH_t < home_PH_t:
        PH_option = f"""only in {host_country} up to  {home_PH_f} and in both countries in the {home_PH_f} - {host_PH_t} period, up to the end of {his_her} {assignment_type}."""
    elif home_PH_f <= host_PH_f and host_PH_t <= home_PH_t:
        PH_option = f"""in both countries throughout {his_her} {assignment_type}."""

    permanent_home = f"""
Based on the information available to us {last_name} had a permanent home {PH_option}"""
    return permanent_home

# SECTION 4 - COVI family

def covi_family(spouse_COVI, children_COVI, child_number, family_move, his_her, him_her, home_country, host_country):
    # Step 1 - figure out family
    family_setup = ""

    # if assignee has 1 child --> "child", else "children"
    child_ren = ""
    if int(child_number) == 1:
        child_ren = "child"
    if int(child_number) > 1:
        child_ren = "children"

    # family move date converting
    family_move= datetime.strptime(family_move, '%m/%d/%y')
    family_move = family_move.strftime('%d %B %Y')

    s = ""
    c = ""

    if spouse_COVI != "" and (child_number == "" or child_number == "0"):
        family_setup = "spouse"
        if spouse_COVI == "home":
            s = f"stayed in {home_country}"
            c = f"resided in {home_country} as well"
        elif spouse_COVI == "host":
            s = f"accompanied {him_her} to {host_country}"
            c = f"shifted to {host_country} as of the move date of {him_her} {family_setup} on {family_move}"
    elif spouse_COVI != "" and child_number != "" and child_number != "0":
        family_setup = f"spouse and {child_ren}"
        if spouse_COVI == "home" and children_COVI == "home":
            s = f"stayed in {home_country}"
            c = f"resided in {home_country} as well"
        elif spouse_COVI == "host" and children_COVI == "host":
            s = f"accompanied {him_her} to {host_country}"
            c = f"shifted to {host_country} as of the move date of {his_her} {family_setup} on {family_move}"
    elif spouse_COVI == "" and child_number != "" and child_number != "0":
        family_setup == f"{child_ren}"

    COVI_text = f"As {his_her} {family_setup} {s}, {his_her} center of vital interests {c}." 

    return COVI_text

# SECTION 5 - COVI other

def covi_other(payroll_COVI, soc_sec_COVI, assets_COVI, he_she, his_her, home_country, host_country):


    #ellenőrizni, hogy mi hol van és annak megfelelően beállítani a country-t
    #ha nem jelölt semmit, akkor a megfelelő szövegrész legyen csak ""

    
    if payroll_COVI != "":
        if payroll_COVI == "host":
            p_country = host_country
        elif payroll_COVI == "home":
            p_country = home_country
        payroll = f"received {his_her} income through the payroll in {p_country}"
    elif payroll_COVI == "":
        payroll = ""

    if soc_sec_COVI != "":
        if soc_sec_COVI == "host":
            s_country = host_country
            rem_shift = "became"
        elif soc_sec_COVI == "home":
            s_country = home_country
            rem_shift = "remained"
        socsec = f"{rem_shift} insured in the social security system of {s_country}"
    elif soc_sec_COVI == "":
        socsec = ""

    if assets_COVI != "":
        if assets_COVI == "host":
            a_country = host_country
        elif assets_COVI == "home":
            a_country = home_country
        assets = f"had the majority of {his_her} assets in {a_country}"

    COVI_other = f"{he_she} {payroll}, {socsec}, {assets}."
    return COVI_other

# SECTION 6 - Habitual Abode

def hab_abode(last_name, home_days, host_days, home_country, host_country, residency):
    
    habitual_abode = f"As {last_name} spent {home_days} days in {home_country} and {host_days} days in {host_country}, his habitual abode resided in {residency}."

    print(habitual_abode)

# SECTION 7 - Residency Conclusion

def resid_concl(last_name, residency):
    residency_conclusion = f"In line with the above we are of the opinion that {last_name} should be considered a treaty resident in {residency}. Please confirm that you argee with our approach."

    print(residency_conclusion)

# SECTION 8 - TAXATION


def taxation(last_name, his_her, engagement, home_country, host_country, residency, exceed183):
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

    print(x)

# SECTION 9 - Closing

def closing():
    closing = """Thank you for your cooperation. Should you have any questions, please do not hesitate to contact us.

Kind regards,
    """