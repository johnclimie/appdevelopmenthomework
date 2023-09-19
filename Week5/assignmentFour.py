# Main function is called upon at the end of the file
def main():
    # Takes input from user of the amount of square feet, along with the cost of paint per square feet
    sqft =  float(input("Enter the amount of square feet of paint you need: "))
    cost = float(input("Enter the cost of paint per gallon: "))

    # Sets variables for each function
    gallonAmount = gallons(sqft)
    hoursAmount = hours(sqft)
    paintCostAmount = paintCost(gallonAmount, cost)
    laborCostAmount = laborCost(hoursAmount)
    totalCostAmount = totalCost(paintCostAmount, laborCostAmount)

    # Prints the amount of gallons, hours, paint cost, labor cost, and total cost seperated into seperate lines
    print(f"You will require {gallonAmount:,.2f} gallons\nThis will require {hoursAmount:,.2f} hours\nThis leave the cost of paint to ${paintCostAmount:,.2f}.\nThis leave the cost of labor to ${laborCostAmount:,.2f}.\nThis leave the total cost of the total paint job to ${totalCostAmount:,.2f}.")


# Returns gallons of paint required
def gallons(sqft):
    return sqft * 0.0089285714285714

# Returns hours of labor
def hours(sqft):
    return sqft / 14

# Returns cost of paint
def paintCost(gallons, cost):
    return gallons * cost

# Returns labor charge
def laborCost(hours):
    return hours * 35

# Returns the total paint job cost
def totalCost(paintCost, hoursCost):
    return paintCost + hoursCost

main()