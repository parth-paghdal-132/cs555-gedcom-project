import pandas
import datetime
from dateutil.relativedelta import relativedelta
import prettytable as ptTable
#17
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
        if (len(lines[i])> 2 and (lines[i][2] in ['FAM','INDI'])):
            lines[i][1], lines[i][2] = lines[i][2], lines[i][1]
        elif(len(lines[i])> 2 and (lines[i][1] in ['FAM','INDI'])):
            lines[i] = "error at line number " + i

infoList = []
for i in range(len(lines)):
    if(len(lines) == 2):
        if((lines[i][1] in allowedTags.keys()) and allowedTags[lines[i][1]] == lines[i][0]):
            infoList.append((lines[i][0], lines[i][1]))
    elif(len(lines[i]) > 2):
        if(lines[i][1] in allowedTags.keys() and allowedTags[lines[i][1]] == lines[i][0]):
            infoList.append((lines[i][0], lines[i][1], lines[i][2]))
        elif(lines[i][0:2] == "In"):
            infoList.append(lines[i])
infoList.pop(-1)
infoList.pop(0)
infoList = list(filter((('1', 'BIRT')).__ne__, infoList))

infoList