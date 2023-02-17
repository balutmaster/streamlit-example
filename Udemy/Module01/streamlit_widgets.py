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
my_lang = ["Python","C#","SQL","Java"]

choice = st.selectbox("Language",my_lang)
st.write("You Selected {}".format(choice))

# Multiple Selection

spoken_lang = ("English","Filipino","Korean","German")
my_spoken_lang = st.multiselect("Spoken Language",spoken_lang,default="English")

# Slider
# Numbers (Int, Float, Date)
age = st.slider("Age",1,100,25)

# Select Slider
# Any Datatype
color = st.select_slider("Choose Color", options= ["Red","Blue","Yellow","Green","Black"],value=("Blue","Green"))
