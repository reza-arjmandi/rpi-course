mealCost=float(input())
tipPercent=int(input())
taxPercent=int(input())

tip = mealCost * (tipPercent / 100.0)
tax = mealCost * (taxPercent / 100.0)
totalCost = mealCost + tip + tax
#'totalCost=totalCost+(mealCost * tipPercent / 100.0)+(mealCost * taxPercent / 100.0)
print("The total meal cost is {} dollars.".format(round(totalCost)))
