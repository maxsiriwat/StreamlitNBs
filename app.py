import streamlit as st
import pandas as pd
import numpy as np
import pickle as pickle

store = pickle.load(open("clf","rb" ) )

st.header("ทำนายความเสี่ยงของการตกเลือด")
st.write("")
Age = st.number_input('Age (อายุ)',step=1,key='None')
Gestation = st.number_input('Gestation (จำนวนการตั้งครรภ์ รวมปัจจุบัน รวมแท้ง)',key='None')
Parity = st.number_input('Parity (จำนวนลูกที่คลอดออกมาได้)',key='None')
GA = st.number_input('GA (อายุครรภ์ต่อสัปดาห์)',key='None')
height = st.number_input("height (ความสูง) ซม.",value=1)
weight = st.number_input("weight (น้ำหนัก) กก.",value=1)
BMI = weight / (height/100)**2
BMI = st.number_input('BMI (ค่า BMI)',value=BMI,key='None')
HxPPH = st.number_input('Hx PPH (เคยตกเลือดมาก่อนในท้องที่แล้ว)',key='None')
DM = st.number_input('DM (เป็นเบาหวานในท้องนี้)',key='None')
PIH = st.number_input('PIH (มีประวัติความดันสูงขณะตั้งครรภ์)',key='None')
submit = st.button('Predict')

if submit:
    y = store.predict([[Age,Gestation,Parity,GA,BMI,HxPPH,DM,PIH]])
    if Age == 0:
        st.info('กรุณากรอกข้อมูลให้ครบถ้วน (Age)')
    elif Gestation == 0:
        st.info('กรุณากรอกข้อมูลให้ครบถ้วน (Gestation)')
    elif GA == 0:
        st.info('กรุณากรอกข้อมูลให้ครบถ้วน (GA)')
    elif BMI < 0 or BMI > 100:
        st.info('ข้อมูลไม่ถูกต้อง (BMI)')
    elif y == 0:
        st.balloons()
        st.write("")
        st.success('คุณไม่อยู่ในกลุ่มเสี่ยงของการตกเลือด')
    elif y == 1:
        st.error('คุณอยู่ในกลุ่มเสี่ยงของการตกเลือด')