score = input("What did you score? ")
conv = int(score)

if conv == 100:
    print("Perfect score!")
elif conv >= 70:
    print("Excellent!")
elif conv >= 50:
    print("You passed!")
else:
    print("You failed. Try again!")