#menu driven command line python program to convert one unit of mass to another.

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


def main():
    while True:
        print("*****************************************************************")
        print(
            """\tAvailable Units for Conversion
              1. Kilogram
              2. Gram
              3. Milligram
              4. Pound
              5.Ounce
              6.Tonne
              
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
            value = float(input("Enter the mass "))
        except ValueError:
            print("Enter a valid mass .....\n")
            continue

        units = {
            1: "Kilogram",
            2: "Gram",
            3: "Milligram",
            4: "Pound",
            5: "Ounce",
            6: "Tonne",
        }

        if from_v in units and to_v in units:
            if from_v == to_v:
                new_value = mass(
                    value, units[from_v].capitalize(), units[to_v].capitalize()
                )
            elif units[from_v] == "Kilogram" and units[to_v] != "Kilogram":
                new_value = mass(
                    value, units[from_v].capitalize(), units[to_v].capitalize()
                )

            else:
                final = mass(value, units[from_v].capitalize(), "Kilogram")
                new_value = mass(final, "Kilogram", units[to_v].capitalize())

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
