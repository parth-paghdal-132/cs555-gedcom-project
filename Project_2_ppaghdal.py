# @Author Parth Paghdal
# CWID 20009364
# E-mail ppaghdal@stevens.edu

# set your input GEDCOM file here
GED_FILE = "input_file.ged"

# main function entry point of the script.
def main():
    printLogs(GED_FILE)

# This function is used to print .ged file each line 
# and line with level, tag, tag is valid or not and
# other arguments of the line
def printLogs(fileName):
    # Variable to store all lines from the file
    lines = []
    # this array variable holds allowed valid tag for the file
    # tag with other value than this will consider as invalid tag and log will show N
    allowedTags = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT',
              'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE',
              'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']

    with open(fileName, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.replace('\n','')
        print('--> {0}'.format(line))

        # Finding tag index
        tag_index = 2 if 'INDI' in line or ('FAMC' not in line and 'FAMS' not in line and 'FAM' in line) else 1

        # Seprating line into chunks
        contentArr = line.split(' ')

        # Current line tag name
        tag = contentArr[tag_index]

        # this variable holds charcater for whether the tag is valid or not
        valid = 'Y' if tag in allowedTags else 'N'

        # Level of line
        level = contentArr[0]
        # removing items from the array so it leaves arguments of the line
        contentArr.pop(tag_index)
        contentArr.pop(0)

        print('<-- {0}|{1}|{2}|{3}'.format(level, tag, valid, ' '.join(contentArr)))

if __name__ == '__main__':
    main()