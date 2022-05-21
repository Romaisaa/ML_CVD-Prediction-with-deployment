import pickle
import streamlit as st
import numpy as np
from helper import converter


model = pickle.load(open("./static/model.sav",'rb'))
def main():
    st.set_page_config(page_title="Cardiovascular Diseas Prediction")
    col1, col2 =  st.columns([20, 30])
    with st.container():
            with col1:
                st.title(" Weclome to CVD check up")
            with col2:
                st.image("./static/logo.png", width=400)

    with st.container():
        st.subheader("Check your health Easily with us")
        st.write("Please, Answer the following honstly")

    #input Var
    age = int(st.number_input("Age", min_value=0,step=1, format="%d"))
    gender = st.selectbox("Gender",(" ","Male","Female"))
    height= int(st.number_input("Height", min_value=0,step=1, format="%d"))
    weight= int(st.number_input("Weight", min_value=0,step=1, format="%d"))
    ap_hi= int(st.number_input("Systolic blood pressure ", min_value=0,step=1, format="%d"))
    ap_lo= int(st.number_input("Diastolic blood pressure", min_value=0,step=1, format="%d"))
    cholestrol =st.selectbox("Cholestrol Level",(" ","Normal","Above Normal","Well Above Normal")) 
    glucose=st.selectbox("Glucose Level",(" ","Normal","Above Normal","Well Above Normal")) 
    smoke = st.radio("Are You a Smoker?",("Yes","No"))
    alco = st.radio("Do you drink Alcohol?",("Yes","No"))
    active = st.radio("Do you usually do physical activities?",("Yes","No")) 

    if st.button("Check"):
        if cholestrol==" " or glucose==" " or gender==" " or age== 0 or height==0 or weight==0 or ap_lo==0 or ap_hi==0 :
            st.write("**Please Fill all required data**")
        else:
            gender = 1 if gender == 'Male' else 2
            smoke = 1 if smoke == 'Yes' else 0
            alco = 1 if alco == 'Yes' else 0
            active = 1 if active == 'Yes' else 0
            features =np.array([[age,gender,height,weight,ap_hi,ap_lo,converter(cholestrol),converter(glucose),smoke,alco,active]])
            result = model.predict(features)
            if(result == [0]): 
                st.markdown("<h1 style='text-align: center; color: #187498;'>Thanks God, You don't need to worry ✅ </h1>", unsafe_allow_html=True) 
            else: 
                st.markdown("<h1 style='text-align: center; color: #FF5D5D;'>Sorry for news, but you need to see a doctor 🚨</h1>", unsafe_allow_html=True) 


if __name__=="__main__":
    main()





