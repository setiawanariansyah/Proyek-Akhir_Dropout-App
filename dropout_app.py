import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import *
from prediction import prediction


col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header("Dropout App (Prototype) :sparkles")

data = pd.DataFrame()

col1, col2, col3 = st.columns(3)

with col1:
    KatMarital_status = st.selectbox(label='KatMarital_status', options=encoder_KatMarital_status.classes_, index=1)
    data["KatMarital_status"] = [KatMarital_status]

with col2:
    KatApplication_mode = st.selectbox(label='KatApplication_mode', options=encoder_KatApplication_mode.classes_, index=1)
    data["KatApplication_mode"] = [KatApplication_mode]

with col3:
    KatCourse = st.selectbox(label='KatCourse', options=encoder_KatCourse.classes_, index=5)
    data["KatCourse"] = KatCourse

col1, col2, col3 = st.columns(3)

with col1:
    Kat_PreviousQualification = st.selectbox(label='Kat_PreviousQualification', options=encoder_Kat_PreviousQualification.classes_, index=1)
    data["Kat_PreviousQualification"] = Kat_PreviousQualification

with col2:
    KatNacionality = st.selectbox(label='KatNacionality', options=encoder_KatNacionality.classes_, index=1)
    data["KatNacionality"] = KatNacionality

with col3:
    Kat_MotherQualification = st.selectbox(label='Kat_MotherQualification', options=encoder_Kat_MotherQualification.classes_, index=3)
    data["Kat_MotherQualification"] = Kat_MotherQualification

col1, col2, col3 = st.columns(3)

with col1:
    Kat_FatherQualification = st.selectbox(label='Kat_FatherQualification', options=encoder_Kat_FatherQualification.classes_, index=3)
    data["Kat_FatherQualification"] = Kat_FatherQualification

with col2:
    Kat_FatherOccupation = st.selectbox(label='Kat_FatherOccupation', options=encoder_Kat_FatherOccupation.classes_, index=1)
    data["Kat_FatherOccupation"] = Kat_FatherOccupation

with col3:
    Kat_MotherOccupation = st.selectbox(label='Kat_MotherOccupation', options=encoder_Kat_MotherOccupation.classes_, index=1)
    data["Kat_MotherOccupation"] = Kat_MotherOccupation

col1, col2, col3 = st.columns(3)

with col1:
    Application_order = st.selectbox(label='Application_order', options=encoder_Application_order.classes_, index=1)
    data["Application_order"] = Application_order

with col2:
    Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.classes_, index=1)
    data["Daytime_evening_attendance"] = Daytime_evening_attendance

with col3:
    Displaced = st.selectbox(label='Displaced', options=encoder_Displaced.classes_, index=1)
    data["Displaced"] = Displaced

col1, col2, col3 = st.columns(3)

with col1:
    Educational_special_needs = st.selectbox(label='Educational_special_needs', options=encoder_Educational_special_needs.classes_, index=1)
    data["Educational_special_needs"] = Educational_special_needs

with col2:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition_fees_up_to_date', options=encoder_Tuition_fees_up_to_date.classes_, index=1)
    data["Tuition_fees_up_to_date"] = Tuition_fees_up_to_date

with col3:
    Debtor = st.selectbox(label='Debtor', options=encoder_Debtor.classes_, index=1)
    data["Debtor"] = Debtor

col1, col2, col3 = st.columns(3)

with col1:
    Gender = st.selectbox(label='Gender', options=encoder_Gender.classes_, index=1)
    data["Gender"] = Gender

with col2:
    Scholarship_holder = st.selectbox(label='Scholarship_holder', options=encoder_Scholarship_holder.classes_, index=1)
    data["Scholarship_holder"] = Scholarship_holder

with col3:
    International = st.selectbox(label='International', options=encoder_International.classes_, index=1)
    data["International"] = International

col1, col2, col3, col4 = st.columns(4)

with col1:
    Previous_qualification_grade = float(st.number_input(label='Previous_qualification_grade', value=11.27))
    data["Previous_qualification_grade"] = Previous_qualification_grade

with col2:
    Admission_grade = float(st.number_input(label='Admission_grade', value=11.27))
    data["Admission_grade"] = Admission_grade

with col3:
    Age_at_enrollment = int(st.number_input(label='Age_at_enrollment', value=21))
    data["Age_at_enrollment"] = Age_at_enrollment

with col4:
    Curricular_units_1st_sem_credited = int(st.number_input(label='Curricular_units_1st_sem_credited', value=10))
    data["Curricular_units_1st_sem_credited"] = Curricular_units_1st_sem_credited

col1, col2, col3 = st.columns(3)

with col1:
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='Curricular_units_1st_sem_enrolled', value=12))
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled

with col2:
    Curricular_units_1st_sem_evaluations = int(st.number_input(label='Curricular_units_1st_sem_evaluations', value=15))
    data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations

with col3:
    Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular_units_1st_sem_approved', value=21))
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved

col1, col2, col3, col4 = st.columns(4)

with col1:
    Curricular_units_1st_sem_grade = int(st.number_input(label='Curricular_units_1st_sem_grade', value=12))
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade

with col2:
    Curricular_units_1st_sem_without_evaluations = int(st.number_input(label='Curricular_units_1st_sem_without_evaluations', value=15))
    data["Curricular_units_1st_sem_without_evaluations"] = Curricular_units_1st_sem_without_evaluations

with col3:
    Curricular_units_2nd_sem_credited = int(st.number_input(label='Curricular_units_2nd_sem_credited', value=21))
    data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited

with col4:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Curricular_units_2nd_sem_enrolled', value=21))
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled

col1, col2, col3, col4 = st.columns(4)

with col1:
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_evaluations', value=12))
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations

with col2:
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Curricular_units_2nd_sem_approved', value=15))
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved

with col3:
    Curricular_units_2nd_sem_grade = int(st.number_input(label='Curricular_units_2nd_sem_grade', value=21))
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade

with col4:
    Curricular_units_2nd_sem_without_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_without_evaluations', value=21))
    data["Curricular_units_2nd_sem_without_evaluations"] = Curricular_units_2nd_sem_without_evaluations

with st.expander("View the Raw Data"):
    st.dataframe(data=data)

if st.button("Predict"):
    new_data = data_preprocessing(data=data)
    with st.expander("View the preprocessed data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Credit Scoring: {}".format(prediction(new_data)))