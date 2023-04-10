import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable
from collections import Counter
import json

# This object holds valid tag with their level
# Tag with other key value pair then this will considered as Invalid
allowedTags = {
    'HEAD':'0', 'NOTE':'0', 'NAME':'1', 'INDI': '0', 'SEX': '1', 'BIRT':'1', 'DATE':'2', 'FAM': '0', 
    'FAMS': '1', 'FAMC': '1', 'DEAT': '1', 'HUSB':'1', 'WIFE':'1','CHIL':'1', 'MARR': '1', 'DIV':'1', 
    'TRLR': '0'
}

# Replace your file name here check data for individuals and families
fileName = "Sprint 4/input.ged"

# This function reads file and stor`e all lines in one variable
with open(fileName, 'r') as file:
    lines = file.read().splitlines()
lines = [[line] for line in lines]

sprint4CodeOutput = open("Sprint 4/sprint_4_code_output.txt","a")
sprint4CodeOutput.truncate(0)

# this for loop is finding any gedcom line with errors
# if line is not having tag or level it will set error to lines
for i in range(len(lines)):
    if((len(lines[i][0].split())) < 2):
        lines[i] = "error at line number " + i
    else:
        lines[i] = lines[i][0].split(" ",2)
        if(len(lines[i]) > 2 and lines[i][2] in ["INDI", "FAM"]):
            lines[i][1], lines[i][2] = lines[i][2], lines[i][1]
        elif(len(lines[i]) > 2 and lines[i][1] in ["INDI", "FAM"]):
            lines[i] = "Error at line number " + i

# This array holds all gedcom entries which has valid tag and level
# It will be used for further data processing of individuals and families.
infoList = []
for i in range(len(lines)):
    if(len(lines[i]) > 2):
        # line has valid tag and level it will add to infolist 
        if(lines[i][1] in allowedTags.keys() and allowedTags[lines[i][1]] == lines[i][0]):
            infoList.append((lines[i][0], lines[i][1], lines[i][2]))
        elif(lines[i][0:2] == "In"):
            infoList.append(lines[i])
    # If line has valid tag and level it means it has data of person or family
    elif(len(lines[i]) == 2):
        if((lines[i][1] in allowedTags.keys()) and allowedTags[lines[i][1]] == lines[i][0]):
            infoList.append((lines[i][0], lines[i][1]))

# Removing unwanted data
# this line is used to remove HEAD tag
infoList.pop(0)
# This line is used to remove TRLR tag
infoList.pop(-1)
# This line is used to remove lines which has level 1 and tag birt
infoList = list(filter((('1', 'BIRT')).__ne__, infoList))

# Flag variable to determing when to stop crawling for individuals
shouldBreak = False
# This both object holds data with tag for individuals and family where key will be id of individual and family
individualsData = {}
familiesData = {}
# Iterating infolist to get infomation of individuals
for i in range(len(infoList)):
    # This array holds array of tag and its value
    vals = []
    j = i + 1
    if(infoList[i][1] == 'INDI' and infoList[i][0] == '0'):
        # this loop will get all infomation about individual
        while(infoList[j][1] != 'INDI'):
            # Key holds the ID of specific individuals
            key = infoList[i][2][1:-1]
            # If we found beggining of family records we will stop execution for individual data gathering
            if(infoList[j][1] == 'FAM' and infoList[j][0] == '0'):
                shouldBreak = True
                break
            elif(infoList[j][1] == 'DEAT' and infoList[j][2] == 'Y'):
                vals.append(('DEAT', infoList[j+1][2]))
                j += 1
            elif(infoList[j][1] == 'FAMC' or infoList[j][1] == 'FAMS'):
                vals.append((infoList[j][1], infoList[j][2][1:-1]))
            else:
                vals.append((infoList[j][1], infoList[j][2]))
            j += 1
        individualsData.update({key: vals})
        if(shouldBreak):
            break

# Columns of individuals table
individualsTable = PrettyTable(["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"])
# This array holds array of individual information
individuals = []

# Iteraing over individuals data and getting only values needed for output
for key, value in individualsData.items():
    age = 0
    name = ""
    gender = ""
    birthday = ""
    death = "NA"
    isAlive = False
    for i in range(len(value)):
        famc = []
        fams = []
        if(value[i][0] == "NAME"):
            temp = value[i][1]
            if(len(temp) == 0):
                temp = "NA"
            name = temp

        if(value[i][0] == "SEX"):
            temp = value[i][1]
            if(len(temp) == 0):
                temp = "NA"
            gender = temp

        if(value[i][0] == "DATE"):
            temp = datetime.datetime.strptime(value[i][1], "%d %b %Y").date()
            if(len(str(temp)) == 0):
                temp = "NA"
            birthday = temp

        if(value[i][0] == "DEAT"):
            temp = datetime.datetime.strptime(value[i][1], "%d %b %Y").date()
            if(len(str(temp)) == 0):
                temp = "NA"
            death = temp

        if(value[i][0] == "FAMC"):
            temp = value[i][1]
            if(len(temp) == 0):
                temp = "NA"
            famc.append(temp)

        if(value[i][0] == "FAMS"):
            temp = value[i][1]
            if(len(temp) == 0):
                temp = "NA"
            fams.append(temp)
    # Finding is individual alive or not. 
    if(any("DEAT" in i for i in value)):
        age = relativedelta(death, birthday).years
    else:
        age = relativedelta(datetime.datetime.now(), birthday).years
        isAlive = True

    # Formating array representation
    if(len(famc) == 0):
        famc = "NA"
    else:
        famc = str(famc)
        famc = famc.replace("[", "{").replace("]", "}")

    if(len(fams) == 0):
        fams = "NA"
    else:
        fams = str(fams)
        fams = fams.replace("[", "{").replace("]", "}")
    
    individuals.append([key, name, gender, str(birthday), age, isAlive, str(death), famc, fams])

