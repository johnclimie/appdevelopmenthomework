def main():
    pass

# Create function that returns gallons of paint required
def gallons(sqft):
    return sqft * 0.0089

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