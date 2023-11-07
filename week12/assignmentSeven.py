# John Climie
# November 7th, 2023
# Asks user to input 10 character phone number in phone number format, then application converts letters then numbers and returns output.

class PhoneNumberConverter:
    def __init__(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def numericConverter(self, char):
        char = char.upper()
        if char in "ABC":
            return "2"
        elif char in "DEF":
            return "3"
        elif char in "GHI":
            return "4"
        elif char in "JKL":
            return "5"
        elif char in "MNO":
            return "6"
        elif char in "PQRS":
            return "7"
        elif char in "TUV":
            return "8"
        elif char in "WXYZ":
            return "9"
        else:
            return char
        
    def convertNum(self):
        newNum = ""
        for char in self.phoneNumber:
            newNum += self.numericConverter(char)
        return newNum
    
    def returnFinalNum(self, newNum):
        finalNum = f"{newNum[:3]}-{newNum[3:6]}-{newNum[6:]}"
        print("Final converted phone number:", finalNum)

if __name__ == "__main__":
    userInput = input("Enter 10 character phone number in the form of XXX-XXX-XXXX: ")

    if len(userInput) == 12 and userInput[3] == '-' and userInput[7] == '-':
        