individualsTable.add_rows(individuals)

# Showing individuals details
# print("Individuals")
# print(individualsTable)
print("Individuals", file=sprint4CodeOutput)
print(individualsTable, file=sprint4CodeOutput)

# Iterating over infolist of gather information for families
for i in range(len(infoList)):
    # This array variable holds array of tag regarding family and its value
    vals = []
    j = i + 1
    if(infoList[i][1] == 'FAM' and infoList[i][0] == '0'):
        while(j < len(infoList)):
            key = infoList[i][2][1:-1]
            # This if block find individuals id for spouce and childern
            if(infoList[j][1] != "MARR" and infoList[j][1] != "DIV" and infoList[j][1] != "DATE" and infoList[j][1] != "FAM"):
                vals.append((infoList[j][1], infoList[j][2][1:-1]))
            # This else if block find divorce date if there is any happen
            elif(infoList[j][1] == "DIV" and len(infoList[j+1]) > 2):
                vals.append(("DIV", infoList[j+1][2]))
            # This else if block finds marriage date
            elif(infoList[j][1] == "MARR" and len(infoList[j+1]) > 2):
                vals.append(("MARR", infoList[j+1][2]))
            # If new family is started then this loop is stopped
            elif(infoList[j][1] == "FAM" and infoList[j][0] == "0"):
                break
            j += 1
        familiesData.update({key: vals})
        
# Columns names for family table
famliesTable = PrettyTable(["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"])
# This array holds array of family details
families = []
for key, value in familiesData.items():
    innerChild = []
    married = ""
    divorce = ""
    husbandId = 0
    wifeId = 0
    husbandName = ""
    wifeName = ""
    for i in range(len(value)):
        # This finds husband name
        if(value[i][0] == "HUSB"):
            husbandId = value[i][1]
            if husbandId in individualsData:
                husbandName = individualsData[husbandId][0][1]
        # This finds wife name
        if(value[i][0] == "WIFE"):
            wifeId = value[i][1]
            if wifeId in individualsData:
                wifeName = individualsData[wifeId][0][1]
        # This collect children name in array
        if(value[i][0] == "CHIL"):
            child = value[i][1]
            innerChild.append(child)
        # This finds marriage date
        if(value[i][0] == "MARR"):
            married = datetime.datetime.strptime(value[i][1],"%d %b %Y").date()
        # This finds divorce date
        if(value[i][0] == "DIV"):
            divorce = datetime.datetime.strptime(value[i][1], "%d %b %Y").date()
    tempArr = [key, married, divorce, husbandId, husbandName, wifeId, wifeName]
    # Putting NA to data if there is no data.
    for i in range(len(tempArr)):
        if(len(str(tempArr[i])) == 0):
            tempArr[i] = "NA"
    # Formatting array reprentation
    if(len(innerChild) == 0):
        innerChild = "NA"
    else:
        innerChild = str(innerChild)
        innerChild = innerChild.replace("[", "{").replace("]", "}")
    tempArr.append(innerChild)
    families.append(tempArr)

# Adding family details to family table
famliesTable.add_rows(families)

# Showing family table
# print("Families")
# print(famliesTable)
print("Families", file=sprint4CodeOutput)
print(famliesTable, file=sprint4CodeOutput)


# Declaring constant for indexes of individuals and family
IDX_IND_ID = 0
IDX_IND_NAME = 1
IDX_IND_GENDER = 2
IDX_IND_BIRTHDAY = 3
IDX_IND_AGE = 4
IDX_IND_ALIVE = 5
IDX_IND_DEATH = 6
IDX_IND_CHILD = 7
IDX_IND_SPOUCE = 8

IDX_FAM_ID = 0
IDX_FAM_MARRIED = 1
IDX_FAM_DIVORCED = 2
IDX_FAM_HUSBAND_ID = 3
IDX_FAM_HUSBAND_NAME = 4
IDX_FAM_WIFE_ID = 5
IDX_FAM_WIFE_NAME = 6
IDX_FAM_CHILD = 7


# User story US03 
# Story Name: Birth before death
# Owner: Parth Paghdal (pp)
# Email: ppaghdal@stevens.edu
def us03_birth_before_death():
    data = []
    # Iterating over individuals data and finding birth and death date
    for individual in individuals:
        death = individual[IDX_IND_DEATH]
        birth = individual[IDX_IND_BIRTHDAY]
        if(death == "NA") :
            continue
        if(birth == "NA"):
            continue
        # Converting string date to date object
        birth = datetime.datetime.strptime(birth, "%Y-%m-%d").date()
        death = datetime.datetime.strptime(death, "%Y-%m-%d").date()
        
        # Comparing birth and death date to find death should not occure before birth 
        if(birth > death) :
            data.append("Error: INDIVIDUAL US03 "  + str(individual[0])+": "+ "named: "+ str(individual[1]) + " Died: "+ str(individual[6] + " before born at " + str(individual[3])))
    return data

