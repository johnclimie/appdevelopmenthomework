# John Climie
# August 16th, 2023
# Program calculates the final price of a meal, including tax and tip

mealPrice = float(input('Enter meal price: ')) #User is prompted and inputs the price of the meal
TAX = 0.07 # Const for tax, which is 7 percent
TIP = 0.18 # const for tip, which is 18 percent

mealTax = mealPrice * TAX # Meal tax is calcuated by multiplying the meal price with the tax const
mealTip = mealPrice * TIP # Meal tip is calculated by multiplying the meal price with the tip const
mealTotal = mealPrice + mealTax + mealTip # Meal total is calculated by adding the meal price, tip and tax

# Application is finalized by displaying the subtotal, tax, tip and total cost
print(f"Meal Subtotal: ${mealPrice:,.2f}\nMeal Tax: ${mealTax:,.2f}\nMeal Tip: ${mealTip:,.2f}\nMeal Total: ${mealTotal:,.2f}")