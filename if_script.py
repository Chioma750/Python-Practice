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


# temperature = 15
# raining = True 

# temperature = int(input("What is your temperature degree: "))
# raining = input("Raining level, (True or False): ")

# if temperature > 15 and raining == "False": 
#     print("safe")
# else:
#     print("not safe")