data = us03_birth_before_death()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US30
# Story Name: List living married
# Owner: Parth Paghdal (pp)
# Email: ppaghdal@stevens.edu
def us30_list_living_married():
    data = []
    # Iterating over families to find out married couple
    for family in families:
        isStillMarried = family[IDX_FAM_DIVORCED] == "NA"
        if(isStillMarried):
            husbandId = family[IDX_FAM_HUSBAND_ID]
            husbandName = family[IDX_FAM_HUSBAND_NAME]
            wifeId = family[IDX_FAM_WIFE_ID]
            wifeName = family[IDX_FAM_WIFE_NAME]
            isBothAlive = True
            # Checking husband and wife are alive using individuals detail list
            for individual in individuals:
                if(individual[IDX_IND_ID] == husbandId or individual[IDX_IND_ID] == wifeId):
                    if(individual[IDX_IND_ALIVE] == False):
                        isBothAlive = False
            # If both are alive then adding record to data
            if(isBothAlive):
                data.append("Error: Family US30 Family id "+ str(family[0])+ " husband name: "+husbandName+ " and wife name: "+ wifeName+ " both are still living married couple.")
    return data

data = us30_list_living_married()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

#User Story US29
#Story Name: List deceased
#Owner:Sai Krishna (km)
#Email : smiriyal@stevens.edu
# Set up the GEDCOM parser.
def us_29_List_deceased():

    data = []
    for individual in individuals:
        if(individual[IDX_IND_DEATH] != "NA"):
            data.append("Error: Individual US29 "+ individual[IDX_IND_ID]+" : named: "+individual[IDX_IND_NAME]+" died on: "+individual[IDX_IND_DEATH])
    return data
data = us_29_List_deceased()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)


# User story US31
# Story Name: List living single
# Owner: Manoj Patel (mp)
# Email: mpateld@stevens.edu
def us31_list_living_single():
    data = []
    idOfPeopleWhoAreMarriedAtleastOne = []
    for family in families:
        idOfPeopleWhoAreMarriedAtleastOne.append(family[IDX_FAM_HUSBAND_ID])
        idOfPeopleWhoAreMarriedAtleastOne.append(family[IDX_FAM_WIFE_ID])
    for individual in individuals:
        age = individual[IDX_IND_AGE]
        if(age < 30):
            continue
        if(individual[IDX_IND_ID] in idOfPeopleWhoAreMarriedAtleastOne):
            continue
        if(individual[IDX_IND_DEATH] != "NA"):
            continue
        data.append("Error: INDIVIDUAL US31 "+ str(individual[IDX_IND_ID])+ " named: "+individual[IDX_IND_NAME]+" is alive, over 30 year old and never married")
    return data

data = us31_list_living_single()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US05
# Story Name: Marriage before death
# Owner: Manoj Patel (mp)
# Email: mpateld@stevens.edu
def us05_marriage_before_death():
    data = []
    for family in families:
        husbandId = family[IDX_FAM_HUSBAND_ID]
        wifeId = family[IDX_FAM_WIFE_ID]
        marriageDate = family[IDX_FAM_MARRIED]

        isHusbandAlive = True
        isWifeAlive = True
        husbandDeath = None
        wifeDeath = None
        for individual in individuals:
            if individual[IDX_IND_ID] == husbandId:
                isHusbandAlive = individual[IDX_IND_ALIVE]
                if not isHusbandAlive:
                    husbandDeath = datetime.datetime.strptime(individual[IDX_IND_DEATH], "%Y-%m-%d").date()
            if individual[IDX_IND_ID] == wifeId:
                isWifeAlive = individual[IDX_IND_ALIVE]
                if not isWifeAlive:
                    wifeDeath = datetime.datetime.strptime(individual[IDX_IND_DEATH], "%Y-%m-%d").date()
        if isHusbandAlive and isWifeAlive:
            continue
        else:
            if not isHusbandAlive and (husbandDeath != None and marriageDate > husbandDeath):
                data.append("ERROR: US05 Family: "+ str(family[IDX_IND_ID]) + " husband died on "+str(husbandDeath)+" before his marriage date "+str(marriageDate))
            elif not isWifeAlive and (wifeDeath != None and marriageDate > wifeDeath):
                data.append("ERROR: US05 Family: "+ str(family[IDX_IND_ID]) + " wife died on "+str(wifeDeath)+" before her marriage date "+str(marriageDate))
    return data

data = us05_marriage_before_death()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US16
# Story Name: Male Last Names
# Owner: Ambati Baby Naga Sahithya (sa)
# Email: bambati@stevens.edu
def us16_male_last_names():
    data = []

    for family in families:
        husbandName = family[IDX_FAM_HUSBAND_NAME]
        names = husbandName.split("/")
        if(len(names) < 2):
            continue
        familyLastName = names[1].strip()
        children_ids = family[IDX_FAM_CHILD]
        children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")
        for individual in individuals:
            if(individual[IDX_IND_ID] not in children_ids):
                continue
            if(individual[IDX_IND_GENDER] != "M"):
                continue
            name = individual[IDX_IND_NAME].split("/")
            if(len(name) < 2):
                continue
            lastName = name[1]
            if(lastName != familyLastName):
                data.append("ERROR US16 Family: "+str(family[IDX_IND_ID])+ " is having child named: "+ individual[IDX_IND_NAME]+" is having different last name")
    return data

data = us16_male_last_names()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US28
# Story Name: order siblings by age
# Owner: Ambati Baby Naga Sahithya (sa)
# Email: bambati@stevens.edu
def us28_order_siblings_by_age():
    data = []
   
    for family in families:
        children_ids = family[IDX_FAM_CHILD]
        children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")
        childrens = []
        for child in children_ids:
            for individual in individuals:
                if child == individual[IDX_IND_ID]:
                    childrens.append(individual)
        if(len(childrens) <= 0):
            continue
        childrens = sorted(childrens, key=lambda x: x[IDX_IND_AGE], reverse= True)
        outputString = "ERROR: US28 FAMILY: "+ str(family[IDX_FAM_ID])+" sorted siblings (oldest first): "
        for child in childrens:
            outputString += "ID:"+str(child[IDX_IND_ID])+" Age: "+ str(child[IDX_IND_AGE])+" |-| "
        outputString = outputString[:-5]
        data.append(outputString)
    return data

