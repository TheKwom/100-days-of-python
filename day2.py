print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

billWithTip = tip / 100 * bill + bill
splitAmount = billWithTip / people

print("Each person should pay: $" + str(round(splitAmount, 2)))