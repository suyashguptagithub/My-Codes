print("Welcome to our tip calculator!")
amount = float(input("what is the bill value? \n"))

# tip = float(input("How much tip you want to give? 10, 20 or 15 \n"))
tip = float(input("How much % tip you want to give? 10%, 20% or 15% \n"))

no_of_people = float(input("no of people sharing the bill ? \n"))
formula = (((amount * tip/100) + amount) / no_of_people)

# formula = ((amount + tip) / no_of_people)
final_amt = round(formula, 2)

print(f"Each person have to pay {final_amt}")





