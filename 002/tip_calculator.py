print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to pay? 10, 12, o 15? "))
people = int(input("How many people to split the bill? "))
tip_percentage = tip/100
total_tip_amount = bill * tip_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people

# final_amount  = (bill_per_person, 2)
# alternative way
final_amount = "{:.2f}".format(bill_per_person) # turned float type to a string, specifies a format in this case it is 2 decimal places format
print(f"Each person should pay: ${final_amount}")



