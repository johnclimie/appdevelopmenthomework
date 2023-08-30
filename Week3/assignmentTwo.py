price = 99.0
input = float(input('Enter how many packages you would like: '))

if input < 10:
    print("You have no discount, making your total", price*input)
elif input >= 10 and input <= 19:
    finalPrice = price*.90*input
    print(f"You have a 10 percent discount, making your total ${finalPrice:,.2f}")
elif input >= 20 and input <= 49:
    finalPrice = price*.80*input
    print(f"You have a 20 percent discount, making your total ${finalPrice:,.2f}")
elif input >= 50 and input <= 99:
    finalPrice = price*.70*input
    print(f"You have a 30 percent discount, making your total ${finalPrice:,.2f}")
else:
    finalPrice = price*.60*input
    print(f"You have a 40 percent discount, making your total ${finalPrice:,.2f}")