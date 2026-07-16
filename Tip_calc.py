Amount = input("What is the total food bill amount: ")
bill = float(Amount)
tip = bill * 0.15
bill += tip
print("Tip Amount: ", tip)
print("Final total bill:", bill)