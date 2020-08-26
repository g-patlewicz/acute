SDFfile = input('Which file to break up?')
InputFile = open(SDFfile,'r', encoding='utf-8')
NameOfOutputFiles = input('Output files should begin with?')
NumberOfMoleculesInEachFile = input('Number of molecules that should be in each file?')
NumberOfMoleculesInEachFile = int(NumberOfMoleculesInEachFile)
moleculeCounter = 0
fileNumber = 1

fileOutName = NameOfOutputFiles + '.' + str(fileNumber) + '.' + 'sdf'
fileOut = open(fileOutName, 'a', encoding='utf-8')

for line in InputFile:
    fileOut.write(line)
    if '$$$$' in line:
        moleculeCounter += 1
        if moleculeCounter % NumberOfMoleculesInEachFile == 0:
            fileNumber += 1
            fileOut.close()
            fileOutName = NameOfOutputFiles + '.' + str(fileNumber) + '.' + 'sdf'
            fileOut = open(fileOutName,'a',encoding='utf-8')
fileOut.close()
InputFile.close()