import os
import streamlit as st
import pandas as pd
import pickle

# Load Model
model_path = os.path.join(os.path.dirname(__file__), "TeenDepressionAnalysisModel.pkl")
try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Model file not found: {model_path}")
    st.stop()
except ModuleNotFoundError as e:
    st.error("A required Python module is missing for the model. Please install dependencies from requirements.txt.")
    st.error(str(e))
    st.stop()
except Exception as e:
    st.error("Failed to load the model.")
    st.error(str(e))
    st.stop()

st.title("Teen Depression Prediction") 

# Input Fields
age = st.number_input("Age" , min_value=13 , max_value=19 , value=16)

gender = st.selectbox(
    "Gender",
    ["Male" , "Female"]
)

daily_social_media_hours = st.slider(
    "Daily Social Media Hours",
    0.0,15.0,5.0
)

# 0.0 = min value , 15.0 max value , 5.0 = default value

platform_usage = st.selectbox(
    "Platform Usage",
    ["Instagram", "TikTok" , "Both"]
)

# first value serves as a default value (eg = instagram)

sleep_hours = st.slider(
    "Sleep Hours",
    0.0,12.0,7.0
)

screen_time_before_sleep = st.slider(
    "Sleep Hours",
    0.0 , 5.0 , 1.0
)

academic_performance = st.slider(
    "Academic Performance",
    1,10,5
)

physical_activity = st.slider(
    "Physical Acticity",
    1,10,5
)

social_interaction_level = st.slider(
    "Social Interaction Level",
    1,10,5
)

stress_level = st.slider(
    "Stress Level",
    1,10,5
)

anxiety_level = st.slider(
    "Anxiety Level",
    1,10,5
)

addiction_level = st.slider(
    "Addiction Level",
    1,10,5
)

# Simple Encoding

gender = 1 if gender == "Male" else 0

platform_dict = {
    "Instagram" : 0,
    "TikTok" : 1,
    "Both" : 2
}

platform_usage = platform_dict[platform_usage]

# Prediction

if st.button("Predict"):

    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "daily_social_media_hours": [daily_social_media_hours],
        "platform_usage": [platform_usage],
        "sleep_hours": [sleep_hours],
        "screen_time_before_sleep": [screen_time_before_sleep],
        "academic_performance": [academic_performance],
        "physical_activity": [physical_activity],
        "social_interaction_level": [social_interaction_level],
        "stress_level": [stress_level],
        "anxiety_level": [anxiety_level],
        "addiction_level": [addiction_level]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("High Risk of Depression")
    else:
        st.success("Low Risk of Depression")