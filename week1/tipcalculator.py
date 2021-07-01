#!/bin/python3

bill_amount = input("What is the bill amount? ")
tip_amount = int(input("Percentage of tip? "))

bill = int(bill_amount.replace("$", ""))

tip = float(bill * tip_amount / 100)
total = float(bill + tip)

print(f"Your tip will be ${tip:.2f} and your total will be ${total:.2f}")
