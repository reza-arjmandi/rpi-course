
mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

tip0 = mealCost * (tipPercent / 100.0)
tax0 = mealCost * (taxPercent / 100.0)
totalCost = mealCost + tip0 + tax0
#'totalCost=totalCost+(mealCost * tipPercent / 100.0)+(mealCost * taxPercent / 100.0)
print("The total meal cost is {} dollars.".format(round(totalCost)))
