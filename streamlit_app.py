import streamlit as st

# Page setup
st.set_page_config(page_title="AI Clinical Decision Support", layout="wide")

# Title
st.title("🫀 AI Clinical Decision Support System")
st.caption("Cardiac Triage, Test Recommendation & Preliminary Risk Assessment")

st.markdown("---")

# Input Section
st.header("📥 Patient Clinical Data")

col1, col2 = st.columns(2)

with col1:
    hr = st.number_input("Heart Rate (bpm)", min_value=40, max_value=180, value=75)
    bp = st.number_input("Blood Pressure (mmHg)", min_value=80, max_value=200, value=120)

with col2:
    symptom = st.selectbox(
        "Primary Symptom",
        ["None", "Chest Pain", "Fatigue", "Breathlessness"]
    )
    stress = st.selectbox("Stress Level", ["Low", "Moderate", "High"])

# Image upload
st.header("🖼️ Echocardiogram Upload (Optional)")
image = st.file_uploader("Upload ultrasound image")

st.markdown("---")

# Analyze Button
if st.button("🔍 Analyze Patient"):

    # Decision Logic
    if symptom == "Chest Pain" or hr > 110:
        result = "Possible Cardiac Abnormality"
        urgency = "🔴 Emergency"
        tests = ["ECG", "Troponin Test", "Echocardiogram"]
        advice = "Avoid exertion. Seek immediate medical care."
        risk_value = 90

    elif symptom == "Breathlessness":
        result = "Moderate Risk"
        urgency = "🟡 Needs Evaluation"
        tests = ["Chest X-ray", "Pulse Oximetry"]
        advice = "Rest and monitor breathing. Visit doctor soon."
        risk_value = 60

    elif symptom == "Fatigue":
        result = "Mild Risk"
        urgency = "🟡 Moderate"
        tests = ["Hemoglobin Test", "Thyroid Profile"]
        advice = "Maintain hydration and proper nutrition."
        risk_value = 50

    else:
        result = "No Immediate Risk"
        urgency = "🟢 Low"
        tests = ["Routine Checkup"]
        advice = "Maintain a healthy lifestyle."
        risk_value = 30

    # Output Section
    st.header("🧠 Clinical Summary")

    col3, col4 = st.columns(2)

    with col3:
        st.success(f"Finding: {result}")
        st.warning(f"Urgency Level: {urgency}")

    with col4:
        st.subheader("📊 Risk Indicator")
        st.progress(risk_value)

    # Image analysis (prototype)
    if image:
        st.info("🧠 Image Analysis: No critical abnormality detected (prototype model)")

    # Recommended Tests
    st.subheader("🧪 Recommended Diagnostic Tests")
    for t in tests:
        st.write("•", t)

    # Advice
    st.subheader("🏠 Immediate Care Guidance")
    st.info(advice)

    # Patient Report
    st.subheader("📄 Generated Patient Report")

    st.markdown(f"""
    **Heart Rate:** {hr} bpm  
    **Blood Pressure:** {bp} mmHg  
    **Symptom:** {symptom}  
    **Stress Level:** {stress}  

    **Assessment:** {result}  
    **Urgency:** {urgency}  

    **Recommended Tests:** {", ".join(tests)}  

    **Advice:** {advice}  
    """)

    # Confidence
    st.caption("Model Confidence: 82% (Prototype Simulation)")

    st.markdown("---")
    st.warning("⚠️ This is a prototype clinical decision support system and not a medical diagnosis tool.")