data = us28_order_siblings_by_age()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

#User Story US12
#Story Name: Parents not too old
#Owner: Sai Krishna (km), Parth Paghdal (pp)
#Email : smiriyal@stevens.edu, ppaghdal@stevens.edu
#Note: this user story is backlog from Sprint 1
#       This user story done using pair programming with Parth Paghdal (pp)
def us12_parents_not_too_old():
    data = []
    for family in families:
        fatherId = family[IDX_FAM_HUSBAND_ID]
        motherId = family[IDX_FAM_WIFE_ID]

        fatherName = family[IDX_FAM_HUSBAND_NAME]
        motherName = family[IDX_FAM_WIFE_NAME]

        children_ids = family[IDX_FAM_CHILD]
        children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")

        fatherAge = None
        motherAge = None
        for individual in individuals:
            if individual[IDX_IND_ID] == fatherId:
                fatherAge = individual[IDX_IND_AGE]
            if individual[IDX_IND_ID] == motherId:
                motherAge = individual[IDX_IND_AGE]
            if fatherAge != None and motherAge != None:
                break
        
        for individual in individuals:
            if individual[IDX_IND_ID] in children_ids:
                childAge = individual[IDX_IND_AGE]
                if motherAge - childAge > 60:
                    data.append("ERROR: US12 Family: "+ str(family[IDX_IND_ID])+" mother named: "+ motherName+" and age:" + str(motherAge)+ " more than 60 year than her child named: "+ individual[IDX_IND_NAME]+" with age "+ str(individual[IDX_IND_AGE]))
                if fatherAge - childAge > 80:
                    data.append("ERROR: US12 Family: "+ str(family[IDX_IND_ID])+" father named: "+ fatherName+" and age:" + str(fatherAge)+ " more than 80 year than his child named: "+ individual[IDX_IND_NAME]+" with age "+ str(individual[IDX_IND_AGE]))
    return data
data = us12_parents_not_too_old()
print(*data, sep="\n")            
print(*data, sep="\n", file=sprint4CodeOutput)


# User story US01
# Story Name: Dates before current date
# Owner: Parth Paghdal (pp)
# Email: ppaghdal@stevens.edu
# This story is implemented individually for finding difference between pair programming and individually
def us01_dates_before_current_date():
    data = []
    todaysDate = datetime.datetime.now().date()
    for individual in individuals:
        birthday = individual[IDX_IND_BIRTHDAY]
        
        if birthday != "NA":
            birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
            if birthday > todaysDate:
                data.append("ERROR US01: Individual: "+ str(individual[IDX_IND_ID])+" named "+ str(individual[IDX_IND_NAME])+" has future birthdate "+ str(birthday)+" in regards to todays' date.")

        if(individual[IDX_IND_DEATH] == "NA"):
            continue
        deathday = individual[IDX_IND_DEATH]
        deathday = datetime.datetime.strptime(deathday, "%Y-%m-%d").date()
        if deathday > todaysDate:
            data.append("ERROR US01: Individual: "+ str(individual[IDX_IND_ID])+" named "+ str(individual[IDX_IND_NAME])+" has future deathdate "+ str(deathday)+" in regards to todays' date.")

    for family in families:
        if family[IDX_FAM_MARRIED] != "NA":
            marriageDate = family[IDX_FAM_MARRIED]
            if marriageDate > todaysDate:
                data.append("ERROR US01: Family: "+ str(family[IDX_FAM_ID])+" has future marriage date "+ str(marriageDate)+" in regards to todays' date.")
        if family[IDX_FAM_DIVORCED] != "NA":
            divorceDate = family[IDX_FAM_DIVORCED]
            if divorceDate > todaysDate:
                data.append("ERROR US01: Family: "+ str(family[IDX_FAM_ID])+" has future divorce date "+ str(divorceDate)+" in regards to todays' date.")
        
    return data

data = us01_dates_before_current_date()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US02
# Story Name: Birth before marriage
# Owner: Parth Paghdal (pp)
# Email: ppaghdal@stevens.edu
def us02_birth_before_marriage():
    data = []
    for family in families:
        husbandId = family[IDX_FAM_HUSBAND_ID]
        wifeId = family[IDX_FAM_WIFE_ID]
        marriageDate = family[IDX_FAM_MARRIED]
        if marriageDate == "NA":
            continue
        
        for individual in individuals:
            if individual[IDX_IND_ID] == husbandId:
                husbandBirthDay = individual[IDX_IND_BIRTHDAY]
                if husbandBirthDay != "NA":
                    husbandBirthDay = datetime.datetime.strptime(husbandBirthDay, "%Y-%m-%d").date()
                    if (husbandBirthDay > marriageDate):
                        data.append("ERROR: US02 Individual: "+ str(husbandId)+ " husband named "+ str(individual[IDX_IND_NAME])+ " has future birthdate "+ str(husbandBirthDay)+ " in regards to his marriage date "+ str(marriageDate))
            
            if individual[IDX_IND_ID] == wifeId:
                wifeBirthday = individual[IDX_IND_BIRTHDAY]
                if wifeBirthday != "NA":
                    wifeBirthday = datetime.datetime.strptime(wifeBirthday, "%Y-%m-%d").date()
                    if (wifeBirthday > marriageDate):
                        data.append("ERROR: US02 Individual: "+ str(wifeId)+ " wife named "+ str(individual[IDX_IND_NAME])+ " has future birthdate "+ str(wifeBirthday)+ " in regards to her marriage date "+ str(marriageDate))
            
    return data

