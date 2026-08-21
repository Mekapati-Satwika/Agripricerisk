import streamlit as st
import requests

st.title("🌾 Agri Price Risk Early Warning System")

if st.button("Get Real-time Prediction"):
    res = requests.get("http://127.0.0.1:8000/predict").json()
    st.json(res)
