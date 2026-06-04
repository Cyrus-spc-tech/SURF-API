import streamlit as st 
import requests 
API_URL = "http://127.0.0.1:8000/predict"


st.title("Insurance Premium Category Predict")

st.markdown("Enter your detail below ")

age = st.number_input("Age", min_value=1, max_value=119, value=26)
weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=3.0, value=1.75)
income = st.number_input("Income", min_value=0.0, value=50000.0)
smoker = st.checkbox("Smoker")
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

# Submit button
if st.button("Predict"):
    # Prepare payload
    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "income": income,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }
    
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['prediction value ']}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")