data = us02_birth_before_marriage()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

#User Story US25
#Story Name: Unique first names in families
#Owner: Sai Krishna (km)
#Email : smiriyal@stevens.edu
def us_25_unique_first_names_in_families():
    data = []
    for family in families:
        children_ids = family[IDX_FAM_CHILD]
        children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")
        childrenBirthName = []
        for individual in individuals:
            if individual[IDX_IND_ID] in children_ids:
                name = individual[IDX_IND_NAME]
                birthday = individual[IDX_IND_BIRTHDAY]
                childrenBirthName.append((name, birthday))
        temp = dict(Counter(childrenBirthName))
        for key, value in temp.items():
            if value > 1:
                data.append("ERROR: US25 FAMILY: "+ str(family[IDX_FAM_ID])+ " is having "+ str(value) + " children with same name: "+ str(key[0]) + " and same birthdate: "+ str(key[1]))

    return data

data = us_25_unique_first_names_in_families()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

#User Story US10
#Story Name: Marriage after 14
#Owner: Sai Krishna (km)
#Email : smiriyal@stevens.edu
def us_10_marriage_after_14():
    data = []
    for family in families:
        husbandId = family[IDX_FAM_HUSBAND_ID]
        wifeId = family[IDX_FAM_WIFE_ID]
        marriageDate = family[IDX_FAM_MARRIED]
        for individual in individuals:
            if individual[IDX_IND_ID] == husbandId:
                husbandBirthday = individual[IDX_IND_BIRTHDAY]
                if husbandBirthday != "NA":
                    husbandBirthday = datetime.datetime.strptime(husbandBirthday, "%Y-%m-%d").date()
                    diffInDays = (marriageDate - husbandBirthday).days
                    years = diffInDays // 365
                    if years < 14:
                        data.append("ERROR: US10 FAMILY: "+ str(family[IDX_IND_ID]) + " has husband named: "+ str(family[IDX_FAM_HUSBAND_NAME])+ " born on "+ str(husbandBirthday)+" and got married on "+ str(marriageDate)+ " and this time difference is less than 14 years")
            if individual[IDX_IND_ID] == wifeId:
                wifeBirthday = individual[IDX_IND_BIRTHDAY]
                if wifeBirthday != "NA":
                    wifeBirthday = datetime.datetime.strptime(wifeBirthday, "%Y-%m-%d").date()
                    diffInDays = (marriageDate - wifeBirthday).days
                    years = diffInDays // 365
                    if years < 14:         
                        data.append("ERROR: US10 FAMILY: "+ str(family[IDX_IND_ID]) + " has wife named: "+ str(family[IDX_FAM_WIFE_NAME])+ " born on "+ str(wifeBirthday)+" and got married on "+ str(marriageDate)+ " and this time difference is less than 14 years")
    return data


data = us_10_marriage_after_14()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US04
# Story Name: Marriage before divorce
# Owner: Ambati Baby Naga Sahithya (sa)
# Email: bambati@stevens.edu
def us_04_marriage_before_divorce():
    data = []
    for family in families:
        marriageDate = family[IDX_FAM_MARRIED]
        divorceDate = family[IDX_FAM_DIVORCED]
        if marriageDate == "NA" or divorceDate == "NA":
            continue
        if divorceDate < marriageDate:
            data.append("ERROR: US04 FAMILY: " + str(family[IDX_FAM_ID]) + " is having future marriage date " + str(
                marriageDate) + " in reagrds to divorce date " + str(divorceDate))
    return data


data = us_04_marriage_before_divorce()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)


# User story US06
# Story Name: Divorce before death
# Owner: Ambati Baby Naga Sahithya (sa)
# Email: bambati@stevens.edu
def us_06_divorce_before_death():
    data = []
    for family in families:
        divorceDate = family[IDX_FAM_DIVORCED]
        if divorceDate == "NA":
            continue
        husbandId = family[IDX_FAM_HUSBAND_ID]
        wifeId = family[IDX_FAM_WIFE_ID]
        for individual in individuals:
            if individual[IDX_IND_ID] == husbandId:
                deathDate = individual[IDX_IND_DEATH]
                if deathDate != "NA":
                    deathDate = datetime.datetime.strptime(deathDate, "%Y-%m-%d").date()
                    if (divorceDate > deathDate):
                        data.append("ERROR: US06 FAMILY: " + str(family[IDX_FAM_ID]) + " divorce happened at " + str(
                            divorceDate) + " which is after the death of husband on " + str(deathDate))

            if individual[IDX_IND_ID] == wifeId:
                deathDate = individual[IDX_IND_DEATH]
                if deathDate != "NA":
                    deathDate = datetime.datetime.strptime(deathDate, "%Y-%m-%d").date()
                    if (divorceDate > deathDate):
                        data.append("ERROR: US06 FAMILY: " + str(family[IDX_FAM_ID]) + " divorce happened at " + str(
                            divorceDate) + " which is after the death of wife on " + str(deathDate))

    return data


data = us_06_divorce_before_death()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US08
# Story Name: Birth before marriage of parents
# Owner: Manoj Patel (mp)
# Email: mpateld@stevens.edu
def us_08_birth_before_marriage_of_parents():
    data = []
    for family in families:
        marriageDate = family[IDX_FAM_MARRIED]
        divorceDate = family[IDX_FAM_DIVORCED]
        children_ids = family[IDX_FAM_CHILD]
        children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")
        for individual in individuals:
            birthday = individual[IDX_IND_BIRTHDAY]
            if birthday != "NA" and individual[IDX_IND_ID] in children_ids:
                birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
                if marriageDate != "NA" and birthday < marriageDate:
                    data.append("ERROR: US08 FAMILY "+ str(family[IDX_FAM_ID])+ " is having child named "+ individual[IDX_IND_NAME] + " born on "+ str(birthday)+" which is earlier than parents' marriage date "+ str(marriageDate))

                if divorceDate != "NA":
                    newDivorceDate = divorceDate + relativedelta(month=+9)
                    if birthday > newDivorceDate:
                        data.append("ERROR: US08 FAMILY "+ str(family[IDX_FAM_ID])+ " is having child named "+ individual[IDX_IND_NAME]+ " born "+ str(birthday)+ " which is 9 months after the parents' divorce date "+ str(divorceDate))
    return data

