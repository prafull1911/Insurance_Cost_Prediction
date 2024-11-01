import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.markdown("""
            ## A Glimpse of Insurance Cost Prediction Data
            """)

price_df = pd.read_csv("D:\Portfolio_Project\insurance.csv")

st.dataframe(price_df.head())

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

with open("best_gbdt_regressor.pkl", "rb") as model_file:
    model = pickle.load(model_file)