# menu driven command line python program for converting different speeds.


def speed(value, from_v, to_v):
    if from_v == to_v:
        return value

    elif from_v == "meter/second" and to_v == "kilometer/hour":
        return value * 3.6

    elif from_v == "meter/second" and to_v == "miles/hour":
        return value * 2.237

    elif from_v == "meter/second" and to_v == "knots":
        return value * 1.151

    elif from_v == "kilometer/hour" and to_v == "meter/second":
        return value / 3.6

    elif from_v == "miles/hour" and to_v == "meter/second":
        return value / 2.373

    elif from_v == "knots" and to_v == "meter/second":
        return value / 1.151


def main():
    while True:
        print("*****************************************************************")
        print(
            """\tAvailable Units for Conversion
              1. Kilometer/Hour
              2. Meter/Second
              3. Miles/Hour
              4. Knots
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
            value = float(input("Enter the speed "))
        except ValueError:
            print("Enter a valid speed .....\n")
            continue

        units = {1: "kilometer/hour", 2: "meter/second", 3: "miles/hour", 4: "knots"}

        if from_v in units and to_v in units:
            if from_v == to_v:
                new_value = speed(value, units[from_v], units[to_v])
            elif units[from_v] == "meter/second" and units[to_v] != "meter/second":
                new_value = speed(value, units[from_v], units[to_v])

            else:
                final = speed(value, units[from_v], "meter/second")
                new_value = speed(final, "meter/second", units[to_v])

            print()
            print(f"the speed is {new_value} {units[to_v]}\n")

        else:
            print("Enter a valid unit....\n")

        choice = input("Do you want to continue (y/n) ")

        if choice.strip().lower() == "n":
            print("Exiting from the program....")
            break


if __name__ == "__main__":
    main()
