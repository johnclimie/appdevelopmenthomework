import math

dataList = []
bmiList = []
ageList = []
weightList = []
physList = []

N = 507

def readTxt():
    txtFile = open('data.txt', 'r')
    for count in range(N):
        dataList.append(txtFile.readline())
    
    txtFile.close()

def calcBMI(weight, height):
    calc = (((float(weight) * 2.20462)/(float(height) * 0.393701)**2) * 703)
    return calc

def calcPhys(chestDiam, chestDep, bitroDiam, wristGir, ankGir, height):
    calc = (-110 + (1.34 * float(chestDiam)) + (1.54 * float(chestDep)) + (1.20 * float(bitroDiam)) + (1.11 * float(wristGir)) + (1.15 * float(ankGir)) + (0.177 * float(height)))
    return calc

def calcSum(list):
    calc = sum(list)
    return calc

def calcSumSq(list):
    tempList = []

    for count in range(N):
        tempList.append(list[count] ** 2)

    sumList = sum(tempList)
    return sumList

def calcXY(list1, list2):
    tempList = []
    
    for count in range(N):
        tempList.append(list1[count] * list2[count])
    
    sumList = sum(tempList)
    return sumList

def storeBMIAgeWeightPhys():
    for count in range(N):
        tempString = dataList[count].split()
        bmiList.append(calcBMI(tempString[22], tempString[23]))
        weightList.append(float(tempString[22]))
        ageList.append(float(tempString[21]))
        physList.append(calcPhys(tempString[4], tempString[3], tempString[2], tempString[20], tempString[19], tempString[23])) 

def calcSlope(count, sumXY, sumX, sumY, sumXSq):
    calc = ((count * sumXY - (sumX * sumY))/(count * sumXSq - (sumX)**2))
    return calc

def calcIntercept(sumY, slope, sumX, count):
    calc = ((sumY - (slope*sumX))/count)
    return calc

def calcCorr(count, sumXY, sumX, sumY, sumXSq, sumYSq):
    calc = ((count*sumXY - (sumX*sumY)) / math.sqrt((count*sumXSq-(sumX)**2) * (count*sumYSq - (sumY)**2)))
    return calc


def main():
    readTxt()
    storeBMIAgeWeightPhys()
    print(calcCorr(N, calcXY(ageList, bmiList), calcSum(ageList), calcSum(bmiList), calcSumSq(ageList), calcSumSq(bmiList)))
    
if __name__ == "__main__":
    main()


#     print(calcSlope(N, calcXY(ageList, bmiList), calcSum(ageList), calcSum(bmiList), calcSumSq(ageList)))
#     print(calcIntercept(calcSum(bmiList), calcSlope(N, calcXY(ageList, bmiList), calcSum(ageList), calcSum(bmiList), calcSumSq(ageList)), calcSum(ageList), N))