# menu driven python command line program to convert one unit of time to another.


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


def main():
    while True:
        print("*****************************************************************")
        print(
            """\tAvailable Units for Conversion
              1. Hours
              2. Minutes
              3. Seconds
              4. Days
              5.Weeks
              6.Months
              7.Years
              
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
            value = float(input("Enter the value "))
        except ValueError:
            print("Enter a valid time .....\n")
            continue

        units = {
            1: "Hours",
            2: "Minutes",
            3: "Seconds",
            4: "Days",
            5: "Weeks",
            6: "Months",
            7: "Years",
        }

        if from_v in units and to_v in units:
            if from_v == to_v:
                new_value = times(
                    value, units[from_v].capitalize(), units[to_v].capitalize()
                )
            elif units[from_v] == "Hours" and units[to_v] != "Hours":
                new_value = times(
                    value, units[from_v].capitalize(), units[to_v].capitalize()
                )

            else:
                final = times(value, units[from_v].capitalize(), "Hours")
                new_value = times(final, "Hours", units[to_v].capitalize())

            print()
            print(f"the time is {new_value} {units[to_v]}\n")

        else:
            print("Enter a valid unit....\n")

        choice = input("Do you want to continue (y/n) ")

        if choice.strip().lower() == "n":
            print("Exiting from the program....")
            break


if __name__ == "__main__":
    main()
