# menu driven python program for converting different temperatures


def main():
    while True:
        print()
        print(
            "***************************************************************************"
        )
        print(
            """
            \t\tmenu
              1.celsius to farenheit
              2.farenheit to celsius 
              3.celsius to kelvin
              4.kelvin to celsius
              5.farenheit to kelvin
              6.kelvin to farenheit
              7.exit from program\n"""
        )
        print(
            "***************************************************************************"
        )

        try:
            choice = int(input("Enter the choice "))
        except ValueError:
            print("Enter a valid choice....\n")
            continue

        if choice == 1:
            try:
                celcius = float(input("Enter the temperature in celsius "))
            except ValueError:
                print("Enter a valid temperature....\n")
                continue

            farenheit = (celcius * 9 / 5) + 32
            print(f"the temperature in farenheit is {farenheit}")

        elif choice == 2:
            try:
                farenheit = float(input("Enter the temperature in farenheit "))
            except ValueError:
                print("Enter a valid temperature ....\n")
                continue

            celsius = (farenheit - 32) * 5 / 9
            print(f"the temperature in celsius is {celsius}")

        elif choice == 3:
            try:
                celsius = float(input("Enter the temperature in celsius "))
            except ValueError:
                print("Enter a valid temperature ....\n")
                continue

            kelvin = celsius + 273.15
            print(f"the temperature in kelvin is {kelvin}")

        elif choice == 4:
            try:
                kelvin = float(input("Enter the temperature in kelvin "))
            except ValueError:
                print("Enter a valid temperature ....\n")
                continue

            celsius = kelvin - 273.15
            print(f"the temperature in celsius is {celsius}")

        elif choice == 5:
            try:
                farenheit = float(input("Enter the temperature in farenheit "))
            except ValueError:
                print("Enter a valid temperature ....\n")
                continue

            kelvin = ((farenheit - 32) * (5 / 9)) + 273.15
            print(f"the temperature in kelvin is {kelvin}")

        elif choice == 6:
            try:
                kelvin = float(input("Enter the temperature in kelvin "))
            except ValueError:
                print("Enter a valid temperature ....\n")
                continue

            farenheit = ((kelvin - 273.15) * (9 / 5)) + 32
            print(f"the temperature in farenheit is {farenheit}")

        elif choice == 7:
            print("exiting....")
            break

        else:
            print("Enter a valid input ")


if __name__ == "__main__":
    main()
