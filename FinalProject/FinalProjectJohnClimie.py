# John Climie
# November 29th, 2023
# Final project | Calculates the slope, intercept, and correlation between both age and BMI, and then weight and physical attributes.

# Imports Math package for sqrt
import math

# Declares emtpy lists for data, bmi, age, weight and physical attributes
dataList = []
bmiList = []
ageList = []
weightList = []
physList = []

# Constant for count of data participants
N = 507

# Function imports data into list
def readTxt():
    txtFile = open('data.txt', 'r')
    for count in range(N):
        dataList.append(txtFile.readline())
    
    txtFile.close()

# Function calculates BMI
def calcBMI(weight, height):
    calc = (((float(weight) * 2.20462)/(float(height) * 0.393701)**2) * 703)
    return calc

# Function calculates physical attributes
def calcPhys(chestDiam, chestDep, bitroDiam, wristGir, ankGir, height):
    calc = (-110 + (1.34 * float(chestDiam)) + (1.54 * float(chestDep)) + (1.20 * float(bitroDiam)) + (1.11 * float(wristGir)) + (1.15 * float(ankGir)) + (0.177 * float(height)))
    return calc

# Function calculates sum of a list
def calcSum(list):
    calc = sum(list)
    return calc

# Function calculates each index in a list squared, then returns sum of that list
def calcSumSq(list):
    tempList = []

    for count in range(N):
        tempList.append(list[count] ** 2)

    sumList = sum(tempList)
    return sumList

# Function calculates each x value by the y value, then returns sum of the results.
def calcXY(list1, list2):
    tempList = []
    
    for count in range(N):
        tempList.append(list1[count] * list2[count])
    
    sumList = sum(tempList)
    return sumList

# Function appends values into lists
def storeBMIAgeWeightPhys():
    for count in range(N):
        tempString = dataList[count].split()
        bmiList.append(calcBMI(tempString[22], tempString[23]))
        weightList.append(float(tempString[22]))
        ageList.append(float(tempString[21]))
        physList.append(calcPhys(tempString[4], tempString[3], tempString[2], tempString[20], tempString[19], tempString[23])) 

# Function calculates slope of x and y value
def calcSlope(count, sumXY, sumX, sumY, sumXSq):
    calc = ((count * sumXY - (sumX * sumY))/(count * sumXSq - (sumX)**2))
    return calc

# Function calculates intercept of x and y value
def calcIntercept(sumY, slope, sumX, count):
    calc = ((sumY - (slope*sumX))/count)
    return calc

# Function calculates correlation of x and y value
def calcCorr(count, sumXY, sumX, sumY, sumXSq, sumYSq):
    calc = ((count*sumXY - (sumX*sumY)) / math.sqrt((count*sumXSq-(sumX)**2) * (count*sumYSq - (sumY)**2)))
    return calc


def main():
    # Functions are called to import data and load data into arrays
    readTxt()
    storeBMIAgeWeightPhys()
    
    # Variables are set for (x)age and (y)BMI's slope, intercept and correlation
    slopeAgeBMI = calcSlope(N, calcXY(ageList, bmiList), calcSum(ageList), calcSum(bmiList), calcSumSq(ageList))
    interceptAgeBMI = calcIntercept(calcSum(bmiList), slopeAgeBMI, calcSum(ageList), N)
    corrAgeBMI = calcCorr(N, calcXY(ageList, bmiList), calcSum(ageList), calcSum(bmiList), calcSumSq(ageList), calcSumSq(bmiList))

    # Variables are set for (x)weight and (y)physical attribute's slope, intercept and correlation
    slopeWeightPhys = calcSlope(N, calcXY(weightList, physList), calcSum(weightList), calcSum(physList), calcSumSq(weightList))
    interceptWeightPhys = calcIntercept(calcSum(physList), slopeWeightPhys, calcSum(weightList), N)
    corrWeightPhys = calcCorr(N, calcXY(weightList, physList), calcSum(weightList), calcSum(physList), calcSumSq(weightList), calcSumSq(physList))

    # Final return is set for results for Age and BMI, and then weight and physical attributes
    finalReturn = f"Results for Age and BMI: \nSlope: {slopeAgeBMI} \nIntercept: {interceptAgeBMI} \nSlope: {corrAgeBMI} \n\n\nResults for Weight and Physical Attributes: \nSlope: {slopeWeightPhys} \nIntercept: {interceptWeightPhys} \nSlope: {corrWeightPhys}"

    # Prints final statement
    print(finalReturn)
    
if __name__ == "__main__":
    main()