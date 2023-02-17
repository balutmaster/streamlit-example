import toml
import streamlit as st 
import pandas as pd 
import snowflake.connector as sf
from datetime import date 

sidebar = st.sidebar
   
def connect_to_snowflake(acct,usr,pwd,rl,wh,db):
    ctx = sf.connect(user=usr,account=acct,password=pwd,role=rl,warehouse=wh,database=db)
    cs = ctx.cursor()
    st.session_state['snow_conn'] = cs
    st.session_state['is_ready'] = True
    return cs

#@st.cache()
def get_data():
    query = 'select    warehouse_name \
        , query_type \
        , usage_date  \
        , hour as usage_hour_ind_day \
        , sum(execution_time) as total_execution_time \
        , sum(compilation_time) as total_compliation_time \
        , sum(queued_overload_time) as total_queued_load_time \
        , sum(total_elapsed_time) as total_elapsed_time \
        , sum(credits_used_cloud_services) as cloud_services_credits \
        , sum(est_credits) as total_estimated_credits \
        , sum(qry_cnt) as total_query_count \
from admin.stats.warehouse_credit_usage \
where usage_date >= current_date() - 90 \
group by 1, 2, 3, 4 \
order by 1, 2, 3, 4 \
;'
    results = st.session_state['snow_conn'].execute(query)
    #results = st.session_state['snow_conn'].fetch_pandas_all()
    return results 


with sidebar:
    account = st.text_input("Account")
    username = st.text_input("Username")
    password = st.text_input("Password",type="password")
    role = st.text_input("Role")
    wh = st.text_input("Virtual Warehouse")
    db = st.text_input("Database")
    connect = st.button("Connect to Snowflake", \
        on_click=connect_to_snowflake, \
        args=[account,username, password, role, wh, db])

if 'is_ready' not in st.session_state:
    st.session_state['is_ready'] = False

   
if st.session_state['is_ready'] == True:
    data = get_data()
    df = pd.DataFrame(data)
    st.dataframe(df,use_container_width=False)