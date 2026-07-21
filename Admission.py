Jamb_Score = input("What is your Jamb score: ")
conv = int(Jamb_Score)

Waec_Credit = input("How many credit did you have: ")
Conv = int(Waec_Credit)

print( )
if conv >= 200 and Conv >= 5:
    print("Congratulations, you are qualified for admission!")
else:
    print("Sorry, you do not meet the requirements.")