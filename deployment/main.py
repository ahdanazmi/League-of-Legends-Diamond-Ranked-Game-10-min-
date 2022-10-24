import streamlit as st
import EDA
import predict

navigation = st.sidebar.selectbox('Choose Page : ', ('Analysis','Winning Prediction'))

if navigation=='Analysis':
    EDA.run()
else:
    predict.run()