import streamlit as st
import pandas as pd
import numpy as np
import pickle as pickle

store = pickle.load(open("clf.pkl","rb" ) )

st.header("Hello World 👏")
st.write("This is my first app eiei")
Age = st.number_input('Age',key='None')
Gestation = st.number_input('Gestation',key='None')
Parity = st.number_input('Parity',key='None')
GA = st.number_input('GA',key='None')
BMI = st.number_input('BMI',key='None')
DM = st.number_input('DM',key='None')
PIH = st.number_input('PIH',key='None')
submit = st.button('Predict')

if submit:
    y = store.predict([[Age,Gestation,Parity,GA,BMI,DM,PIH]])
    if y == 0:
        st.balloons()
        st.write("")
        st.success('ยินดีด้วย! คุณไม่อยู่ในกลุ่มเสี่ยงของการตกเลือด')
    else:
        st.error('เสียใจด้วย คุณอยู่ในกลุ่มเสี่ยงของการตกเลือด')