# John Climie
# September 12th, 2023
# Program returns the cost of tuition for 5 years with a 3% increase each year.

# Sets value for tuition cost int
tuitionCost = 8000

# Sets value for APR and Years consts
APR = 1.03
YEARS = 5

# Loops over the years, multiplies the tuition with the APR and returns each of the tuition costs.
for year in range (1, YEARS + 1):
    tuitionCost *= APR
    print(f"For year {year}, your semester tuition will cost ${tuitionCost:.2f}")