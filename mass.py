def mass(value, from_v, to_v):
    if from_v == to_v:
        return value
    elif from_v == "Kilogram" and to_v == "Gram":
        return value * 1000

    elif from_v == "Kilogram" and to_v == "Milligram":
        return value * (10**6)

    elif from_v == "Kilogram" and to_v == "Pound":
        return value * 2.20462

    elif from_v == "Kilogram" and to_v == "Tonne":
        return value * (10**-3)

    elif from_v == "Gram" and to_v == "Kilogram":
        return value * (10**-3)

    elif from_v == "Milligram" and to_v == "Kilogram":
        return value * (10**-6)

    elif from_v == "Pound" and to_v == "Kilogram":
        return value / 2.205

    elif from_v == "Tonne" and to_v == "Kilogram":
        return value * 1000

    elif from_v == "Ounce" and to_v == "Kilogram":
        return value / 35.274

    elif from_v == "Kilogram" and to_v == "Ounce":
        return value * 35.274
