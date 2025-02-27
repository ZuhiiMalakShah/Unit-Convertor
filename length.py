def length(value, from_v, to_v):
    if from_v == to_v:
        return value

    elif from_v == "Meter" and to_v == "Kilometer":
        return value / 1000

    elif from_v == "Meter" and to_v == "Hectometer":
        return value / 100

    elif from_v == "Meter" and to_v == "Decameter":
        return value / 10

    elif from_v == "Meter" and to_v == "Decimeter":
        return value * 10

    elif from_v == "Meter" and to_v == "Centimeter":
        return value * 100
    elif from_v == "Meter" and to_v == "Millimeter":
        return value * 1000

    elif from_v == "Meter" and to_v == "Feet":
        return value * 3.281
    elif from_v == "Meter" and to_v == "Inch":
        return value * 39.37
    elif from_v == "Meter" and to_v == "Mile":
        return value / 1609

    elif from_v == "Meter" and to_v == "Yard":
        return value * 1.094

    elif from_v == "Meter" and to_v == "Nautical Miles":
        return value / 1852

    elif from_v == "Kilometer" and to_v == "Meter":
        return value * 1000

    elif from_v == "Hectometer" and to_v == "Meter":
        return value * 100

    elif from_v == "Decameter" and to_v == "Meter":
        return value * 10

    elif from_v == "Decimeter" and to_v == "Meter":
        return value / 10

    elif from_v == "Centimeter" and to_v == "Meter":
        return value / 100

    elif from_v == "Millimeter" and to_v == "Meter":
        return value / 1000

    elif from_v == "Feet" and to_v == "Meter":
        return value / 3.281

    elif from_v == "Inch" and to_v == "Meter":
        return value / 39.37

    elif from_v == "Yard" and to_v == "Meter":
        return value / 1.094

    elif from_v == "Nautical Miles" and to_v == "Meter":
        return value * 1852