data = us_08_birth_before_marriage_of_parents()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US09
# Story Name: Birth before death of parents
# Owner: Manoj Patel (mp)
# Email: mpateld@stevens.edu
def us_09_birth_before_death_of_parents():
    data = []
    for family in families:
        marriageDate = family[IDX_FAM_MARRIED]
        divorceDate = family[IDX_FAM_DIVORCED]
        children_ids = family[IDX_FAM_CHILD]
        children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")
        motherDeathDate = "NA"
        motherId = family[IDX_FAM_WIFE_ID]
        fatherDeathDate = "NA"
        fatherId = family[IDX_FAM_HUSBAND_ID]

        for individual in individuals:
            if individual[IDX_IND_ID] == fatherId:
                fatherDeathDate = individual[IDX_IND_DEATH]

            if individual[IDX_IND_ID] == motherId:
                motherDeathDate = individual[IDX_IND_DEATH]
        if motherDeathDate != "NA" and fatherDeathDate != "NA":
            motherDeathDate = datetime.datetime.strptime(motherDeathDate, "%Y-%m-%d").date()
            fatherDeathDate = datetime.datetime.strptime(fatherDeathDate, "%Y-%m-%d").date()
                    
        for individual in individuals:
            birthday = individual[IDX_IND_BIRTHDAY]
            if birthday != "NA" and individual[IDX_IND_ID] in children_ids:
                birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
                
                if motherDeathDate != "NA":
                    if motherDeathDate < birthday:
                        data.append("ERROR: US09 FAMILY "+ str(family[IDX_FAM_ID])+ " is having child named " + str(individual[IDX_IND_NAME])+ " who is born on "+str(birthday)+" after death of mother on "+ str(motherDeathDate))
                
                if fatherDeathDate != "NA":
                    fatherNewDeathDate = fatherDeathDate - relativedelta(month=9)
                    if birthday > fatherNewDeathDate:
                        data.append("ERROR: US09 FAMILY "+ str(family[IDX_IND_ID])+ " is having child named "+ str(individual[IDX_IND_NAME]) + " who is born on "+ str(birthday)+ " after 9 months of father death on "+ str(fatherDeathDate))
    return data

data = us_09_birth_before_death_of_parents()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US13 
# Story Name: Siblings spacing
# Owner: Parth Paghdal (pp)
# Email: ppaghdal@stevens.edu
def us_13_siblings_spacing():
    data = []
    for family in families:
        children_ids = family[IDX_FAM_CHILD]
        children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")
        childInfomation = []
        for individual in individuals:
            if individual[IDX_IND_ID] in children_ids:
                birthday = individual[IDX_IND_BIRTHDAY]
                if birthday != "NA":
                    birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
                    newIndividual = individual.copy()
                    newIndividual[IDX_IND_BIRTHDAY] = birthday
                    childInfomation.append(newIndividual)

        childInfomation = sorted(childInfomation, key= lambda x: x[IDX_IND_BIRTHDAY])

        for i in range(len(childInfomation) - 1):
            diff = childInfomation[i+1][IDX_IND_BIRTHDAY] - childInfomation[i][IDX_IND_BIRTHDAY]
            if diff < timedelta(days=2) or diff > timedelta(days=240):
                id = childInfomation[i][IDX_IND_ID]
                name = childInfomation[i][IDX_IND_NAME]
                birthday = childInfomation[i][IDX_IND_BIRTHDAY]
                hisOrHer = "her" if childInfomation[i][IDX_IND_GENDER] == "F" else "his"
                siblingName = childInfomation[i+1][IDX_IND_NAME]
                siblingId = childInfomation[i+1][IDX_IND_ID]
                siblingBirthday = childInfomation[i+1][IDX_IND_BIRTHDAY]
                data.append("ERROR: US13 Individual " + str(id)+" named "+name+ " born on "+ str(birthday)+ " is either born before 8 months or less than 2 days apart "+hisOrHer+" sibling id "+str(siblingId)+" named "+ str(siblingName)+" born on "+str(siblingBirthday))
    return data

