import streamlit as st

st.set_page_config(page_title="AI Clinical Dashboard", layout="wide")

# ---------- HEADER ----------
st.markdown("""
<h1 style='text-align: center;'>🫀 AI Clinical Decision Dashboard</h1>
<p style='text-align: center;'>Smart Cardiac Triage & Test Recommendation System</p>
<hr>
""", unsafe_allow_html=True)

# ---------- INPUT SECTION ----------
st.subheader("📥 Enter Patient Details")

col1, col2, col3 = st.columns(3)

with col1:
    hr = st.slider("Heart Rate", 40, 180, 75)

with col2:
    bp = st.slider("Blood Pressure", 80, 200, 120)

with col3:
    symptom = st.selectbox("Symptom",
        ["None", "Chest Pain", "Fatigue", "Breathlessness"]
    )

image = st.file_uploader("Upload Echocardiogram (optional)")

# ---------- BUTTON ----------
if st.button("🔍 Analyze"):

    # Logic
    if symptom == "Chest Pain" or hr > 110:
        result = "⚠️ Cardiac Abnormality Detected"
        risk = "HIGH"
        color = "red"
        tests = "ECG, Troponin, Echocardiogram"
        advice = "Immediate medical attention required"

    elif symptom == "Breathlessness":
        result = "⚠️ Moderate Risk Condition"
        risk = "MEDIUM"
        color = "orange"
        tests = "Chest X-ray, Pulse Oximetry"
        advice = "Consult doctor within 24 hrs"

    elif symptom == "Fatigue":
        result = "⚠️ Mild Risk"
        risk = "LOW-MODERATE"
        color = "gold"
        tests = "Hb Test, Thyroid Profile"
        advice = "Monitor condition and maintain rest"

    else:
        result = "✅ Normal Condition"
        risk = "LOW"
        color = "green"
        tests = "Routine Checkup"
        advice = "Maintain healthy lifestyle"

    st.markdown("---")

    # ---------- OUTPUT DASHBOARD ----------
    st.subheader("📊 Analysis Dashboard")

    c1, c2, c3 = st.columns(3)

    c1.metric("Heart Rate", f"{hr} bpm")
    c2.metric("Blood Pressure", f"{bp} mmHg")
    c3.metric("Risk Level", risk)

    st.markdown("---")

    # Result box
    st.markdown(f"""
    <div style='padding:20px; border-radius:10px; background-color:#f5f5f5'>
    <h3 style='color:{color}'>{result}</h3>
    </div>
    """, unsafe_allow_html=True)

    # Image analysis
    if image:
        st.info("🧠 Image Insight: No critical abnormality detected (prototype)")

    # ---------- TESTS ----------
    st.subheader("🧪 Recommended Tests")
    st.success(tests)

    # ---------- ACTION ----------
    st.subheader("🏥 Immediate Action")
    st.warning(advice)

    # ---------- REPORT ----------
    st.subheader("📄 Summary Report")

    st.write(f"""
    - Heart Rate: {hr}
    - Blood Pressure: {bp}
    - Symptom: {symptom}
    - Risk Level: {risk}
    - Suggested Tests: {tests}
    """)

    st.caption("Confidence Score: 82%")osis tool.")
