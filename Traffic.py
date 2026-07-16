light_color = input("What color is the traffic light? (red/yellow/green): ")

if light_color == "red":
    print("Stop!")
elif light_color == "yellow":
    print("Slow down!")
elif light_color == "green":
    print("Go!")
else:
    print("Invalid color! That is not a traffic light color.")
