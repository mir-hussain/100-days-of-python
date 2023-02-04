print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? "))
people_count = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? "))

after_split = total_bill / people_count

total_payable = after_split + after_split * (tip_percentage / 100)

print(f"Each person should pay {round(total_payable, 2)}")
