meal_Cost = float(input())
tip_Percent = int(input())
tax_Percent = int(input())


tip = meal_Cost * tip_Percent / 100
tax = meal_Cost * tax_Percent / 100
total_Cost = meal_Cost + tip + tax


print("The total meal cost is " + str(round(total_Cost)) + " dollars.")