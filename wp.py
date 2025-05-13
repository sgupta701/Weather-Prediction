import streamlit as st
import pickle

st.title("Weather prediction app")
pn=st.number_input("Enter precipitation")
maxt=st.number_input("Enter maximum temperature")
mint=st.number_input("Enter minumun temperature")
ws=st.number_input("Enter wind speed")

button=st.button("Predict")

if button:
    lr=pickle.load(open("wp.pkl","rb"))
    res=lr.predict([[pn,maxt,mint,ws]])[0]
    st.markdown(f"Today's weather situation: {res}")