def times(value, from_v, to_v):
    if from_v == to_v:
        return value
    elif from_v == "Hours" and to_v == "Minutes":
        return value * 60

    elif from_v == "Hours" and to_v == "Seconds":
        return value * 60 * 60

    elif from_v == "Hours" and to_v == "Days":
        return value / 24

    elif from_v == "Hours" and to_v == "Weeks":
        return value / 168

    elif from_v == "Hours" and to_v == "Months":
        return value / 730

    elif from_v == "Hours" and to_v == "Years":
        return value / 8760

    elif from_v == "Seconds" and to_v == "Hours":
        return value / 3600

    elif from_v == "Minutes" and to_v == "Hours":
        return value / 60

    elif from_v == "Days" and to_v == "Hours":
        return value * 24

    elif from_v == "Weeks" and to_v == "Hours":
        return value * 168

    elif from_v == "Months" and to_v == "Hours":
        return value * 730

    elif from_v == "Years" and to_v == "Hours":
        return value * 8760
