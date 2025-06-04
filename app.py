#Importing Libraries
import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="IBM Employee Attrition Predictor", page_icon="🏢",layout="wide")

#import model
st.title("IBM Employee Attrition Predictor 🏢")
pipe=pickle.load(open("./models/pipe.pkl","rb"))
df=pickle.load(open("./models/df.pkl","rb"))

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # Age
    age = st.number_input("Age")

with middle_column:
    # Business Travel
    bt = st.selectbox("Business Travel", df["BusinessTravel"].unique())

with right_column:
    # Daily Rate
    dt = st.number_input("Daily Rate (Rs)")

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # Department
    dept = st.selectbox("Department",df['Department'].unique())

with middle_column:
    # Distance From Home
    dfh = st.number_input('Distance From Home (KM)')

with right_column:
    # Education
    ed = st.selectbox("Education", ['Below College','College','Bachelor','Master','Doctor'])

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # education field
    edf = st.selectbox("Education Field",df['EducationField'].unique())

with middle_column:
    # Environment Satisfaction
    es = st.number_input("Environment Satisfaction (1-5)")

with right_column:
    # Gender
    gender = st.selectbox('Gender',df['Gender'].unique())

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # Hourly Rate
    hr = st.number_input("Hourly Rate (Rs)")

with middle_column:
    # Job Envolvement
    je = st.number_input('Job Envolvement (1-5)')

with right_column:
    # Job Level
    jl = st.number_input("Job Level (1-5)")

# making 3 cols left_column, middle_column, right_column
left_column,middle_column,right_column = st.columns(3)
with left_column:
    # Job Role
    jr = st.selectbox("Job Role",df['JobRole'].unique())

with middle_column:
    # Job Satisfaction
    js = st.number_input('Job Satisfaction (1-5)')

with right_column:
    # Martial Status
    ms = st.selectbox('Martial Status',df['MaritalStatus'].unique())

left_column,middle_column,right_column=st.columns(3)
with left_column:
    # Monthly Income
    mi = st.number_input('Monthly Income (Rs)')

with middle_column:
    # Monthly Rate
    mr = st.number_input('Monthly Rate (Rs)')

with right_column:
    # Num comp worked
    nmw = st.number_input('Number of Companies Worked')

left_column,middle_column,right_column=st.columns(3)
with left_column:
    # over time
    ot=st.selectbox('Over Time',['Yes','No'])

with middle_column:
    # percent salary hike
    psh=st.number_input('Salary Hike (%)')

with right_column:
    # Perf rating
    pr=st.number_input('Performance Rating (1-5)')

left_column,middle_column,right_column=st.columns(3)
with left_column:
    # relationship satis,
    rs=st.number_input('Relationship Satisfaction (1-5)')

with middle_column:
    # stock option level
    sol=st.number_input('Stock Option Level (0-5)')

with right_column:
    # total working years
    twy=st.number_input('Total Working Years')

left_column,middle_column,right_column=st.columns(3)
with left_column:
    # training times last year
    tyl=st.number_input('Training Times Last Year')

with middle_column:
    # work life bal
    wlb=st.number_input('Work Life Balance (1-5)')

with right_column:
    # years at company
    yac=st.number_input('Years at Company')

left_column,middle_column,right_column=st.columns(3)
with left_column:
    # years in current role
    ycr=st.number_input('Years in Current Role')

with middle_column:
    # years since last promotion
    yslp=st.number_input('Years Since Last Promotion')

with right_column:
    # years with curr manager
    ycm=st.number_input('Years with Current Manager')

if st.button("Predict Attrition"):
    if ot=="Yes":
        ot=1
    else:
        ot=0

    if ed=='Below College':
        ed=1
    elif ed=='College':
        ed=2
    elif ed=='Bachelor':
        ed=3
    elif ed=='Master':
        ed=4
    else:
        ed=5
    
    query=np.array([age,bt,dt,dept,dfh,ed,edf,es,gender,hr,je,jl,jr,js,ms,mi,mr,nmw,ot,psh,pr,rs,sol,twy,tyl,wlb,yac,ycr,yslp,ycm])

    query=query.reshape(1, 30)
    ans=pipe.predict(query)[0]
    if ans==1:
        st.title("The Predicted Attrition of Employee = Yes")
    else:
        st.title("The Predicted Attrition of Employee = No")
    