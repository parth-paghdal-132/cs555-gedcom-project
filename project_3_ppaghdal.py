import datetime
from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable

# This object holds valid tag with their level
# Tag with other key value pair then this will considered as Invalid
allowedTags = {
    'HEAD':'0', 'NOTE':'0', 'NAME':'1', 'INDI': '0', 'SEX': '1', 'BIRT':'1', 'DATE':'2', 'FAM': '0', 
    'FAMS': '1', 'FAMC': '1', 'DEAT': '1', 'HUSB':'1', 'WIFE':'1','CHIL':'1', 'MARR': '1', 'DIV':'1', 
    'TRLR': '0'
}

# Replace your file name here check data for individuals and families
fileName = "input_file.ged"

# This function reads file and store all lines in one variable
with open(fileName, 'r') as file:
    lines = file.read().splitlines()
lines = [[line] for line in lines]

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
name = ""
gender = ""
birthday = ""
death = ""
isAlive = False

# Iteraing over individuals data and getting only values needed for output
for key, value in individualsData.items():
    age = 0
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
        isAlive = True
    else:
        age = relativedelta(datetime.datetime.now(), birthday).years

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
    
    individuals.append([key, name, gender, birthday, age, isAlive, death, famc, fams])

individualsTable.add_rows(individuals)

# Showing individuals details
print("Individuals")
print(individualsTable)

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
        
husbandId = 0
wifeId = 0
husbandName = ""
wifeName = ""
# Columns names for family table
famliesTable = PrettyTable(["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"])
# This array holds array of family details
families = []
for key, value in familiesData.items():
    innerChild = []
    married = ""
    divorce = ""
    for i in range(len(value)):
        # This finds husband name
        if(value[i][0] == "HUSB"):
            husbandId = value[i][1]
            husbandName = individualsData[husbandId][0][1]
        # This finds wife name
        if(value[i][0] == "WIFE"):
            wifeId = value[i][1]
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
print("Families")
print(famliesTable)