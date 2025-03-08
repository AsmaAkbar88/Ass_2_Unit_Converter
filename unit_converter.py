# pip install streamlit

import  streamlit as st

st.set_page_config(page_title = "⏳ Unit Converter", layout = 'wide')
st.title("🌏 Unit Converter")
st.subheader(" Converters Distance, Length, Weight and Time Instantly")
st.write("Welcome ! Select a category, enter a value and get the converted result in real time")

category = st.sidebar.selectbox("Select Category" , ["Distance","Length" , "Weight","Time"])

# =======================================================================================(function distance )
def distance_converter(from_unit, to_unit , value):
    units= {
        "Meters":1 ,
        "Kilometers":1000,
        "Feet": 0.3048,
        "Miles": 1609.34
    }
    result =  value * units[ from_unit] / units[to_unit]
    return result 
# ========================================================================================(function length)
def length_converter(from_unit, to_unit , value):
    units= {
        "Kilometers": 0.621371,
        "Miles": 1 / 0.621371,
    }
    result =  value * units[ from_unit] / units[to_unit]
    return result 
# =========================================================================================( function weight) 
def weight_converter(from_unit, to_unit , value):
    units= {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592
    }
    result =  value * units[ from_unit] / units[to_unit]
    return result 
# ===================================================================================== ===( funtion time )
def time_converter(from_unit, to_unit , value):
    units= {
        "Seconds": 1,
        "Minutes": 60,
        "Hours": 3600,
        "Days" : 86400,
    }
    result =  value * units[ from_unit] / units[to_unit]
    return result 
# =====================================================================================(2nd last )



#  =======================================================================================(Condition Distance)
if category == "Distance" :
    col1, col2 = st.columns(2)  
    from_unit = col1.selectbox("From: ", ["Meters" , "Kilometers", "Feet" ,"Miles"])
    to_unit = col2.selectbox("To : ", ["Meters" , "Kilometers", "Feet" ,"Miles"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
        result = distance_converter(from_unit , to_unit , value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit }")
# ====================================================================================(Condition Length)
elif category == "Length" :
    col1, col2 = st.columns(2)
    from_unit = col1.selectbox("From: ", ["Kilometers", "Miles"])
    to_unit = col2.selectbox("To: ", ["Kilometers", "Miles"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
        result = length_converter(from_unit , to_unit , value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit }")

# ========================================================================================(Condition weight)

elif category == "Weight" :
    col1, col2 = st.columns(2)
    from_unit = col1.selectbox("From: ", ["Kilograms","Grams", "Pounds"])
    to_unit = col2.selectbox("To:  ", ["Kilograms","Grams", "Pounds"])
    value = st.number_input("Enter Value ")
    if st.button("Convert"):
        result = weight_converter(from_unit , to_unit , value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit }")

# ========================================================================================(Condition Time)

elif category == "Time" :
    col1, col2 = st.columns(2)
    from_unit = col1.selectbox("From: ", ["Seconds" , "Minutes" , "Hours", "Days"])
    to_unit = col2.selectbox("To: ", ["Seconds" , "Minutes" , "Hours", "Days"])
    value = st.number_input("Enter Value ")
    if st.button("Convert"):
        result = time_converter(from_unit , to_unit , value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit }")
st.markdown("<h6 style='text-align: right; color: gray;'> 2025 © Code & Creativity by Asma Akbar ✨ </h6>" , unsafe_allow_html=True)
