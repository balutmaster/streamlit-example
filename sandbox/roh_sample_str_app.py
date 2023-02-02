import streamlit as st

st.title('📈 My first app')

st_name = st.sidebar.text_input('Enter your name','')

#st.write(f'Hello World {st_name}!')
st.write('Hello', st_name )