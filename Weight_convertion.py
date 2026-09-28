def solution(kilograms):
    kg = float(kilograms)
    grams = kg * 1000 
    pounds = kg * 2.20462

    rounded_pounds = round(pounds, 2)
    pounds_str = f"{rounded_pounds:.2f}"
    if pounds_str.endswith("0"):
        pounds_str = f"{rounded_pounds:.1f}"
        
    return f"""Kilograms: {kg}
Grams: {grams}
Pounds: {pounds_str}"""
