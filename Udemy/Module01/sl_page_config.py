# Core Packages

import streamlit as st
from PIL import Image

#method 1
#must be the first activity of the Streamlit file and can only be set once 
p_icon = Image.open("C:/GitHub/streamlit-example/Udemy/Intricity.png")
#st.set_page_config(page_title='Rich - Streamlit Page'
#                   ,page_icon=p_icon
#                   ,layout='wide'
#                   ,initial_sidebar_state='expanded')

# method 2: dictionary
PAGE_CONFIG = {'page_title':'Rich - Streamlit Page','page_icon':p_icon,'layout':'centered','initial_sidebar_state':'auto'}
st.set_page_config(**PAGE_CONFIG)


def main():
    # Image from url
    st.text('Image from URL 🦈')
    st.image('https://www.intricity.com/hubfs/Full-Logo%20-%20white@4x.png',caption='www.intiricty.com')
    
    st.sidebar.success('Menu')
    
main()