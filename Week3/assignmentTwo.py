# John Climie
# August 29th, 2023
# Program calculates the final discounted price of software packages that could be in bulk and displays the price along with how much the discount is


price = 99.0 # Price of each package
input = float(input('Enter how many packages you would like: ')) # User is prompted and inputs desired package amount

if input < 10: # Returns no discount and total when under 10 purchased
    print("You have no discount, making your total", price*input)
elif input >= 10 and input <= 19: # Returns 10% discount and total when under 20 purchased
    finalPrice = price*.90*input
    print(f"You have a 10 percent discount, making your total ${finalPrice:,.2f}")
elif input >= 20 and input <= 49: # Returns 20% discount and total when under 50 purchased
    finalPrice = price*.80*input
    print(f"You have a 20 percent discount, making your total ${finalPrice:,.2f}")
elif input >= 50 and input <= 99: # Returns 30% discount and total when under 100 purchased
    finalPrice = price*.70*input
    print(f"You have a 30 percent discount, making your total ${finalPrice:,.2f}")
else: # Returns 40% discount and total when over 100 purchased
    finalPrice = price*.60*input
    print(f"You have a 40 percent discount, making your total ${finalPrice:,.2f}")