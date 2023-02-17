# Core Packages

import streamlit as st
from PIL import Image 
import pandas as pd



# Load EDA Pkg
import pandas as pd
import numpy as np

# load data visualization packages
import plotly.express as px

from snowflake.snowpark import Session, exceptions

connection_parameters = {
    "account": "intricity.east-us-2.azure",
    "user": "rhathaway",
    "password": "AQr#Kc5@",
    "role": "sysgen",  # optional
    "warehouse": "stats_gen",  # optional
    "database": "admin",  # optional
    "schema": "stats",  # optional
}  

session = Session.builder.configs(connection_parameters).create()


def run_sync_sql(session, sql2run):
    # Query Processing
    try:
        res = session.sql(sql2run).collect()
        return res
    except exceptions.SnowparkSQLException as e:
        print(f'Snowflake query error was raised:\nQuery with issues:\n\n{sql2run.lstrip()}\n')
        print(f'The query failed with an error {e.error_code} {e.message}\n\tSee Query_ID: {e.sfqid} for more details\n')

# Page Config

p_icon = Image.open("C:/GitHub/streamlit-example/FlowObjects/FlowObjectsLogo_sm.png")
#p_icon = Image.open("C:/GitHub/streamlit-example/Udemy/Intricity.png")
PAGE_CONFIG = {'page_title':'FlowObjects - Snowflake Audit and Monitor','page_icon':p_icon,'layout':'centered','initial_sidebar_state':'auto'}
st.set_page_config(**PAGE_CONFIG)


def load_image(image_file):
    img = Image.open(image_file)
    return img

#@st.cache
def main():
    main_logo = ("C:/GitHub/streamlit-example/FlowObjects/FlowObjectsLogo.png")
    #st.image(load_image(main_logo))
    st.image(load_image(main_logo),width=200)
    st.title("Snowflake Audit & Monitoring")
    
    
    
    menu = ["Home","General Snowflake","Access Control","Query Performance","Storage","Usage","Virtual Warehouses","About"]
    choice = st.sidebar.selectbox("Audit & Monitor Areas",menu)
    
    if choice == "Home":
        st.subheader("Home")
        
    
    elif choice == "General Snowflake":
        st.subheader("General Snowflake")
        df = pd.read_csv("C:/GitHub/streamlit-example/Udemy/Streamlit_Data_Set_summary.csv")
        # Pie Chart
        vs_1 = px.pie(df,values='QUERY_COUNT',names='WAREHOUSE_NAME', title='Warehouse Query Counts')
        st.plotly_chart(vs_1)
        
    
    elif choice == "Access Control":
        st.subheader("Access Control")
        # Bar Chart
    
        df_1 = pd.read_csv("C:/GitHub/streamlit-example/Udemy/Streamlit_Data_Set_detail.csv")
        st.dataframe(df_1)
        vs_2 = px.bar(df_1,x='QUERY_DATE',y='TOTAL_CREDITS_USED', title='Warehouse Credits Used')
        st.plotly_chart(vs_2)
    
    elif choice == "Query Performance":
        st.subheader("Query Performance")
        sql2run = f"""select * from admin.stats.large_table"""
        lt = run_sync_sql(session, sql2run)
        vs_large_table = px.bar(lt,x='TABLE_PATH',y='SIZE_GB',title='Large Tables')
        st.plotly_chart(vs_large_table)
    
    elif choice == "Storage":
        st.subheader("Storage")
    
    elif choice == "Usage":
        st.subheader("Usage")
    
    elif choice == "Virtual Warehouses":
        st.subheader("Virtual Warehouses")
        # Bar Chart
    
        df_1 = pd.read_csv("C:/GitHub/streamlit-example/Udemy/Streamlit_Data_Set_detail.csv")
        st.dataframe(df_1)
        vs_2 = px.bar(df_1,x='QUERY_DATE',y='TOTAL_CREDITS_USED', title='Warehouse Credits Used')
        st.plotly_chart(vs_2)
                    

    
    elif choice == "About":
        st.subheader("About")
    
    
if __name__ == '__main__':
    main()