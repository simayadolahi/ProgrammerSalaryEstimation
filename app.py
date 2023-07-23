import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load('pipeline.joblib')
st.title('Salary Prediction in 2022')
st.write("""### We need some information to predict the salary""")

countries = ('United States of America', 'Other', 'Germany', 'United Kingdom of Great Britain and Northern Ireland',
            'India','Canada','France', 'Brazil', 'Spain', 'Poland','Netherlands','Australia', 'Italy','Sweden','Russian Federation',
            'Switzerland', 'Turkey', 'Austria', 'Israel' ,'Czech Republic', 'Belgium','Portugal','Denmark ','Mexico',
            'Norway','Romania', 'Greece', 'Pakistan', 'New Zealand', 'Finland','Argentina','South Africa','Iran, Islamic Republic of...',
             'Ukraine', 'Hungary', 'Bangladesh', 'Ireland','Japan','Colombia')

education = (
    "Less than a Bachelors",
    "Bachelor’s degree",
    "Master’s degree",
    "Post grad"
)
gender =(
    'Man',
    'Woman',
    'other'
)
remotework = ('Fully remote',
              'Full in-person',
              'Hybrid (some remote, some in-person)')

age =('Under 18 years old',
      '18-24 years old',
    '25-34 years old',
    '35-44 years old',
    '45-54 years old',
    'older than 55')

country = st.selectbox("Country", countries)
education = st.selectbox("Education Level", education)
expericence = st.slider("Years of Experience", 0, 50, 3)
age = st.selectbox("age", age)
gender = st.selectbox("gender", gender)
remotework = st.selectbox("remotework", remotework)



columns = ['Country', 'EdLevel', 'YearsCodePro', 'Age', 'Gender','RemoteWork']


def predict():
    # Combine all the user inputs into a list
    row = [countries,education,expericence, age,gender,remotework]

    # Create a DataFrame with the 'columns' list
    df = pd.DataFrame([row], columns=columns)

    salary = model.predict(df)
    st.write(f"The estimated salary is ${salary[0]:.2f}")

if st.button('Predict'):
    predict() 