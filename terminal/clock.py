# menu driven python program to convert different time formats

import re

conversion = {
    00: 12,
    13: 1,
    14: 2,
    15: 3,
    16: 4,
    17: 5,
    18: 6,
    19: 7,
    20: 8,
    21: 9,
    22: 10,
    23: 11,
}
conversion_2 = {
    1: 13,
    2: 14,
    3: 15,
    4: 16,
    5: 17,
    6: 18,
    7: 19,
    8: 20,
    9: 21,
    10: 22,
    11: 23,
}


def clock(value, from_v, to_v):
    if from_v == "12 Hour" and to_v == "12 Hour":
        check = validate(value, from_v)
        if check:
            return value
        else:
            return False

    if from_v == "24 Hour" and to_v == "24 Hour":
        check = validate(value, from_v)
        if check:
            return value
        else:
            return False

    if from_v == "24 Hour" and to_v == "12 Hour":
        check = validate(value, from_v)
        if check:
            hour, minutes = value.split(":")
            if int(hour) >= 12:
                am_pm = "pm"
                hour_24 = conversion[int(hour)]

            else:
                am_pm = "am"
                hour_24 = hour
            if len(minutes) == 1:
                minutes = f"0+{minutes}"

        else:
            return False

        return f"{str(hour_24)}:{minutes} {am_pm}"

    if from_v == "12 Hour" and to_v == "24 Hour":
        check = validate(value, from_v)
        if check:
            hour, minutes, am_pm = value.split(":")
            if am_pm == "am" and int(hour) != 12:
                if len(hour) == 1:
                    hour = "0" + hour
                if len(minutes) == 1:
                    minutes = "0" + minutes

                return f"{hour}:{minutes}"
            elif am_pm == "am" and int(hour) == 12:
                hour = "00"
                if len(minutes) == 1:
                    minutes = "0" + minutes
                return f"{hour}:{minutes}"

            elif am_pm == "pm":
                hour = conversion_2[int(hour)]
                if len(minutes) == 1:
                    minutes = "0" + minutes

                return f"{hour}:{minutes}"

        else:
            return False


def validate(value, from_v):
    if from_v == "24 Hour":
        if re.search(r"^(0?[1-9]|1[0-9]|2[0-4]):(0?[0-9]|[1-5][0-9])$", value):
            return True
        else:
            return False
    else:
        if re.search(r"^(0?[0-9]|1[1-2]):(0?[0-9]|[1-5][0-9]):(am|pm)$", value):
            return True
        else:
            return False


def main():
    while True:
        print()
        print(
            "*************************************************************************"
        )
        print(
            """
              \t\t\tMENU
              1. 12 Hour format to 24 Hour format
              2.24 Hour format to 12 Hour format
              3.Exit from Program

              """
        )
        print(
            "*************************************************************************"
        )

        choice = int(input("Enter the choice "))
        print()

        if choice == 2:
            input_time = input("Enter the time in 24 hour format ").strip().lower()
            output_time = clock(input_time, "24 Hour", "12 Hour")

            if output_time:
                print(f"The time in 12 Hour fomat is {output_time}\n")

            else:
                print("The time inputted is not in correct format.. please try again\n")

        elif choice == 1:
            input_time = input("Enter the time ").strip().lower()
            am_pm = input("Enter am/pm ").strip().lower()
            new_input_time = input_time + f":{am_pm}"
            output_time = clock(new_input_time, "12 Hour", "24 Hour")

            if output_time:
                print(f"The time in 24 Hour format is {output_time}\n")

            else:
                print("Inputted time not in correct format ... please try again...\n")
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Enter a valid choice...\n")


if __name__ == "__main__":
    main()
