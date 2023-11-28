dataList = []
bmiList = []
ageList = []
weightList = []
physList = []

def readTxt():
    txtFile = open('data.txt', 'r')
    for count in range(507):
        dataList.append(txtFile.readline())
    
    txtFile.close()

def calcBMI(weight, height):
    calc = (((float(weight) * 2.20462)/(float(height) * 0.393701)**2) * 703)
    return calc

def calcPhys(chestDiam, chestDep, bitroDiam, wristGir, ankGir, height):
    calc = (-110 + (1.34 * float(chestDiam)) + (1.54 * float(chestDep)) + (1.20 * float(bitroDiam)) + (1.11 * float(wristGir)) + (1.15 * float(ankGir)) + (0.177 * float(height)))
    return calc

def storeBMIAgeWeightPhys():
    for count in range(507):
        tempString = dataList[count].split()
        bmiList.append(calcBMI(tempString[22], tempString[23]))
        weightList.append(tempString[22])
        ageList.append(tempString[21])


        
        
    

def main():
    readTxt()

if __name__ == "__main__":
    main()