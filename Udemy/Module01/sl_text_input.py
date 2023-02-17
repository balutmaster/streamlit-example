# Core Packages

import streamlit as st

# text input
fname = st.text_input("Enter first name")
st.title(fname)

# text input - hide password
password = st.text_input("Enter password",type='password')

# text area
message = st.text_area('Enter Message',height=100)
st.write(message)

# numbers
number = st.number_input('Enter number (Between 1 and 25)',1,25)
number = st.number_input('Enter number (Between 1.00 and 25.00)',1.00,25.00,2.5)

# date input
myappointment = st.date_input("Appointment")

# time input
mytime = st.time_input("My Time")

# color picker
color = st.color_picker('Select Color')