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
