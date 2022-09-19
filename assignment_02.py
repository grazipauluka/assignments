# Tip calculator Create a Tip calculator (or rather a function for a tip calculator)!
# For any number of guests sharing a restaurant bill, calculate how much tip each guest needs to pay.
# Use variables to store the number of guests, the amount of the bill and the tip in percentage,
# e.g. guest = 2; bill = 80; tipPercentage = 10;
# Create a function which takes these values as input and outputs the total amount each guest needs to pay as well as the amount of tip that is included,
# eg `Each guest needs to pay: 44 euro` and `The amount of tip for each guest is: 4 euro`.



def tip_calculator():
    guest_input = input("Enter number of guest ")
    bill_input = input("Enter total bill ")
    tip_percentage_input = input("Enter tip percentage ")
    guest = int(guest_input)
    bill = int(bill_input)
    tip_percentage = int(tip_percentage_input)/100
    bill_without_tip = bill/guest
    total_tip_for_guest = bill/guest * tip_percentage
    total_bill_plus_tip = bill_without_tip + total_tip_for_guest
    print(f' Each guest needs to pay: {bill_without_tip} euros and the amount of tip for each guest is: {total_tip_for_guest} euros, so {total_bill_plus_tip} euros')

tip_calculator()