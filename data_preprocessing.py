import joblib
import numpy as np
import pandas as pd

# Load all the data preprocessing objects
encoder_KatMarital_status = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_KatMarital_status.joblib")
encoder_KatApplication_mode = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_KatApplication_mode.joblib")
encoder_KatCourse = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_KatCourse.joblib")
encoder_Kat_PreviousQualification = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_Kat_PreviousQualification.joblib")
encoder_KatNacionality = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_KatNacionality.joblib")
encoder_Kat_MotherQualification = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_Kat_MotherQualification.joblib")
encoder_Kat_FatherQualification = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_Kat_FatherQualification.joblib")
encoder_Kat_FatherOccupation = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_Kat_FatherOccupation.joblib")
encoder_Kat_MotherOccupation = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_Kat_MotherOccupation.joblib")
encoder_Application_order = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_Application_order.joblib")
encoder_Daytime_evening_attendance = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_Daytime_evening_attendance.joblib")
encoder_Displaced = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_Displaced.joblib")
encoder_Educational_special_needs = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_Educational_special_needs.joblib")
encoder_Debtor = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_Debtor.joblib")
encoder_Tuition_fees_up_to_date = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_Tuition_fees_up_to_date.joblib")
encoder_Gender = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_Gender.joblib")
encoder_Scholarship_holder = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_Scholarship_holder.joblib")
encoder_International = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/encoder_International.joblib")

scaler_Previous_qualification_grade = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Previous_qualification_grade.joblib")
scaler_Admission_grade = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Admission_grade.joblib")
scaler_Age_at_enrollment = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Age_at_enrollment.joblib")
scaler_Curricular_units_1st_sem_credited = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Curricular_units_1st_sem_credited.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_evaluations = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Curricular_units_1st_sem_evaluations.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_grade = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Curricular_units_1st_sem_grade.joblib")
scaler_Curricular_units_1st_sem_without_evaluations = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Curricular_units_1st_sem_without_evaluations.joblib")
scaler_Curricular_units_2nd_sem_credited = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Curricular_units_2nd_sem_credited.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_Curricular_units_2nd_sem_evaluations = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Curricular_units_2nd_sem_evaluations.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Curricular_units_2nd_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_without_evaluations = joblib.load("D:/Kuliah/NonSTIS/Programming/Python/Proyek Final/Model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib")

categorical_columns = [
    'KatMarital_status', 'KatApplication_mode', 
    'KatCourse', 'Kat_PreviousQualification', 
    'KatNacionality', 'Kat_MotherQualification', 
    'Kat_FatherQualification', 'Kat_FatherOccupation', 
    'Kat_MotherOccupation', 'Application_order', 
    'Daytime_evening_attendance', 'Displaced',
    'Educational_special_needs', 'Debtor', 
    'Tuition_fees_up_to_date', 'Gender', 
    'Scholarship_holder', 'International'
]
numerical_columns = ["Previous_qualification_grade", "Admission_grade",
                    "Age_at_enrollment", "Curricular_units_1st_sem_credited",
                     "Curricular_units_1st_sem_enrolled", "Curricular_units_1st_sem_evaluations",
                     "Curricular_units_1st_sem_approved", "Curricular_units_1st_sem_grade",
                     "Curricular_units_1st_sem_without_evaluations", "Curricular_units_2nd_sem_credited",
                     "Curricular_units_2nd_sem_enrolled", "Curricular_units_2nd_sem_evaluations",
                     "Curricular_units_2nd_sem_approved", "Curricular_units_2nd_sem_grade",
                     "Curricular_units_2nd_sem_without_evaluations"]

def data_preprocessing(data):
    """Preprocessing data

    Args:
        data (Pandas Dataframe): Dataframe that contain all the data to make prediction
    return
        Pandas Dataframe: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()

    df["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1,1))[0]
    df["Admission_grade"] = scaler_Admission_grade.transform(np.asarray(data["Admission_grade"]).reshape(-1,1)) 
    df["Age_at_enrollment"] = scaler_Age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1,1)) 
    df["Curricular_units_1st_sem_credited"] = scaler_Curricular_units_1st_sem_credited.transform(np.asarray(data["Curricular_units_1st_sem_credited"]).reshape(-1,1)) 
    df["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1,1)) 
    df["Curricular_units_1st_sem_evaluations"] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_evaluations"]).reshape(-1,1)) 
    df["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1,1)) 
    df["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1,1)) 
    df["Curricular_units_1st_sem_without_evaluations"] = scaler_Curricular_units_1st_sem_without_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_without_evaluations"]).reshape(-1,1)) 
    df["Curricular_units_2nd_sem_credited"] = scaler_Curricular_units_2nd_sem_credited.transform(np.asarray(data["Curricular_units_2nd_sem_credited"]).reshape(-1,1)) 
    df["Curricular_units_2nd_sem_enrolled"] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1,1)) 
    df["Curricular_units_2nd_sem_evaluations"] = scaler_Curricular_units_2nd_sem_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_evaluations"]).reshape(-1,1)) 
    df["Curricular_units_2nd_sem_approved"] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1,1)) 
    df["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1,1)) 
    df["Curricular_units_2nd_sem_without_evaluations"] = scaler_Curricular_units_2nd_sem_without_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_without_evaluations"]).reshape(-1,1)) 

    df["KatMarital_status"] = encoder_KatMarital_status.transform(np.asarray(data["KatMarital_status"]))[0] 
    df["KatApplication_mode"] = encoder_KatApplication_mode.transform(np.asarray(data["KatApplication_mode"])) 
    df["KatCourse"] = encoder_KatCourse.transform(np.asarray(data["KatCourse"])) 
    df["Kat_PreviousQualification"] = encoder_Kat_PreviousQualification.transform(np.asarray(data["Kat_PreviousQualification"])) 
    df["KatNacionality"] = encoder_KatNacionality.transform(np.asarray(data["KatNacionality"])) 
    df["Kat_MotherQualification"] = encoder_Kat_MotherQualification.transform(np.asarray(data["Kat_MotherQualification"])) 
    df["Kat_FatherQualification"] = encoder_Kat_FatherQualification.transform(np.asarray(data["Kat_FatherQualification"])) 
    df["Kat_FatherOccupation"] = encoder_Kat_FatherOccupation.transform(np.asarray(data["Kat_FatherOccupation"])) 
    df["Kat_MotherOccupation"] = encoder_Kat_MotherOccupation.transform(np.asarray(data["Kat_MotherOccupation"])) 
    df["Application_order"] = encoder_Application_order.transform(np.asarray(data["Application_order"])) 
    df["Daytime_evening_attendance"] = encoder_Daytime_evening_attendance.transform(np.asarray(data["Daytime_evening_attendance"])) 
    df["Displaced"] = encoder_Displaced.transform(np.asarray(data["Displaced"])) 
    df["Educational_special_needs"] = encoder_Educational_special_needs.transform(np.asarray(data["Educational_special_needs"])) 
    df["Debtor"] = encoder_Debtor.transform(np.asarray(data["Debtor"])) 
    df["Tuition_fees_up_to_date"] = encoder_Tuition_fees_up_to_date.transform(np.asarray(data["Tuition_fees_up_to_date"])) 
    df["Gender"] = encoder_Gender.transform(np.asarray(data["Gender"])) 
    df["Scholarship_holder"] = encoder_Scholarship_holder.transform(np.asarray(data["Scholarship_holder"])) 
    df["International"] = encoder_International.transform(np.asarray(data["International"])) 

    return df