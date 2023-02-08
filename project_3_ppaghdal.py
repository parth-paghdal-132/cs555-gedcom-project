import datetime
from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable

allowedTags = {
    'HEAD':'0', 'NOTE':'0', 'NAME':'1', 'INDI': '0', 'SEX': '1', 'BIRT':'1', 'DATE':'2', 'FAM': '0', 
    'FAMS': '1', 'FAMC': '1', 'DEAT': '1', 'HUSB':'1', 'WIFE':'1','CHIL':'1', 'MARR': '1', 'DIV':'1', 
    'TRLR': '0'
}

fileName = "input_file.ged"

with open(fileName, 'r') as file:
    lines = file.read().splitlines()
lines = [[line] for line in lines]

for i in range(len(lines)):
    if((len(lines[i][0].strip().split())) < 2):
        lines[i] = "error at line number " + i
    else:
        lines[i] = lines[i][0].strip().split(" ",2)
        if(len(lines[i]) > 2 and lines[i][1] in ["INDI", "FAM"]):
            lines[i] = "Error at line number " + i
        elif(len(lines[i]) > 2 and lines[i][2] in ["INDI", "FAM"]):
            lines[i][1], lines[i][2] = lines[i][2], lines[i][1]

infoList = []
for i in range(len(lines)):
    if(len(lines[i]) > 2):
        if(lines[i][1] in allowedTags.keys() and allowedTags[lines[i][1]] == lines[i][0]):
            infoList.append((lines[i][0], lines[i][1], lines[i][2]))
        elif(lines[i][0:2] == "In"):
            infoList.append(lines[i])
        else:
            continue
    elif(len(lines[i]) == 2):
        if((lines[i][1] in allowedTags.keys()) and allowedTags[lines[i][1]] == lines[i][0]):
            infoList.append((lines[i][0], lines[i][1]))
        else:
            continue

infoList.pop(0)
infoList.pop(-1)
infoList = list(filter((('1', 'BIRT')).__ne__, infoList))

shouldBreak = False
individualsData = {}
familiesData = {}
for i in range(len(infoList)):
    vals = []
    j = i + 1
    if(infoList[i][1] == 'INDI' and infoList[i][0] == '0'):
        while(infoList[j][1] != 'INDI'):
            key = infoList[i][2][1:-1]
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

individualsTable = PrettyTable(["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"])
name = ""
gender = ""
birthday = ""
death = ""
isAlive = False

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
    if(any("DEAT" in i for i in value)):
        age = relativedelta(death, birthday).years
        isAlive = True
    else:
        age = relativedelta(datetime.datetime.now(), birthday).years

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
    
    tempArr = [key, name, gender, birthday, age, isAlive, death, famc, fams]
    individualsTable.add_row(tempArr)

print("Individuals")
print(individualsTable)

# shouldBreak = False
for i in range(len(infoList)):
    vals = []
    j = i + 1
    if(infoList[i][1] == 'FAM' and infoList[i][0] == '0'):
        while(j < len(infoList)):
            key = infoList[i][2][1:-1]
            if(infoList[j][1] != "MARR" and infoList[j][1] != "DIV" and infoList[j][1] != "DATE" and infoList[j][1] != "FAM"):
                vals.append((infoList[j][1], infoList[j][2][1:-1]))
            elif(infoList[j][1] == "MARR" and len(infoList[j+1]) > 2):
                vals.append(("MARR", infoList[j+1][2]))
            elif(infoList[j][1] == "DIV" and len(infoList[j+1]) > 2):
                vals.append(("DIV", infoList[j+1][2]))
            elif(infoList[j][1] == "FAM" and infoList[j][0] == "0"):
                # shouldBreak = True
                break
            j += 1
        familiesData.update({key: vals})
        
husbandId = 0
wifeId = 0
husbandName = ""
wifeName = ""
famliesTable = PrettyTable(["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"])
for key, value in familiesData.items():
    innerChild = []
    married = ""
    divorce = ""
    for i in range(len(value)):
        if(value[i][0] == "HUSB"):
            husbandId = value[i][1]
            husbandName = individualsData[husbandId][0][1]
        if(value[i][0] == "WIFE"):
            wifeId = value[i][1]
            wifeName = individualsData[wifeId][0][1]
        if(value[i][0] == "CHIL"):
            child = value[i][1]
            innerChild.append(child)
        if(value[i][0] == "MARR"):
            married = datetime.datetime.strptime(value[i][1],"%d %b %Y").date()
        if(value[i][0] == "DIV"):
            divorce = datetime.datetime.strptime(value[i][1], "%d %b %Y").date()
    tempArr = [key, married, divorce, husbandId, husbandName, wifeId, wifeName]
    for i in range(len(tempArr)):
        if(len(str(tempArr[i])) == 0):
            tempArr[i] = "NA"
    if(len(innerChild) == 0):
        innerChild = "NA"
    else:
        innerChild = str(innerChild)
        innerChild = innerChild.replace("[", "{").replace("]", "}")
    tempArr.append(innerChild)
    famliesTable.add_row(tempArr)

print("Families")
print(famliesTable)