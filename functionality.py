from datetime import datetime

# variables from program
title = "Mr."
f_name = "Norbert"
l_name = "Adam"
engagement = "Deloitte"
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

full_name = ""
last_name = ""
his_her = ""
he_she = ""
him_her = ""
other_country = ""


# Create the variables used below from user input

def create_variables(title, first_name, last_name, engagement): #home, host): #home_PH_f, home_PH_t, host_PH_f, host_PH_t, home, host, child_number)
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

    # convert provided dates to datetime
    # home_PH_f= datetime.strptime(PH_home_f, '%m/%d/%y')
    # home_PH_f = home_PH_f.strftime('%m %B %y')
    # home_PH_t = datetime.strptime(PH_home_t, '%m/%d/%y')
    # home_PH_t = home_PH_t.strftime('%m %B %y')
    # host_PH_f = datetime.strptime(PH_host_f, '%m/%d/%y')
    # host_PH_f = host_PH_f.strftime('%m %B %y')
    # host_PH_t = datetime.strptime(PH_host_t, '%m/%d/%y')
    # host_PH_t = host_PH_t.strftime('%m %B %y')

    # there is Hungary and "other country" - determine which country is other country
    # if home == "Hungary":
    #     other_country = host
    # else:
    #     other_country = home 

    # if assignee has 1 child --> "child", else "children"
    # ch = ""
    # if int(child_number) == 1:
    #     ch = "child"
    # if int(child_number) > 1:
    #     ch = "children"

    return last_name, he_she, his_her, him_her, engagement

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

# create_variables()