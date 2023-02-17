# Core Packages

import streamlit as st
from PIL import Image 
import pandas as pd
import docx2txt 
from PyPDF2 import PdfFileReader 
import pdfplumber 



# Load EDA Pkg
import pandas as pd
import numpy as np

# load data visualization packages
import plotly.express as px

# Page Config

p_icon = Image.open("C:/GitHub/streamlit-example/Udemy/Intricity.png")
PAGE_CONFIG = {'page_title':'Rich - Streamlit Page','page_icon':p_icon,'layout':'centered','initial_sidebar_state':'auto'}
st.set_page_config(**PAGE_CONFIG)


def load_image(image_file):
    img = Image.open(image_file)
    return img

#@st.cache
def main():
    st.title("File Uploads in Streamlit")
    st_file_uploads_dg = Image.open("C:/GitHub/streamlit-example/Udemy/streamlit_file_upload.png")
    
    menu = ["Home","Dataset","DocumentFiles","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Home")
        st.image(st_file_uploads_dg,use_column_width=True)
        image_file = st.file_uploader("Upload Images",type=["png","jpg","jpeg"])
        if image_file is not None:
            # See Details
            st.write(type(image_file))
            #st.write(dir(image_file))
            file_details = {"filename":image_file.name,
                            "filetype":image_file.type,
                            "filesize":image_file.size}
            st.write(file_details)
            
            #st.image(load_image(image_file),width=250)
            st.image(load_image(image_file))
    
    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV",type=["csv"])
        if data_file is not None:
            # See Details
            st.write(type(data_file))
            #st.write(dir(data_file))
            file_details = {"filename":data_file.name,
                            "filetype":data_file.type,
                            "filesize":data_file.size}
            st.write(file_details)
            df = pd.read_csv(data_file)
            st.dataframe(df)
        
    
    elif choice == "DocumentFiles":
        st.subheader("DocumentFiles")
        docx_file = st.file_uploader("Upload Document",
                                     type=["PDF","docx","txt"])
        if st.button("Process"):
            if docx_file is not None:
                # See Details
                st.write(type(docx_file))
                #st.write(dir(data_file))
                file_details = {"filename":docx_file.name,
                                "filetype":docx_file.type,
                                "filesize":docx_file.size}
                st.write(file_details)
                if docx_file.type == "text/plain":
                    # Read as bytes
                    #raw_text = docx_file.read()
                    #st.write(raw_text) 
                    #st.text(raw_text)
                    
                    # Read as string (decode bytes to string)
                    raw_text = str(docx_file.read(),"utf-8")
                    st.write(raw_text)  
                    

    
    elif choice == "About":
        st.subheader("About")
    
    
if __name__ == '__main__':
    main()