mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

tip = (mealCost * tipPercent)/100
tax = (mealCost * taxPercent)/100

totalCost = mealCost + tax + tip

print("The total meal cost is {} dollars.".format(round(totalCost)))
