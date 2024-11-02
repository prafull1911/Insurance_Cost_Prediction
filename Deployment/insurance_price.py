import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle

# Set up custom background
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo&family=Poppins:wght@400;700&display=swap');

    .main {{
        background-image: url("insurance.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        font-family: 'Poppins', sans-serif;
        color: #333333;
    }}

    .sidebar .sidebar-content {{
        background-color: rgba(255, 255, 255, 0.8);
    }}
    
    .stButton>button {{
        background-color: #4CAF50;
        color: white;
        padding: 8px 20px;
        border: none;
        cursor: pointer;
        font-weight: bold;
    }}

    .stButton>button:hover {{
        background-color: #515152;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Insurance Cost Prediction App")

st.markdown("""
    Welcome to the Insurance Cost Prediction app! 
    Please enter the required features on the left sidebar for your premium price prediction.
""")
# Rest of your code
st.markdown("## A Glimpse of Insurance Cost Prediction Data")

price_df = pd.read_csv("D:\Portfolio_Project\insurance.csv")
st.dataframe(price_df.head())

# Sidebar input options
st.sidebar.header("Enter the Features for Prediction")
age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=30, step=1)
diabetes = st.sidebar.selectbox("Diabetes", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
blood_pressure_problems = st.sidebar.selectbox("Blood Pressure Problems", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
any_transplants = st.sidebar.selectbox("Any Transplants", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
any_chronic_diseases = st.sidebar.selectbox("Any Chronic Diseases", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
height = st.sidebar.number_input("Height (in cm)", min_value=50, max_value=250, value=170)
weight = st.sidebar.number_input("Weight (in kg)", min_value=10, max_value=200, value=70)
known_allergies = st.sidebar.selectbox("Known Allergies", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
history_of_cancer_in_family = st.sidebar.selectbox("History of Cancer in Family", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
number_of_major_surgeries = st.sidebar.selectbox("Number of Major Surgeries", options=[0, 1, 2, 3])

# Calculate BMI
bmi = round(weight * 10000 / (height ** 2), 2)
st.sidebar.write(f"Calculated BMI: {bmi}")

input_data = np.array([[age, diabetes, blood_pressure_problems, any_transplants, any_chronic_diseases,
                        known_allergies, history_of_cancer_in_family, number_of_major_surgeries, bmi]])

# Load the scaler and scale the data
scaler = joblib.load("robust_scaler.pkl")
input_data_scaled = scaler.transform(input_data)

# Load the model and make a prediction
with open("best_gbdt_regressor.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Predict Premium Price
if st.sidebar.button("Predict Premium Price"):
    prediction = model.predict(input_data_scaled)
    st.write(f"### Predicted Premium Price: {prediction[0]:.2f} Rs.")
