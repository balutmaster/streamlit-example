# Core Pkgs
import streamlit as st 

# Working with widgets
# Buttons/Radio/CheckBox/Select/Multi-Select/Sliders/Select Sliders

# Working with buttons
name = "Rich"

if st.button("Submit"):
    st.write("Name: {}".format(name.upper()))
    
if st.button("Submit",key='new02'):
    st.write("First Name: {}".format(name.lower()))    
    
# Working with Radio
status = st.radio("What is your status?" , ("Active","Inactive"))
if status == 'Active':
    st.success("You are active")
elif status == 'Inactive':
    st.warning("You are NOT active")


# Working with CheckBox
if st.checkbox("Show/Hide"):
    st.text("Showing Something")

# Working with expander
with st.expander("Python"):
    st.success("Hello Python")   

with st.expander("Rich"):
    st.text("Hello Rich") 


# Working with Select
