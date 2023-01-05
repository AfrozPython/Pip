# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 18:42:26 2023

@author: Appu
"""


import streamlit as st
# Video Upload
video_file = open('Karina3.png', 'rb')
video_bytes = video_file.read()
st.image(video_bytes)


st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)
