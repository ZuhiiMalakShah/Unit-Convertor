def temperature(value, from_v, to_v):
    if from_v == to_v:
        return value
    elif from_v == "Celcius" and to_v == "Farenheit":
        return (value * 9 / 5) + 32

    elif from_v == "Farenheit" and to_v == "Celcius":
        return (value - 32) * 5 / 9

    elif from_v == "Celcius" and to_v == "Kelvin":
        return value + 273.15

    elif from_v == "Kelvin" and to_v == "Celcius":
        return value - 273.15

    elif from_v == "Farenheit" and to_v == "Kelvin":
        return ((value - 32) * (5 / 9)) + 273.15

    elif from_v == "Kelvin" and to_v == "Farenheit":
        return ((value - 273.15) * (9 / 5)) + 32
