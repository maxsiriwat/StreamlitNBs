import streamlit as st
import pandas as pd
import numpy as np
import pickle as pickle

store = pickle.load(open("model","rb" ) )

st.header("ทำนายความเสี่ยงของการตกเลือด")
st.write("")
Age = st.number_input('Age (อายุ)',min_value=1,max_value=100,step=1,value=20,key='None')
Gestation = st.number_input('Gestation (จำนวนการตั้งครรภ์ รวมปัจจุบัน รวมแท้ง)',min_value=1,max_value=20,value=1,key='None')
Parity = st.number_input('Parity (จำนวนลูกที่คลอดออกมาได้)',min_value=0,max_value=20,value=1,key='None')
GA = st.number_input('GA (อายุครรภ์ต่อสัปดาห์)',min_value=1,max_value=100,value=30,key='None')
Hct = st.number_input('Hct (ความเข้มข้นเลือด)',min_value=1,max_value=100,value=30,key='None')
height = st.number_input("height (ความสูง) ซม.",min_value=1,max_value=250,value=150)
weight = st.number_input("weight (น้ำหนัก) กก.",min_value=1,max_value=200,value=50)
BMI = weight / (height/100)**2
BMI = st.number_input('BMI (ค่า BMI)',value=BMI,key='None')
HxPPH = st.radio('Hx PPH (เคยตกเลือดมาก่อนในท้องที่แล้ว)',('เคย','ไม่เคย'),key='None')
if HxPPH == 'เคย':
    HxPPH = 1
elif HxPPH == 'ไม่เคย':
    HxPPH = 0
DM = st.radio('DM (เป็นเบาหวานในท้องนี้)',('เป็น','ไม่เป็น'),key='None')
if DM == 'เป็น':
    DM = 1
elif DM == 'ไม่เป็น':
    DM = 0
PIH = st.radio(
    "PIH (มีประวัติความดันสูงขณะตั้งครรภ์)",
    ('มี','ไม่มี'))
if PIH == 'มี':
    PIH = 1
elif PIH == 'ไม่มี':
    PIH = 0
submit = st.button('Predict')



if submit:
    y = store.predict([[Age,Gestation,Parity,GA,Hct,BMI,HxPPH,DM,PIH]])
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