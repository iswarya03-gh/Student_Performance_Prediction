import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models.joblib")


st.title(" Student Grade Prediction")

st.subheader(" Enter Student Details")


age = st.number_input("Age", 10, 25)
study_time = st.slider("Study Time Weekly", 0.0, 50.0)
absences = st.number_input("Absences", 0, 100)
sports = st.number_input("Sports", 0, 1)

Input_data = pd.DataFrame({
    'Age': [age],
    'StudyTimeWeekly': [study_time],
    'Absences': [absences],
    'Sports': [sports]
})

st.subheader(" Input Data")
st.write(Input_data)

if st.button("Predict"):
    prediction = model.predict(Input_data)
    if prediction < 2 :
        st.success(f' Predicted Grade Class: {prediction[0]}')
        st.balloons()
    else:
        st.warning(f'Predicted Grade Class: {prediction[0]}')

user_data=pd.DataFrame({'Feature':['Age','StudyTimeWeekly','Absences','Sports'],'Values':[age,study_time,absences,sports]})
st.subheader('Input Feature Comparison')
st.bar_chart(user_data.set_index('Feature'))

    
# st.info(f' Predicted Grade Class: {prediction[0]} ')
# st.warning(f' Predicted Grade Class: {prediction[0]} ')