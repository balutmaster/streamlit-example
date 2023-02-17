# Core Packages

import streamlit as st
from PIL import Image 

# Load EDA Pkg
import pandas as pd
import numpy as np

# load data visualization packages
import plotly.express as px

# Page Config

p_icon = Image.open("C:/GitHub/streamlit-example/Udemy/Intricity.png")
PAGE_CONFIG = {'page_title':'Rich - Streamlit Page','page_icon':p_icon,'layout':'centered','initial_sidebar_state':'auto'}
st.set_page_config(**PAGE_CONFIG)









def main():
    st.title("Plotting in Streamlit with Plotly")
    df = pd.read_csv("C:/GitHub/streamlit-example/Udemy/Streamlit_Data_Set_summary.csv")
    st.dataframe(df)
    
    # Pie Chart
    vs_1 = px.pie(df,values='QUERY_COUNT',names='WAREHOUSE_NAME', title='Warehouse Query Counts')
    st.plotly_chart(vs_1)
    
    # Bar Chart
    
    df_1 = pd.read_csv("C:/GitHub/streamlit-example/Udemy/Streamlit_Data_Set_detail.csv")
    st.dataframe(df_1)
    vs_2 = px.bar(df_1,x='QUERY_DATE',y='TOTAL_CREDITS_USED', title='Warehouse Credits Used')
    st.plotly_chart(vs_2)
    
    
    
if __name__ == '__main__':
    main()