data = us_13_siblings_spacing()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US26
# Story Name: Corresponding entries
# Owner: Parth Paghdal (pp)
# Email: ppaghdal@stevens.edu
def us_26_corresponding_entries():
    data = []
    individualDict = {}
    for individual in individuals:
        dict = {}
        if individual[IDX_IND_CHILD] != "NA":
            children_ids = individual[IDX_IND_CHILD]
            children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")
            dict["child"] = children_ids
        if individual[IDX_IND_SPOUCE] != "NA":
            spouceIds = individual[IDX_IND_SPOUCE]
            spouceIds = spouceIds.replace("{", "").replace("}","").replace("'","").replace(" ", "").split(",")
            dict["spouce"] = spouceIds
        individualDict[individual[IDX_IND_ID]] = dict
    
    familyDict = {}
    for family in families:
        dict = {}
        dict["husband"] = family[IDX_FAM_HUSBAND_ID]
        dict["wife"] = family[IDX_FAM_WIFE_ID]
        if family[IDX_FAM_CHILD] != "NA":
            children_ids = family[IDX_FAM_CHILD]
            children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")
            dict["children"] = children_ids
        familyDict[family[IDX_FAM_ID]] = dict


    for familyId, family in familyDict.items():
        for spouce in ["husband", "wife"]:
            if spouce in family:
                spouce_id = family[spouce]
                if spouce_id not in individualDict:
                    data.append("ERROR: US26 FAMILY "+ familyId + " is having spouce "+ spouce_id+ " whose id not found in individual table.")
        if "children" in family:
            for child_id in family["children"]:
                if child_id not in individualDict:
                    data.append("ERROR: US26 FAMILY "+ familyId+ " is having child "+ child_id+" whose id not found in individual table.")

    for individualId, individual in individualDict.items():
        if "spouce" in individual:
            for familyId in individual["spouce"]:
                if familyId not in familyDict:
                    data.append("ERROR: US26 INDIVIDUAL "+ individualId + " is not having record in family table.")
        if "child" in individual:
            for familyId in individual["child"]:
                if familyId not in familyDict:
                    data.append("ERROR: US26 INDIVIDUAL "+ individualId + " is child of family "+ familyId+ " but record not found in family table.")

    return data

data = us_26_corresponding_entries()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

#User Story US14
#Story Name: Multiple births <= 5
#Owner: Sai Krishna (km)
#Email : smiriyal@stevens.edu
def us_14_multiple_births():
    data = []
    for family in families:
        familyId = family[IDX_FAM_ID]
        children_ids = family[IDX_FAM_CHILD]
        children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")
        birthDates = {}
        for individual in individuals:
            if individual[IDX_IND_ID] in children_ids:
                if individual[IDX_IND_BIRTHDAY] != "NA":
                    birthday = individual[IDX_IND_BIRTHDAY]
                    if birthday in birthDates:
                        birthDates[birthday] = birthDates[birthday] + 1
                    else:
                        birthDates[birthday] = 1
        for birthdate, count in birthDates.items():
            if(count > 5):
                data.append("ERROR: US14 FAMILY "+ familyId+ " is having more than 5 children born on "+ birthdate)

    return data

data = us_14_multiple_births()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

#User Story US18
#Story Name: Siblings should not marry
#Owner: Sai Krishna (km)
#Email : smiriyal@stevens.edu
def us_18_siblings_should_not_marry():
    data = []
    for family in families:
        familyId = family[IDX_FAM_ID]
        children_ids = family[IDX_FAM_CHILD]
        children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")
        for family2 in families:
            husbandId = family2[IDX_FAM_HUSBAND_ID]
            wifeId = family2[IDX_FAM_WIFE_ID]
            if(husbandId in children_ids and wifeId in children_ids):
                data.append("ERROR: US18 FAMILY "+ familyId+" is having siblings "+ husbandId + " and "+ wifeId+ " are married to each other.")
    return data

data = us_18_siblings_should_not_marry()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US22
# Story Name: Unique IDs
# Owner: Ambati Baby Naga Sahithya (sa)
# Email: bambati@stevens.edu
def us_22_unique_ids():
    data = []
    individualDuplicates = []
    individualSeen = set()
    for individual in individuals:
        if individual[IDX_IND_ID] in individualSeen:
            individualDuplicates.append(individual)
        else:
            individualSeen.add(individual[IDX_IND_ID])
    
    familyDuplicates = []
    familySeen = set()
    for family in families:
        if family[IDX_FAM_ID] in familySeen:
            familyDuplicates.append(family)
        else:   
            familySeen.add(family[IDX_FAM_ID])
    
    for individualDuplicate in individualDuplicates:
        data.append("ERROR: US22 INDIVIDUAL "+ individualDuplicate[IDX_IND_ID]+" unique id rule is violated this time name is "+ individualDuplicate[IDX_IND_NAME])
    
    for familyDuplicate in familyDuplicates:
        data.append("ERROR: US22 FAMILY "+ familyDuplicate[IDX_FAM_ID]+" unique id rule for family id is violated.")
    return data

data = us_22_unique_ids()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US23
# Story Name: Unique name and birth date
# Owner: Ambati Baby Naga Sahithya (sa)
# Email: bambati@stevens.edu
def us_23_unique_name_and_birth_date():
    data = []

    tempIds = []
    for i in range(len(individuals)):
        for j in range(i+1, len(individuals)):
            a = individuals[i]
            b = individuals[j]
            if a[IDX_IND_NAME] == b[IDX_IND_NAME] and a[IDX_IND_BIRTHDAY] == b[IDX_IND_BIRTHDAY]:
                data.append("ERROR US23 INDIVIDUAL "+ a[IDX_IND_ID] +" is having duplicate record with same name "+ a[IDX_IND_NAME]+" and same birthdate "+ a[IDX_IND_BIRTHDAY])
                data.append("ERROR US23 INDIVIDUAL "+ b[IDX_IND_ID] +" is having duplicate record with same name "+ b[IDX_IND_NAME]+" and same birthdate "+ b[IDX_IND_BIRTHDAY])

    return data

data = us_23_unique_name_and_birth_date()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)


# User story US15
# Story Name: Fewer than 15 siblings
# Owner: Manoj Patel (mp)
# Email: mpateld@stevens.edu
def us_15_fewer_then_15_siblings():
    data = []
    for family in families:
        children_ids = family[IDX_FAM_CHILD]
        children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")
        if len(children_ids) > 15:
            data.append("ERROR: US15 FAMILY "+ family[IDX_FAM_ID]+ " is having more than 15 siblings.")
    return data

