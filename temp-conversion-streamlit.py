# PossiblyAxolotl
# Temperature Unit Converter using Streamlit
# Oct 18, 2023

import streamlit as st
st.title("Temperature Converter")

# freezing points and boiling points of water in units, easy to add other units
freezing_points = {"Celsius":0,"Fahrenheit":32,"Kelvin":273.15}
boiling_points = {"Celsius":100,"Fahrenheit":212,"Kelvin":373.15}

# convert units to & from a value based on freezing & boiling point
def convert_from_units_to_value(value, freezingPoint, boilingPoint):
    return (value-freezingPoint) / (boilingPoint-freezingPoint)

def convert_to_units_from_value(units, freezingPoint, boilingPoint):
    return (units * (boilingPoint-freezingPoint)) + freezingPoint

def convert_units(units, unit_from, unit_to):
    value = convert_from_units_to_value(units, freezing_points[unit_from], boiling_points[unit_from])
    return round(convert_to_units_from_value(value, freezing_points[unit_to], boiling_points[unit_to]), 2)

# get values
value_input = st.number_input(label="Value to convert",value=0.0,placeholder="Type the value to convert")

unit_from = st.selectbox("Units to convert from", ["Celsius","Fahrenheit","Kelvin"])
unit_to = st.selectbox("Units to convert to", ["Celsius","Fahrenheit","Kelvin"])

# update, convert, and print values
st.write(f"{value_input}° {unit_from} is equal to {convert_units(value_input, unit_from, unit_to)}° {unit_to}")