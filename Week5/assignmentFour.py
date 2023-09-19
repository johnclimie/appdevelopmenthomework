def main():
    sqft =  float(input("Enter the amount of square feet of paint you need: "))
    cost = float(input("Enter the cost of paint per square feet: "))

    gallonAmount = gallons(sqft)
    hoursAmount = hours(sqft)
    paintCostAmount = paintCost(gallonAmount, cost)
    laborCostAmount = laborCost(hoursAmount)
    totalCostAmount = totalCost(paintCostAmount, laborCostAmount)

    print(gallonAmount)
    print(hoursAmount)
    print(paintCostAmount)
    print(laborCostAmount)
    print(totalCostAmount)


# Create function that returns gallons of paint required
def gallons(sqft):
    return sqft * 0.0089285714285714

# Create a funcion that returns hours of labor
def hours(sqft):
    return sqft / 14

# Create a function that returns cost of paint
def paintCost(gallons, cost):
    return gallons * cost

# Create a function that returns labor charge
def laborCost(hours):
    return hours * 35

# Create a funciton that returns the total cost
def totalCost(paintCost, hoursCost):
    return paintCost + hoursCost

main()