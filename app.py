import streamlit as st
import joblib

st.set_page_config(page_title="Kidney Disease Prediction", layout="centered")

st.markdown(
    """
    <style>
    .main {background-color: #f0f2f6;}
    .stButton>button {background-color: #4CAF50; color: white;}
    .result {font-size: 1.5em; font-weight: bold; color: #4CAF50;}
    input[type="text"] {background-color: #fff !important; color: #222 !important;}
    input[type="text"]:focus {
    border: 2px solid #4CAF50 !important;
    background-color: #eaffea !important;
}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🩺 Kidney Disease Prediction")
st.write("Enter the main details to check your kidney health:")

model = joblib.load("kidney_model.pkl")

feature_names = [
    ("age", "Age"),
    ("bp", "Blood Pressure"),
    ("sg", "Specific Gravity"),
    ("al", "Albumin"),
    ("hemo", "Hemoglobin"),
    ("pcv", "Packed Cell Volume"),
    ("sc", "Serum Creatinine"),
    ("bgr", "Blood Glucose Random")
]

placeholders = {
    "age": "Enter age (15-90)",
    "bp": "Enter BP (50-180)",
    "sg": "Enter SG (1.005-1.025)",
    "al": "Enter Albumin (1-5)",
    "hemo": "Enter Hemoglobin (3-17)",
    "pcv": "Enter PCV (20-54)",
    "sc": "Enter Serum Creatinine (0.5-5)",
    "bgr": "Enter BGR (70-500)"
}

ranges = {
    "age": (15, 90),
    "bp": (50, 180),
    "sg": (1.005, 1.025),
    "al": (1, 5),
    "hemo": (3, 17),
    "pcv": (20, 54),
    "sc": (0.5, 5),
    "bgr": (70, 500)
}

user_input = []
cols = st.columns(2)
for i, (feature, full_form) in enumerate(feature_names):
    with cols[i % 2]:
        value = st.text_input(
            f"{feature.upper()} ({full_form})",
            placeholder=placeholders[feature],
            label_visibility="visible"
        )
        min_val, max_val = ranges[feature]
        st.caption(f"Valid range: {min_val} - {max_val}")
        user_input.append(value)

if st.button("Predict"):
    try:
        if "" in user_input:
            st.error("Please fill all fields.")
        else:
            features = []
            for idx, (feature, _) in enumerate(feature_names):
                val = float(user_input[idx])
                min_val, max_val = ranges[feature]
                if not (min_val <= val <= max_val):
                    st.error(f"{feature.upper()} should be between {min_val} and {max_val}.")
                    st.stop()
                features.append(val)
            features_full = features + [0]*(24-len(features))
            prediction = model.predict([features_full])[0]
            # Prediction result
            if prediction == 1:
                st.markdown("<div class='result'>🛑 Kidney Disease Detected</div>", unsafe_allow_html=True)
                st.markdown("<b>Status:</b> <span style='color:red'>Kidney NOT SAFE</span>", unsafe_allow_html=True)
                st.markdown("<b>Advice:</b> Please consult a healthcare professional for further advice and diagnosis. Early detection and treatment can help manage the condition effectively.", unsafe_allow_html=True)
                st.markdown("<b>Final Remark:</b> <span style='color:red; font-size:1.2em;'>Your kidney is NOT SAFE. Immediate medical attention is recommended.</span>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='result'>✅ No Kidney Disease</div>", unsafe_allow_html=True)
                st.markdown("<b>Status:</b> <span style='color:green'>Kidney SAFE</span>", unsafe_allow_html=True)
                st.markdown("<b>Advice:</b> Your results are within the normal range. Keep maintaining a healthy lifestyle, drink plenty of water, and have regular checkups to keep your kidneys healthy.", unsafe_allow_html=True)
                st.markdown("<b>Final Remark:</b> <span style='color:green; font-size:1.2em;'>Your kidney is SAFE. Keep up your healthy habits!</span>", unsafe_allow_html=True)
            st.markdown("---")
            st.markdown("#### SG (Specific Gravity) Value Meaning")
            st.markdown(
                """
                <table style='width:100%; font-size:1em; background:#f9f9f9; border-radius:8px'>
                    <tr><th>SG Value</th><th>Meaning</th></tr>
                    <tr><td>1.005</td><td>Very dilute urine</td></tr>
                    <tr><td>1.010</td><td>Slightly dilute</td></tr>
                    <tr><td>1.015</td><td>Normal</td></tr>
                    <tr><td>1.020–1.025</td><td>Slightly concentrated</td></tr>
                    <tr><td>1.030</td><td>Very concentrated</td></tr>
                </table>
                """,
                unsafe_allow_html=True
            )
    except Exception as e:
        st.error("Please enter valid numbers for all fields.")
