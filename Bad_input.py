def solution(value):
    try:
        number = float(value)
        doubled = number * 2

        # Checking if the doubled number is a clean whole number (like 10.0)
        if doubled.is_integer():
            return int(doubled)  # returns 10 instead of 10.0
        else:
            return round(doubled, 2) # returns decimals rounded to 2 places (like 5.33)

    except ValueError:
        # If the input was a word like "hello", return this error.
        return "Invalid number"