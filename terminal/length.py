# menu driven command line python program to convert length from one unit to another.


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


def main():
    while True:
        print("*****************************************************************")
        print(
            """\tAvailable Units for Conversion
              1. Kilometer
              2. Hectometer
              3. Decameter
              4. Meter
              5.Decimeter
              6.Centimeter
              7.Millimeter
              8.Feet
              9.Inch
              10.Yard
              11.Nautical Miles
              """
        )
        print("*****************************************************************")
        print()

        try:
            from_v = int(input("Enter the unit you want to convert from "))
            to_v = int(input("Enter the unit you want to convert to "))
        except ValueError:
            print("Enter a valid choice....\n")
            continue

        try:
            value = float(input("Enter the length "))
        except ValueError:
            print("Enter a valid length .....\n")
            continue

        units = {
            1: "kilometer",
            2: "hectometer",
            3: "decameter",
            4: "meter",
            5: "decimeter",
            6: "centimeter",
            7: "millimeter",
            8: "feet",
            9: "inch",
            10: "yard",
            11: "nautical miles",
        }

        if from_v in units and to_v in units:
            if from_v == to_v:
                new_value = length(
                    value, units[from_v].capitalize(), units[to_v].capitalize()
                )
            elif units[from_v] == "Meter" and units[to_v] != "Meter":
                new_value = length(
                    value, units[from_v].capitalize(), units[to_v].capitalize()
                )

            else:
                final = length(value, units[from_v].capitalize(), "Meter")
                new_value = length(final, "Meter", units[to_v].capitalize())

            print()
            print(f"the length is {new_value} {units[to_v]}\n")

        else:
            print("Enter a valid unit....\n")

        choice = input("Do you want to continue (y/n) ")

        if choice.strip().lower() == "n":
            print("Exiting from the program....")
            break


if __name__ == "__main__":
    main()
