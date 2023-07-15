# import necessary libraries
import pickle #loading the saved models
import streamlit as st #to create app
from streamlit_option_menu import option_menu # to display options


# loading models

dia_model = pickle.load(open("Diabetes.sav", 'rb'))
heart_model = pickle.load(open("Heart.sav", 'rb'))
park_model = pickle.load(open("Parkinsons.sav", 'rb'))

# sidebar for navigation
with st.sidebar:

    selected = option_menu('E- Doctor Multiple Disease Prediction System', 
                           
                           ['Diabetes Prediction', 
                            'Heart Prediction', 
                            'Parkinsons Prediction'],
                            icons=['activity', 'heart', 'person'],
                            default_index=0)
# in option menu we first gave the heading and then array of options we want
# and the icons to be displayed all this is stored in selected variable


# Diabetes Prediction Page
if(selected == 'Diabetes Prediction') :
    
    # page title
    st.title("Diabetes Prediction using ML")

    # getting input data from the user
    col1, col2, col3 = st.columns(3)
    # all labels will be displayed in 3 cols
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Levels')

    with col3:
        BloodPressure = st.text_input('Blood Pressure Level')

    # it will automatically go to next level
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI Value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')

    with col2:
        Age = st.text_input('Age of the person')

    # code for predictions
diab_diagnosis =''

    # creating button for  prediction
if st.button('Diabetes Test Result'): #st.button makes a button
    diab_prediction = dia_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])


    if (diab_prediction[0] == 1):
        diab_diagnosis = 'The person is Diabetic'
    else:
        diab_diagnosis = 'The person is Not Diabetic'

st.success(diab_diagnosis)

# if heart disease selected
if(selected == 'Heart Prediction') :
    
    # page title
    st.title("Heart Disease Prediction using ML")

    # getting input data from the user
    col1, col2, col3 = st.columns(3)
    # all labels will be displayed in 3 cols
    with col1:
        Age = st.text_input('Age')
    
    with col2:
        Sex = st.text_input('Sex')
    
    with col3:
        CP = st.text_input('Chest Pain Value')

    with col1:
        Restbps = st.text_input('Resting Blood Pressure')

    with col2:
        Chol = st.text_input('Serum Cholestoral in mg/dL')
    
    with col3:
        Fbs = st.text_input('Fasting Blood Sugar>120 mg/dL')

    with col1:
        Restecg = st.text_input('Resting Electorcardiographic results')

    with col2:
        Thalach = st.text_input('Maximum Heart Rate Achieved')

    with col3:
       Exang = st.text_input('Exercise Induced Angina')

    with col1:
        Oldpeak = st.text_input('ST depression Indeuced by exercise')

    with col2:
        Slope = st.text_input('Slope of peak exercise ST segment')

    with col3:
        Ca = st.text_input('Major vessels colored by Fluorosopy')
    
    with col1:
        Thal = st.text_input('THAL:   0 = Normal; 1 = Fixed defect; 2 = Reversable defect')

    # code for predictions
heart_diagnosis =''

    # creating button for  prediction
if st.button('Heart Test Result'): #st.button makes a button
    heart_predicition = heart_model.predict([[Age, Sex, CP, Restbps, Chol, Fbs, Restecg,
                                               Thalach, Exang, Oldpeak, Slope, Ca, Thal]])


    if (heart_predicition[0] == 1):
        heart_diagnosis = 'The person is Heart Disease Affected'
    else:
        heart_diagnosis = 'The person is Not Heart Disease Affected'

st.success(heart_diagnosis)

# if parkinson selected
if(selected == 'Parkinsons Prediction') :
    
    # page title
    st.title("Parkinsons Disease Prediction using ML")

    # getting input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)
    # all labels will be displayed in 3 cols
    with col1:
        MDVPFo = st.text_input('MDVP:Fo(Hz)')
    
    with col2:
        MDVPFhi = st.text_input('MDVP:Fhi(Hz)')
    
    with col3:
        MDVPFlo = st.text_input('# MDVP:Flo(Hz)')

    with col4:
        MDVPJitter = st.text_input('MDVP:Jitter(%)')

    with col5:
        CMDVPJitter = st.text_input('MDVP:Jitter(Abs)')
    
    with col1:
        MDVPRAP = st.text_input('MDVP:RAP')

    with col2:
        MDVPPPQ = st.text_input('MDVP:PPQ')

    with col3:
        JitterDDP = st.text_input('Jitter:DDP')

    with col4:
        MDVPShimmer = st.text_input('MDVP:Shimmer')

    with col5:
        MDVPShimmer = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        ShimmerAPQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        ShimmerAPQ5 = st.text_input('Shimmer:APQ5')
    
    with col2:
        MDVPAPQ = st.text_input('MDVP:APQ')

    with col3:
        ShimmerDDA = st.text_input('Shimmer:DDA')
    
    with col4:
        NHR = st.text_input('NHR')
    
    with col5:
        HNR = st.text_input('HNR')
    
    with col1:
        RPDE = st.text_input('RPDE')

    with col2:
        DFA = st.text_input('DFA')

    with col3:
        spread1 = st.text_input('Spread1')
    
    with col4:
        spread2 = st.text_input('Spread2')

    with col5:
        D2 = st.text_input('D2')

    with col1:
        PPE = st.text_input('PPE')
    # code for predictions
park_diagnosis =''

    # creating button for  prediction
if st.button('Parkinson Test Result'): #st.button makes a button
    park_predicition = park_model.predict([[ MDVPFo, MDVPFhi, MDVPFlo, MDVPJitter, 
                                                MDVPJitter, MDVPRAP, MDVPPPQ, JitterDDP,
                                                MDVPShimmer, MDVPShimmer, ShimmerAPQ3,
                                                ShimmerAPQ5, MDVPAPQ, ShimmerDDA, 
                                                NHR, HNR, RPDE, DFA, spread1, spread2,
                                                D2, PPE]])


    if (park_predicition[0] == 1):
        park_diagnosis = 'The person is Parkinson Disease Affected'
    else:
        park_diagnosis = 'The person is Not Parkinson Disease Affected'

st.success(park_diagnosis)
