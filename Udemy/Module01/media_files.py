# Core Packages

import streamlit as st
from PIL import Image

# Working with media files (Videos, Images, audio)
# Display Images
st.text("Image from file")
img = Image.open("C:/GitHub/streamlit-example/Udemy/Module01/IntricityLogo.png")
#st.image(img)
#st.image(img,use_column_width=True)
st.image(img,width=200)


# from url
st.text('Image from URL')
st.image('https://www.intricity.com/hubfs/Full-Logo%20-%20white@4x.png',caption='www.intiricty.com')

# Display videos
st.text('embeded video')
video_file = open("C:/Users/rich/Videos/savior-christmas.mp4",'rb').read()
#st.video(video_file)
st.video(video_file,start_time=90)

# Audio files

st.text('embeded audio')
audio_file = open('C:/Users/rich/bob_shepard.mp3','rb') 
st.audio(audio_file.read(),format='audio/mp3')