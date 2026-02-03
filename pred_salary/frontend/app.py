import streamlit as st
import requests 

st.title("💼 Salary Predictor App")

st.write("Enter your years of experience:")
exp = st.number_input("Experience (years)", min_value=0.0, step=0.5,max_value=20.0) 

if st.button("Predict Salary"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"exp": exp},
        headers={"Content-Type": "application/json"}
    )  

if response.status_code == 200:
    result = response.json()
    st.success(f"Predicted Salary: ₹ {result['predicted_salary']}")

else:
    st.error("Error connecting to API")