# John Climie
# November 7th, 2023
# Asks user to input 10 character phone number in phone number format, then application converts letters then numbers and returns output.

# PhoneNumberConverter class is intiated with a phone number initiated. 
class PhoneNumberConverter:
    def __init__(self, phoneNumber):
        self.phoneNumber = phoneNumber

    # Method is created in order to convert letters to numbers if needed
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
        
    # Method is created in order to convert each character in the phoneNumber
    def convertNum(self):
        newNum = ""
        for char in self.phoneNumber:
            newNum += self.numericConverter(char)
        return newNum
    
    # Method returns the phone number in the correct format
    def returnFinalNum(self, newNum):
        finalNum = f"{newNum[:3]}-{newNum[3:6]}-{newNum[6:]}"
        print("Final converted phone number:", finalNum)

# Main code
if __name__ == "__main__":
    # User input is stored
    userInput = input("Enter 10 character phone number in the form of XXX-XXX-XXXX: ")

    # Validates that user input is 12 characters long, with dashes at char 3 & char 7. Then methods are called upon, converts the final product, then returns the final product.
    if len(userInput) == 12 and userInput[3] == '-' and userInput[7] == '-':
        numConverter = PhoneNumberConverter(userInput.replace("-", ""))
        convertedNum = numConverter.convertNum()
        numConverter.returnFinalNum(convertedNum)
    else:
        print("Input is invalid, please try again")