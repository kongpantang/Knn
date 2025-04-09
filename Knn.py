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
<div style="background-color:#33a5ff;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h4>ข้อมูล หรือ ข้อมูลสำหรับทำนาย</h4></center>
</div>
"""
st.markdown(html_7, unsafe_allow_html=True)
st.markdown("")
st.markdown("")

st.subheader("ข้อมูลส่วนแรก 10 แถว")
dt = pd.read_csv("./data/iris-3.csv")
st.write(dt.head(10))
st.subheader("ข้อมูลส่วนสุดท้าย 10 แถว")
st.write(dt.tail(10))

# สถิติพื้นฐาน
st.subheader("📈 สถิติพื้นฐานของข้อมูล")
st.write(dt.describe())

# การเลือกแสดงกราฟตามฟีเจอร์
st.subheader("📌 เลือกฟีเจอร์เพื่อดูการกระจายข้อมูล")
feature = st.selectbox("เลือกฟีเจอร์", dt.columns[:-1])

# วาดกราฟ boxplot
st.write(f"### 🎯 Boxplot: {feature} แยกตามชนิดของดอกไม้")
fig, ax = plt.subplots()
sns.boxplot(data=dt, x='variety', y=feature, ax=ax)
st.pyplot(fig)

# วาด pairplot
if st.checkbox("แสดง Pairplot (ใช้เวลาประมวลผลเล็กน้อย)"):
    st.write("### 🌺 Pairplot: การกระจายของข้อมูลทั้งหมด")
    fig2 = sns.pairplot(dt, hue='variety')
    st.pyplot(fig2)