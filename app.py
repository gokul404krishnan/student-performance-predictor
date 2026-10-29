import streamlit as st

st.title("🎓 Student Performance Predictor")
st.write("Enter the student details below")

attendance = st.number_input(
    "Attendance (%)", min_value=0, max_value=100
)

study_hours = st.number_input(
    "Study Hours per Day", min_value=0.0, max_value=24.0
)

assignment = st.number_input(
    "Assignment Mark", min_value=0, max_value=100
)

internal = st.number_input(
    "Internal Mark", min_value=0, max_value=100
)

if st.button("Predict Performance"):
    score = (attendance + assignment + internal) / 3

    if score >= 85 and study_hours >= 3:
        result = "Excellent 🌟"
    elif score >= 70:
        result = "Good 👍"
    elif score >= 50:
        result = "Average 📚"
    else:
        result = "Needs Improvement"

    st.success("Predicted Performance: " + result)
