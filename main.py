import mass, length, clock, times, temperature, speed
import streamlit as st
from streamlit_option_menu import option_menu


def main():
    st.set_page_config(page_title="Unit Converter", page_icon="⚖️")
    with st.sidebar:
        navigate = option_menu(
            menu_title="Unit Converter",
            menu_icon="calculator",
            options=["Length", "Mass", "Time", "Clock", "Temperature", "Speed"],
            icons=[
                "rulers",
                "speedometer2",
                "hourglass-split",
                "clock",
                "thermometer-sun",
                "speedometer",
            ],
            default_index=0,
        )

    if navigate == "Mass":
        st.title("Mass Converter")
        col1, col2 = st.columns([1, 2])

        with col1:
            from_v = st.selectbox(
                "From", ["Kilogram", "Gram", "Milligram", "Tonne", "Ounce", "Pound"]
            )
            to_v = st.selectbox(
                "To", ["Gram", "Kilogram", "Milligram", "Tonne", "Ounce", "Pound"]
            )
            press = st.button("Convert")

        with col2:
            value = st.number_input(" ")

            if press:
                if from_v == to_v:
                    new_value = mass.mass(value, from_v, to_v)
                    final = st.text_input(" ", str(new_value), key=1)

                elif from_v == "Kilogram" and to_v != "Kilogram":
                    new_value = mass.mass(value, from_v, to_v)
                    final = st.text_input(" ", str(new_value), key=1)

                else:
                    new_value = mass.mass(value, from_v, "Kilogram")
                    final = mass.mass(new_value, "Kilogram", to_v)
                    new_final = st.text_input(" ", str(final), key=1)
    elif navigate == "Length":
        st.title("Length Converter")
        col1, col2 = st.columns([1, 2])
        with col1:
            from_v = st.selectbox(
                "From",
                [
                    "Kilometer",
                    "Hectometer",
                    "Decameter",
                    "Meter",
                    "Decimeter",
                    "Centimeter",
                    "Millimeter",
                    "Feet",
                    "Inch",
                    "Mile",
                    "Yard",
                    "Nautical Miles",
                ],
            )
            to_v = st.selectbox(
                "To",
                [
                    "Meter",
                    "Hectometer",
                    "Decameter",
                    "Kilometer",
                    "Decimeter",
                    "Centimeter",
                    "Millimeter",
                    "Feet",
                    "Inch",
                    "Mile",
                    "Yard",
                    "Nautical Miles",
                ],
            )
            press = st.button("Convert")

        with col2:
            value = st.number_input(" ")

            if press:
                if from_v == to_v:
                    new_value = length.length(value, from_v, to_v)
                    final = st.text_input(" ", str(new_value), key=2)
                elif from_v == "Meter" and to_v != "Meter":
                    new_value = length.length(value, from_v, to_v)
                    st.text_input(" ", str(new_value), key=2)
                else:
                    new_value = length.length(value, from_v, "Meter")
                    final = length.length(new_value, "Meter", to_v)
                    st.text_input(" ", str(final), key=2)

    elif navigate == "Time":
        st.title("Time Converter")

        col1, col2 = st.columns([1, 2])
        with col1:
            from_v = st.selectbox(
                "From",
                ["Hours", "Minutes", "Seconds", "Days", "Weeks", "Months", "Years"],
            )
            to_v = st.selectbox(
                "To",
                ["Minutes", "Hours", "Seconds", "Days", "Weeks", "Months", "Years"],
            )

            press = st.button("Convert")

        with col2:
            value = st.number_input(" ")

            if press:
                if from_v == to_v:
                    new_value = times.times(value, from_v, to_v)

                    st.text_input(" ", str(new_value))

                elif from_v == "Hours" and to_v != "Hours":
                    new_value = times.times(value, from_v, to_v)
                    st.text_input(" ", str(new_value))

                else:
                    new_value = times.times(value, from_v, "Hours")
                    final = times.times(new_value, "Hours", to_v)
                    st.text_input(" ", str(final))
    elif navigate == "Clock":
        st.title("Clock Converter")
        col1, col2 = st.columns([1, 2])
        with col1:
            from_v = st.selectbox("From", ["12 Hour", "24 Hour"])
            to_v = st.selectbox("To", ["24 Hour", "12 Hour"])

            if from_v == "12 Hour":
                am_pm = st.radio("Select am/pm", ["am", "pm"])

            press = st.button("Convert")

        with col2:
            value = st.text_input(" ").strip()
            if from_v == "12 Hour":
                value = value + f":{am_pm}"

            if press:
                value = clock.clock(value, from_v, to_v)
                if value:
                    st.text_input(" ", value)
                else:
                    special = ":"
                    st.error(f"Input not in time format ")

    elif navigate == "Temperature":
        st.title("Temperature Converter")
        col1, col2 = st.columns([1, 2])

        with col1:
            from_v = st.selectbox("From", ["Celcius", "Farenheit", "Kelvin"])
            to_v = st.selectbox("To", ["Farenheit", "Celcius", "Kelvin"])
            press = st.button("Convert")

        with col2:
            value = st.number_input(" ")
            if press:
                new_value = temperature.temperature(value, from_v, to_v)
                st.text_input(" ", str(new_value), key=4)
    elif navigate == "Speed":
        st.title("Speed Converter")
        col1, col2 = st.columns([1, 2])
        with col1:
            from_v = st.selectbox(
                "From",
                ["Meter/Second", "Kilometer/Hour", "Knots", "Miles/Hour"],
            )
            to_v = st.selectbox(
                "To",
                ["Meter/Second", "Kilometer/Hour", "Knots", "Miles/Hour"],
            )

            press = st.button("Convert")

        with col2:
            value = st.number_input(" ")

            if press:
                if from_v == to_v:
                    new_value = speed.speed(value, from_v, to_v)
                    st.text_input(" ", str(new_value), key=5)

                elif from_v == "Meter/Second" and to_v != "Meter/Second":
                    new_value = speed.speed(value, from_v, to_v)

                    st.text_input(" ", str(new_value), key=5)

                else:
                    new_value = speed.speed(value, from_v, "Meter/Second")
                    final = speed.speed(new_value, "Meter/Second", to_v)

                    st.text_input(" ", str(final), key=5)


if __name__ == "__main__":
    main()
