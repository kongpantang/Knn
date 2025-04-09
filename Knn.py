from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.header('การจำแนกข้อมูลด้วยเทคนิค ML')
st.image("./img/img1.jpg")
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Versicolor")
   st.image("./img/img2.jpg")

with col2:
   st.header("Verginiga")
   st.image("./img/img3.jpg")

with col3:
   st.header("Setosa")
   st.image("./img/img4.jpg")

html_7 = """
<div style="background-color:#33a5ff;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:white">
<center><h5>ข้อมูล หรือ ข้อมูลสำหรับทำนาย</h5></center>
</div>
"""
st.markdown(html_7, unsafe_allow_html=True)
st.markdown("")
st.markdown("")