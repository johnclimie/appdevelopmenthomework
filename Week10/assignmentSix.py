# John Climie
# October 10th, 2023
# User inputs 20 numbers into a list, which will then print the lowest number, highest number, total of the numbers, and average of the numbers.

# Declares variables for the list and total
numberList = []
total = 0

# Loops 20 times for each number that is input, adding each number to the list and adding to the total.
for each in range(20):
    try:
        inputNumber = float(input("Please input a number: "))
        total += inputNumber
        numberList.append(inputNumber)
    except ValueError:
        print("Please enter a valid number")

# Sets minNumber variable
minNumber = min(numberList)

# Sets maxNumber variable
maxNumber = max(numberList)

# Sets average variable
average = total/len(numberList)

# Prints Lowest Number
print(f"Lowest Number: {minNumber}")
# Prints highest number
print(f"Highest Number: {maxNumber}")
# Prints total
print(f"Total: {total}")
# Prints average
print(f"Average: {average}")