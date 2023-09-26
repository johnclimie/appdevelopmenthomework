# John Climie
# September 26th, 2023
# Asks user to input how many random numbers they would like to randomly generate, then prints all the numbers, the total, and the average of the numbers

#Imports Random Library
import random

# Asks user for the numbers to input and calls each function
def main(): 
    numbers = int(input("Enter how many numbers you'd like to generate:"))
    writeNumbers(numbers)
    calcAvg()

# Creates text file and writes each random number
def writeNumbers(nums):
    numsFile = open('nums.txt', 'w')

    for count in range(1, nums + 1):
        number = random.randint(1,500)

        numsFile.write(f"{number}\n")
          
    numsFile.close()

# Logs each number, the total, and calculated average
def calcAvg():
    numTotal = 0
    numCount = 0

    numsFile = open("nums.txt", "r")

    print("Your numbers:")

    for line in numsFile:
        numTotal+=float(line)
        numCount+=1
        print(line)

    numsFile.close()

    avg = numTotal/numCount

    print(f"Your total will be {numTotal}, making your average {avg}")

# Calls main function 
if __name__ == "__main__":   
    main()