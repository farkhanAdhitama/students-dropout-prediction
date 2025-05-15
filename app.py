import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model, scaler, dan label encoder
model = joblib.load("model/random_forest_model.pkl")
scaler = joblib.load("model/scaler.pkl")

# Daftar fitur yang digunakan
selected_features = [
    "Curricular_units_2nd_sem_approved",
    "Curricular_units_2nd_sem_grade",
    "Curricular_units_1st_sem_approved",
    "Curricular_units_1st_sem_grade",
    "Tuition_fees_up_to_date",
    "Scholarship_holder",
    "Age_at_enrollment",
    "Debtor",
    "Admission_grade",
    "Application_mode",
    "Displaced",
    "Previous_qualification_grade",
]

st.title("Prediksi Status Siswa 🏫")

st.write("Masukkan data siswa untuk memprediksi status akademik:")


# ==================================================================================

# Bagi input menjadi dua kolom
col1, col2 = st.columns(2)
input_data = {}

# Input kolom kiri
with col1:
    # Curricular_units_2nd_sem_approved
    input_data["Curricular_units_2nd_sem_approved"] = st.number_input(
        "Curricular_units_2nd_sem_approved", min_value=0, step=1
    )

    # Curricular_units_2nd_sem_grade
    input_data["Curricular_units_2nd_sem_grade"] = st.number_input(
        "Curricular_units_2nd_sem_grade", min_value=0, step=1
    )

    # Tuition_fees_up_to_date
    input_data["Tuition_fees_up_to_date"] = st.selectbox(
        "Tuition_fees_up_to_date", ["No", "Yes"]
    )
    input_data["Tuition_fees_up_to_date"] = (
        1 if input_data["Tuition_fees_up_to_date"] == "Yes" else 0
    )

    # Age_at_enrollment
    input_data["Age_at_enrollment"] = st.number_input(
        "Age_at_enrollment", min_value=0, max_value=100, step=1
    )

    # Admission_grade
    input_data["Admission_grade"] = st.number_input(
        "Admission_grade (between 0 and 200)", min_value=0, max_value=200, step=1
    )

    # Displaced
    input_data["Displaced"] = st.selectbox("Displaced", ["No", "Yes"])
    input_data["Displaced"] = 1 if input_data["Displaced"] == "Yes" else 0


# Input kolom kanan
with col2:
    # Curricular_units_1st_sem_approved
    input_data["Curricular_units_1st_sem_approved"] = st.number_input(
        "Curricular_units_1st_sem_approved", min_value=0, step=1
    )

    # Curricular_units_1st_sem_grade
    input_data["Curricular_units_1st_sem_grade"] = st.number_input(
        "Curricular_units_1st_sem_grade", min_value=0, step=1
    )

    # Scholarship_holder
    input_data["Scholarship_holder"] = st.selectbox("Scholarship_holder", ["No", "Yes"])
    input_data["Scholarship_holder"] = (
        1 if input_data["Scholarship_holder"] == "Yes" else 0
    )

    # Debtor
    input_data["Debtor"] = st.selectbox("Debtor", ["No", "Yes"])
    input_data["Debtor"] = 1 if input_data["Debtor"] == "Yes" else 0

    # Application mode
    application_mode_map = {
        1: "1st phase - general contingent",
        2: "Ordinance No. 612/93",
        5: "1st phase - special contingent (Azores Island)",
        7: "Holders of other higher courses",
        10: "Ordinance No. 854-B/99",
        15: "International student (bachelor)",
        16: "1st phase - special contingent (Madeira Island)",
        17: "2nd phase - general contingent",
        18: "3rd phase - general contingent",
        26: "Ordinance No. 533-A/99, item b2) (Different Plan)",
        27: "Ordinance No. 533-A/99, item b3 (Other Institution)",
        39: "Over 23 years old",
        42: "Transfer",
        43: "Change of course",
        44: "Technological specialization diploma holders",
        51: "Change of institution/course",
        53: "Short cycle diploma holders",
        57: "Change of institution/course (International)",
    }

    # Create the selectbox with labels
    application_mode_label = st.selectbox(
        "Application mode", list(application_mode_map.values())
    )

    # Map label ke numerik asli
    input_data["Application_mode"] = next(
        key
        for key, value in application_mode_map.items()
        if value == application_mode_label
    )

    input_data["Previous_qualification_grade"] = st.number_input(
        "Previous_qualification_grade (between 0 and 200)",
        min_value=0,
        max_value=200,
        step=1,
    )

# ==================================================================================
# Prediksi ketika tombol ditekan
if st.button("🔍 Prediksi Status"):
    df_input = pd.DataFrame([input_data])
    df_input = df_input[selected_features]  # Reorder columns to match training features
    # Scaling input
    X_scaled = scaler.transform(df_input)
    # Lakukan prediksi
    prediction = model.predict(X_scaled)[0]
    prediction_proba = model.predict_proba(X_scaled)[0]

    st.success(f"📌 Prediksi Status: **{prediction}**")
    st.write("Probabilitas Kelas:")
    proba_df = pd.DataFrame(
        [prediction_proba],
        columns=model.classes_,
    )
    st.dataframe(
        proba_df.T.rename(columns={0: "Probability"}), use_container_width=True
    )
