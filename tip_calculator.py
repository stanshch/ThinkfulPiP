meal = float(raw_input("What is the pre-tax cost of your meal?\n"))
tax = float(raw_input("What is the tax rate?\n"))/100
tip = float(raw_input("What percent tip would you like to leave?\n"))/100
tax_value = meal*tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax*tip
total = meal_with_tax+tip_value

print "The base cost of the meal is $%1.2f" %meal
print "Your tax is $%1.2f" %tax_value
print "The tip you will pay is $%1.2f" %tip_value
print "Your grand total is $%1.2f" %total

