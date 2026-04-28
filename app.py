import streamlit as st

st.title("🫀 AI Cardiac Triage + Test Recommendation System")

hr = st.number_input("Heart Rate")
bp = st.number_input("Blood Pressure")

symptom = st.selectbox(
    "Symptom",
    ["None", "Chest Pain", "Fatigue", "Breathlessness"]
)

if st.button("Analyze"):

    if symptom == "Chest Pain" or hr > 110:
        result = "Possible Cardiac Abnormality"
        urgency = "🔴 Emergency"
        tests = ["ECG", "Troponin Test", "Echocardiogram"]
        advice = "Avoid exertion. Seek immediate medical care."

    elif symptom == "Breathlessness":
        result = "Moderate Risk"
        urgency = "🟡 Needs Evaluation"
        tests = ["Chest X-ray", "Pulse Oximetry"]
        advice = "Rest and monitor breathing. Visit doctor soon."

    elif symptom == "Fatigue":
        result = "Mild Risk"
        urgency = "🟡 Moderate"
        tests = ["Hemoglobin Test", "Thyroid Profile"]
        advice = "Maintain hydration and proper nutrition."

    else:
        result = "No Immediate Risk"
        urgency = "🟢 Low"
        tests = ["Routine Checkup"]
        advice = "Maintain a healthy lifestyle."

    st.write("Finding:", result)
    st.write("Urgency:", urgency)

    st.write("Recommended Tests:")
    for t in tests:
        st.write("-", t)

    st.write("Advice:", advice)
