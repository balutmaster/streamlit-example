# Basics and Fundamentals

# Core Packages
import streamlit as st

#Load EDA Packages
import pandas as pd 

# Display Data
df = pd.read_csv("iris.csv")

# Method 1 
st.dataframe(df)
# Control height and width
# st.dataframe(df,200,100)

# Adding color style from Pandas

st.dataframe(df.style.highlight_max(axis=0))


# Method 2: Static Table
st.table(df)

# Method 3: Using super function st.write
st.write(df.head())

# Display Json
st.json({'data':"name"})

# Display Code
mycode = """ 
def sayhello():
    print("Hello Streamlit")
"""
st.code(mycode, language='python')