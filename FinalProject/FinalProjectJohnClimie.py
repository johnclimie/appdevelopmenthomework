dataList = []
bmiList = []
weightList = []
ageList = []

def readTxt():
    txtFile = open('data.txt', 'r')
    for count in range(507):
        dataList.append(txtFile.readline())
    
    txtFile.close()

def calcBMI(weight, height):
    calc = (((float(weight) * 2.20462)/(float(height) * 0.393701)**2) * 703)
    return calc

def storeBMIAgeWeight():
    for count in range(507):
        tempString = dataList[count].split()
        bmiList.append(calcBMI(tempString[22], tempString[23]))
        weightList.append(tempString[22])
        ageList.append(tempString[21])

        
        
    

def main():
    readTxt()
    storeBMIAgeWeight()

if __name__ == "__main__":
    main()