data = us_15_fewer_then_15_siblings()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US20
# Story Name: Aunts and uncles
# Owner: Manoj Patel (mp)
# Email: mpateld@stevens.edu
def us_20_aunts_and_uncles():
    data = []

    arrayofChildWithUncleAndAunts = []
    for family in families:
        fatherId = family[IDX_FAM_HUSBAND_ID]
        motherId = family[IDX_FAM_WIFE_ID]
        children_ids = family[IDX_FAM_CHILD]
        children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")
        for childId in children_ids:
            arrayofChildWithUncleAndAunts.append({"childId":childId, "fatherId":fatherId, "motherId": motherId, "uncleAuntsOfThisChild": []})
    for family in families:
        fatherId = family[IDX_FAM_HUSBAND_ID]
        motherId = family[IDX_FAM_WIFE_ID]
        children_ids = family[IDX_FAM_CHILD]
        children_ids = children_ids.replace("{", "").replace("}", "").replace("'","").replace(" ","").split(",")
        for childId in children_ids:
            matchingObjects = [obj for obj in arrayofChildWithUncleAndAunts if obj["fatherId"] == childId or obj["motherId"] == childId]
            if matchingObjects is not None:
                for matchingObject in matchingObjects:
                    matchingObject["uncleAuntsOfThisChild"].extend(children_ids)

    for family in families:
        familyId = family[IDX_FAM_ID]
        husbandId = family[IDX_FAM_HUSBAND_ID]
        wifeId = family[IDX_FAM_WIFE_ID]
        matchingObjects = [obj for obj in arrayofChildWithUncleAndAunts if obj["childId"] == husbandId]
        if len(matchingObjects) != 0:
            for matchedObject in matchingObjects:
                if wifeId in matchedObject["uncleAuntsOfThisChild"]:
                    data.append("ERROR US20 FAMILY "+ familyId+ " husband "+ husbandId + " is married to his aunt "+ wifeId)
        matchingObjects = [obj for obj in arrayofChildWithUncleAndAunts if obj["childId"] == wifeId]
        if len(matchingObjects) != 0:
            for matchedObject in matchingObjects:
                if husbandId in matchedObject["uncleAuntsOfThisChild"]:
                    data.append("ERROR US20 FAMILY "+ familyId+ " wife "+ wifeId + " is married to her uncle "+ husbandId)                    
    return data

data = us_20_aunts_and_uncles()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US07
# Story Name: Less then 150 years old
# Owner: Parth Paghdal (pp)
# Email: ppaghdal@stevens.edu
def us_07_less_than_150_years():
    data = []
    for individual in individuals:
        age = individual[IDX_IND_AGE]
        if(age > 150):
            data.append("ERROR: US07 INDIVIDUAL "+ str(individual[IDX_IND_ID])+ " named "+ str(individual[IDX_IND_NAME])+ " has age more than 150 years.")        
    return data

data = us_07_less_than_150_years()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User story US21
# Story Name: Correct gender for role
# Owner: Parth Paghdal (pp)
# Email: ppaghdal@stevens.edu
def us_21_correct_gender_for_role():
    data = []
    for family in families:
        husbandId = family[IDX_FAM_HUSBAND_ID]
        wifeId = family[IDX_FAM_WIFE_ID]
        husbandGender = "M"
        wifeGender = "F"
        for individual in individuals:
            if(individual[IDX_IND_ID] == husbandId):
                husbandGender = individual[IDX_IND_GENDER]
            if(individual[IDX_IND_ID] == wifeId):
                wifeGender = individual[IDX_IND_GENDER]
        if(husbandGender != "M"):
            data.append("ERROR: US21 FAMILY "+ str(family[IDX_FAM_ID])+" is having incorrect gender role for husband with id "+ str(husbandId)+ " named "+str(family[IDX_FAM_HUSBAND_NAME]) )
        if(wifeGender != "F"):
            data.append("ERROR: US21 FAMILY "+ str(family[IDX_FAM_ID])+" is having incorrect gender role for wife with id "+ str(wifeId)+ " named "+str(family[IDX_FAM_WIFE_NAME]) )
    return data

data = us_21_correct_gender_for_role()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

# User Story US24
# Story Name: Unique families by spouses
# Owner: Sai Krishna (km), Parth Paghdal (pp)
# Email : smiriyal@stevens.edu, ppaghdal@stevens.edu
# This user story done using pair programming with Parth Paghdal (pp)
def us_24_unique_families_by_spouces():
    data = []
    marriageData = []
    for family in families:
        marriageDate = family[IDX_FAM_MARRIED]
        husbandName = family[IDX_FAM_HUSBAND_NAME]
        wifeName = family[IDX_FAM_WIFE_NAME]
        marriageData.append((marriageDate, husbandName, wifeName))

    counter = dict(Counter(marriageData))
    for key, value in counter.items():
        if(value > 1):
            data.append("ERROR: US24 FAMILY is having family where husband named  "+ key[1] + " and wife named" + key[2] + " married on "+ str(key[0]+" is breaking the user storey rule") )
        
    return data

data = us_24_unique_families_by_spouces()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)

#User Story US27
#Story Name: Include individual ages
#Owner: Sai Krishna (km)
#Email : smiriyal@stevens.edu
def us_27_include_individual_ages():
    data = []
    for individual in individuals:
        id = individual[IDX_IND_ID]
        name = individual[IDX_IND_NAME]
        age = individual[IDX_IND_AGE]
        data.append("ERROR: US27 INDIVIDUAL "+str(id)+" named "+str(name)+" is "+str(age)+" years old.")
    return data

data = us_27_include_individual_ages()
print(*data, sep="\n")
print(*data, sep="\n", file=sprint4CodeOutput)
