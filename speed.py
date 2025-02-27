def speed(value, from_v, to_v):
    if from_v == to_v:
        return value

    elif from_v == "Meter/Second" and to_v == "Kilometer/Hour":
        return value * 3.6

    elif from_v == "Meter/Second" and to_v == "Miles/Hour":
        return value * 2.237

    elif from_v == "Meter/Second" and to_v == "Knots":
        return value * 1.151

    elif from_v == "Kilometer/Hour" and to_v == "Meter/Second":
        return value / 3.6

    elif from_v == "Miles/Hour" and to_v == "Meter/Second":
        return value / 2.373

    elif from_v == "Knots" and to_v == "Meter/Second":
        return value / 1.151
