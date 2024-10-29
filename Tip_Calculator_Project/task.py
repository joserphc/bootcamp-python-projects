print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

discount = tip / 100 + 1

result = bill * discount / people

formatted_bill = "{:.2f}".format(result)

print(f"Each person should pay: ${formatted_bill}")