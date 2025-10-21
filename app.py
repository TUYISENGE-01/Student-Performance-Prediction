# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# app.py
import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# App title
st.title("🎓 Student Performance Prediction App")
st.write("This app predicts whether a student will **Pass** or **Fail** based on demographic and performance data.")

# Input fields
st.header("Enter Student Details")

gender = st.selectbox("Gender", ["Male", "Female"])
race = st.selectbox("Race/Ethnicity", ["Group A", "Group B", "Group C", "Group D", "Group E"])
parent_edu = st.selectbox("Parental Level of Education", [
    "High School", "Some College", "Associate's Degree", "Bachelor's Degree", "Master's Degree"])
lunch = st.selectbox("Lunch Type", ["Standard", "Free/Reduced"])
test_prep = st.selectbox("Test Preparation Course", ["None", "Completed"])

math_score = st.number_input("Math Score", min_value=0, max_value=100, value=50)
reading_score = st.number_input("Reading Score", min_value=0, max_value=100, value=50)
writing_score = st.number_input("Writing Score", min_value=0, max_value=100, value=50)

# Convert categorical values to numeric (based on label encoding used in training)
def encode_input(gender, race, parent_edu, lunch, test_prep):
    gender_dict = {"female": 0, "male": 1}
    race_dict = {"group a": 0, "group b": 1, "group c": 2, "group d": 3, "group e": 4}
    parent_dict = {"high school": 0, "some college": 1, "associate's degree": 2,
                   "bachelor's degree": 3, "master's degree": 4}
    lunch_dict = {"free/reduced": 0, "standard": 1}
    prep_dict = {"none": 0, "completed": 1}

    # Normalize all inputs to lowercase to avoid KeyError
    return [
        gender_dict[gender.strip().lower()],
        race_dict[race.strip().lower()],
        parent_dict[parent_edu.strip().lower()],
        lunch_dict[lunch.strip().lower()],
        prep_dict[test_prep.strip().lower()],
        math_score, reading_score, writing_score
    ]

# Predict button
if st.button("Predict Result"):
    features = np.array(encode_input(gender, race, parent_edu, lunch, test_prep)).reshape(1, -1)
    prediction = model.predict(features)
    result = "✅ PASS" if prediction[0] == 1 else "❌ FAIL"

    st.subheader("Prediction Result:")
    st.success(f"The student will get: {result}")


