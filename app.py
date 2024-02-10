
import pickle
import streamlit as st
import pandas as pd
from PIL import Image


# loading the saved models

heart_model = pickle.load(open('C:/Users/Shreyas/Desktop/Heart_Attack_Prediction/saved models/heart_predict_model.sav', 'rb'))

    
# page title
st.title('Heart Attack Prediction using ML')
    
# getting the input data from the user
col1, col2, col3 = st.columns(3)
    
    
with col1:
    age = st.number_input('Age',key='Age', min_value=0, max_value=1000, value=0, step=1)
        
with col2:
    totChol = st.number_input('Total Cholestrol',key='Total Cholestrol', min_value=0, max_value=1000, value=0, step=1)
        
with col3:
    sysBP = st.number_input('Systolic Blood Pressure',key='Systolic Blood Pressure', min_value=0, max_value=1000, value=0, step=1)
        
with col1:
    diaBP = st.number_input('Diastolic Blood Pressure',key='Diastolic Blood Pressure', min_value=0, max_value=1000, value=0, step=1)
        
with col2:
    BMI = st.number_input('Body Mass Index',key='Body Mass Index', min_value=0, max_value=1000, value=0, step=1)
        
with col3:
    heartRate = st.number_input('Heart Rate',key='Heart Rate', min_value=0, max_value=1000, value=0, step=1)
        
with col1:
    glucose = st.number_input('Glucose',key='Glucose', min_value=0, max_value=1000, value=0, step=1)

    
# code for Prediction
heart_diagnosis = ''
    
# creating a button for Prediction
    
if st.button('Heart Attack Test Result'):
    heart_prediction = heart_model.predict([[age, totChol, sysBP, diaBP, BMI, heartRate, glucose]])
        
    if (heart_prediction[0] == 1):
        st.markdown(f'<p style="background-color:#ff4b4b;text-align:center;color:#ffffff;font-size:24px;border-radius:2%;">CHECK YOUR RESULTS</p>', unsafe_allow_html=True)
        
        st.markdown(f'<p style="text-align:center;color:#ff4b4b;font-size:16px;">You are having a risk of a Heart Attack</p>', unsafe_allow_html=True)
        
        st.markdown(f'<p style="text-align:center;font-size:12px;">I am sorry to hear that having a risk of a Heart Attack. It must be challenging to manage your health condition, but please know that you are not alone, and there is help available to you. It takes a lot of courage and strength to deal with this, and I wish you all the best in your journey towards better health.</p>', unsafe_allow_html=True)


             ##################################################################################################################
        def load_data():
            return pd.DataFrame(
                {
                        "Label": ["Age", "Total Cholestrol", "Systolic BP", "Diastolic BP","Body Mass Index","Heart Rate","Glucose"],
                        "Value": [age, totChol, sysBP, diaBP, BMI, heartRate, glucose],
                }
            )    
        df = load_data()
        st.dataframe(df)
            
        img1 = Image.open("heart/Bhujangasana.png")
        img2 = Image.open("heart/Padangusthasana.png")
        img3 = Image.open("heart/Paschimottanasana.png")
        img4 = Image.open("heart/Savasana.png")
        img5 = Image.open("heart/Setu Bandhasana.png")
        img6 = Image.open("heart/Svanasana.png")
        img7 = Image.open("heart/Tadasana.png")
        img8 = Image.open("heart/Utkatasana.png")
        img9 = Image.open("heart/Uttanasana.png")
        img10 = Image.open("heart/Vrikshasana.png")


        st.subheader('Breathwork for Heart Health: Using Pranayama Techniques to Improve Cardiovascular Function')
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(img1,caption='Bhujangasana')        

        with col2:
            st.image(img2,caption='Padangusthasana')

        with col3:
            st.image(img3,caption='Paschimottanasana')

        with col1:
            st.image(img4,caption='Savasana')        

        with col2:
            st.image(img5,caption='Setu Bandhasana')

        with col3:
            st.image(img6,caption='Svanasana')

        with col1:
            st.image(img7,caption='Tadasana')        

        with col2:
            st.image(img8,caption='Utkatasana')

        with col3:
            st.image(img9,caption='Uttanasana')

        with col1:
            st.image(img10,caption='Vrikshasana')

        st.video("https://youtu.be/dAHrFEGxuS4")
        heart_diagnosis = 'The person is in danger of a heart attack.'
    else:
        heart_diagnosis = 'The person is not in danger of a heart attack.'

st.success(heart_diagnosis)

st.markdown(f'<p style="text-align:center;">Project by Avantika Marathe</p>', unsafe_allow_html=True)